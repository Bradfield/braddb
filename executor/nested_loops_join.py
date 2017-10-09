from .base import PlanNode


class NestedLoopsJoin(PlanNode):
    """
    Return records across two input relational instances.

    Requires a theta function, the truth set of which determines the records
    to be joined.

    TODO: this is super slow! Rather than re-reading all of S for each record
    in R, we should be utilizing extra RAM and reading B-2 pages of R at a
    time (where B is the total capacity of pages). This is known as block
    or chunk nested loops join.
    """
    def __init__(self, theta):
        super().__init__()
        self.theta = theta
        self._current_r = None

    def __next__(self):
        R = self._inputs[0]
        S = self._inputs[1]
        r = self._current_r = self._current_r or next(R)
        while True:
            for s in S:
                if self.theta(r, s):
                    return r + s
            S.reset()
            r = self._current_r = next(R)
