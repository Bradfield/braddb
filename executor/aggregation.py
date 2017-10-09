from .base import PlanNode


class Aggregation(PlanNode):
    """
    A generic aggeregation plan node interface.

    Set `initial`, `transition` and `finalize` to implement specific
    aggregations.
    """
    def __init__(self, initial, transition, finalize):
        super().__init__()
        self.finished = False
        self.initial = initial
        self.transition = transition
        self.finalize = finalize

    def __next__(self):
        if self.finished:
            raise StopIteration

        state = self.initial()
        for record in self._inputs[0]:
            state = self.transition(state, record)
        self.finished = True
        return tuple([self.finalize(state)])


class Count(Aggregation):
    """
    Simply count all input records.

    To only count records for which a given field is not null (ie to perform
    a `COUNT(foo)` rather than `COUNT(*)`) use a `Selection` as input.
    """
    def __init__(self):
        super().__init__(
            initial=lambda: 0,
            transition=lambda s, r: s + 1,
            finalize=lambda s: s
        )


class Average(Aggregation):
    """
    Average all the input records.

    Assumes that each record is a numeric 1-tuple. It's the caller's
    responsibility to ensure that `Projection` is used to satisfy this
    constraint.

    Does not handle division by zero in the case of zero input records.
    """
    def __init__(self):
        super().__init__(
            initial=lambda: (0, 0),
            transition=lambda s, r: (s[0] + r[0], s[1] + 1),
            finalize=lambda s: s[0] / s[1]
        )
