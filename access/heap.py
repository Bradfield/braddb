import struct
import sys

from .constants import BLOCK_SIZE


def heap_read(table_name, width, block_number, offset):
    """
    Just read the bytes specified by the arguments.

    TODO bounds checking and error handling gawd!!
    """
    with open('data/{}.table'.format(table_name), 'rb') as f:
        f.seek(block_number * BLOCK_SIZE + offset)
        return f.read()


def heap_write(table_name, record_bytes):
    """
    Write the given bytes to the _end_ of the specified table.
    """
    filename = 'data/{}.table'.format(table_name)
    # create file if doesn't exist
    open(filename, 'a').close()
    f = open(filename, 'r+b')

    # read starting block to see where next free space is
    block = f.read(BLOCK_SIZE)

    # at the beggining, the file is empty
    if len(block) == 0:
        f.seek(0)
        f.write(b'\0\0\0\0' + struct.pack('I', 8) + b'\0' * (BLOCK_SIZE - 8))
        f.flush()
        f.seek(0)
        block = f.read(BLOCK_SIZE)
        f.seek(0)

    # the first 4 bytes of the first block indicates the block number of the
    # first free block
    block_i, = struct.unpack('I', block[:4])
    if block_i != 0:
        f.seek(block_i * BLOCK_SIZE)
        block = f.read(BLOCK_SIZE)

    # the next 4 bytes indicate the offset into the block at which the next
    # available space is
    offset, = struct.unpack('I', block[4:8])
    # if there's not enough space in the current block, move to the next one
    if offset + len(record_bytes) > BLOCK_SIZE:
        block_i += 1
        f.seek(0)
        f.write(struct.pack('I', block_i))
        f.flush()
        f.seek(block_i * BLOCK_SIZE)
        # TODO probably need to write the next empty block here
        block = f.read(BLOCK_SIZE)
        offset = 8

    # write the record itself
    f.seek(block_i * BLOCK_SIZE + offset)
    n = f.write(record_bytes)
    assert n == len(record_bytes)
    f.flush()
    # update the offset
    f.seek(block_i * BLOCK_SIZE + 4)
    f.write(struct.pack('I', offset + n))
    f.flush()

    f.close()
    return block_i, offset
