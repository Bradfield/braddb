from .base import PlanNode
from sorting import external_sort


class Sort(PlanNode):
    """
    Sort records out-of-core, by a given key fuction.
    """
    def __init__(self, key):
        super().__init__()
        self.key = key
        self.records = None

    def __next__(self):
        # if no records have been yielded, consume child's records and sort
        if self.records is None:
            self.records = external_sort(self._inputs[0], self.key)

        return next(self.records)
