from itertools import product, starmap

from .base import PlanNode


class MergeJoin(PlanNode):
    """
    Return records across two sorted input relational instances.

    Requires a theta function, the truth set of which determines the records
    to be joined.

    Here we assume that both inputs are already in sorted order. Providing
    unsorted inputs will yield surprising results.

    We also assume that the join is an equijoin. The interface for specifying
    the join condition is a little dorky for now, to simplify our logic:
    we require two functions, the first of which is called on R records, and
    the latter on S records. A joined record is yielded when both functions
    return the same values. An inequality should use NestedLoopsJoin.

    There is effectively a small nested loops join for the subset of
    records from one relation and another where the join condition is met,
    for which records from both tables are buffered into memory. TODO this
    simply assumes that there's suffiicent memory to do so.
    """
    def __init__(self, r_key, s_key):
        super().__init__()
        self.r_key = r_key
        self.s_key = s_key
        self._r_next = None
        self._s_next = None
        self._buffer = None
        self._last_io_finished = False
        self._finished = False

    def __next__(self):
        if self._finished:
            raise StopIteration

        R = self._inputs[0]
        S = self._inputs[1]

        # step 1 - load r and s buffers with records from R and S for which
        # their respective key functions return the same values
        r = self._r_next = self._r_next or next(R)
        self._s_next = self._s_next or next(S)
        if not self._buffer:
            r_buff = [r]
            s_buff = []
            while True:
                # the r buffer simply contains all adjacent R records with
                # the same r key return value
                try:
                    self._r_next = next(R)
                except StopIteration:
                    self._last_io_finished = True
                    break
                if self.r_key(self._r_next) != self.r_key(r):
                    break
                r_buff.append(self._r_next)
            while True:
                # the s buffer contains all S records for which the s key
                # returns a value that equals that of the buffered R records
                if self.s_key(self._s_next) > self.r_key(r):
                    break
                if self.s_key(self._s_next) == self.r_key(r):
                    s_buff.append(self._s_next)
                try:
                    self._s_next = next(S)
                except StopIteration:
                    break
            # construct an iterable of the cartesian product, constituting
            # the buffer of joined records to yield one by one
            self._buffer = starmap(lambda a, b: a + b, product(r_buff, s_buff))

        # step 2 - with a buffer available, just yield the next record off it
        try:
            return next(self._buffer)
        except StopIteration:
            if self._last_io_finished:
                self._finished = True
            self._buffer = None
            return next(self)
