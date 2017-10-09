from .base import PlanNode


class Selection(PlanNode):
    """
    Yield only tuples for which the given predicate returns True.
    """
    def __init__(self, predicate):
        super().__init__()
        self.predicate = predicate

    def __next__(self):
        while True:
            record = next(self._inputs[0])
            if self.predicate(record):
                return record
