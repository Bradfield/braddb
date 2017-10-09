from .base import PlanNode


class Projection(PlanNode):
    """
    Yield tuples mapped by the given function
    """
    def __init__(self, mapping):
        super().__init__()
        self.mapping = mapping

    def __next__(self):
        record = next(self._inputs[0])
        return tuple(self.mapping(record))
