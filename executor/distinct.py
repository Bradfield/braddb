from .base import PlanNode


class Distinct(PlanNode):
    """
    Assuming sorted input, stream out distinct output.
    """
    def __init__(self):
        super().__init__()
        self.prior = None
        self.finished = False

    def __next__(self):
        while True:
            record = next(self._inputs[0])
            if record != self.prior:
                self.prior = record
                return record
