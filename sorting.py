import pickle
from struct import pack, unpack
from uuid import uuid4


MAX_RECORDS_PER_FILE = 5000000  # TODO should be based on bytes, not n


def _write(f, r):
    """
    Serialize and write a length-prefixed record to the given file handle.
    """
    serialized = pickle.dumps(r)
    f.write(pack('H', len(serialized)))  # write length as unsigned short
    f.write(serialized)


def _read(f):
    """
    Read and deserialize a record from the given file handle.
    """
    length_b = f.read(2)
    if not length_b:
        return None
    length = unpack('H', length_b)[0]
    return pickle.loads(f.read(length))


def _dump_partition(partition):
    filename = '/tmp/part-{}'.format(uuid4())
    with open(filename, 'wb') as f:
        for record in partition:
            _write(f, record)
    return filename


def _merge(filenames, key, level=0):
    n = len(filenames)

    if n == 1:
        return filenames[0]

    left = _merge(filenames[:n//2], key, level + 1)
    right = _merge(filenames[n//2:], key, level + 1)
    out = '/tmp/{}-{}'.format(level, uuid4())
    fl = open(left, 'rb')
    fr = open(right, 'rb')
    fout = open(out, 'wb')
    lowest_left = _read(fl)
    lowest_right = _read(fr)
    left_finished = False
    right_finished = False

    while not left_finished or not right_finished:
        if left_finished:
            _write(fout, lowest_right)
            lowest_right = _read(fr)
            if not lowest_right:
                right_finished = True
        elif right_finished:
            _write(fout, lowest_left)
            lowest_left = _read(fl)
            if not lowest_left:
                left_finished = True
        elif key(lowest_left) < key(lowest_right):
            _write(fout, lowest_left)
            lowest_left = _read(fl)
            if not lowest_left:
                left_finished = True
        else:
            _write(fout, lowest_right)
            lowest_right = _read(fr)
            if not lowest_right:
                right_finished = True

    fl.close()
    fr.close()
    fout.close()
    return out


def external_sort(records, key, max_records_per_file=MAX_RECORDS_PER_FILE):
    """
    Perform an out-of-core sort on the stream of given records.

    Reads some number of records into memory, sorts them then writes to
    temporary files for later merging.

    TODO: clean up after oneself.
    """
    partition = []
    filenames = []
    total_records = 0
    while True:
        try:
            partition.append(next(records))
            total_records += 1
        except StopIteration:
            break
        if len(partition) == max_records_per_file:
            # a partition has reached capacity, so dump it
            partition.sort(key=key)
            filenames.append(_dump_partition(partition))
            partition = []

    if len(partition) > 0:
        # dump also the final partition
        partition.sort(key=key)
        filenames.append(_dump_partition(partition))

    outfile = _merge(filenames, key)
    with open(outfile, 'rb') as f:
        for _ in range(total_records):
            record = _read(f)
            if not record:
                break
            yield record
