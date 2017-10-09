from .base import PlanNode


class MemScan(PlanNode):
    """
    A plan node that scans over records in memory.

    This is intended to behave equivalently to FileScan, but
    over a list of input records rather than reading from disk.
    """
    def __init__(self, items):
        super().__init__()
        self.items = items
        self.reset()

    def __next__(self):
        return next(self._iterable)

    def reset(self):
        self._iterable = iter(self.items)
