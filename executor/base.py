
class PlanNode(object):
    """
    The base class from which all plan nodes should inherit.
    """

    def __init__(self):
        """
        Nodes should implement `__init__` to set their own state, then
        call super init to ensure that `_inputs` exists to be used in plan
        tree construction.
        """
        self._inputs = []

    def __iter__(self):
        """
        Since all plan nodes must have a `__next__`, they can all be iterated
        over like any other Python iterable.
        """
        return self

    def __next__(self):
        """
        All nodes require an interface to return the next record, so that its
        parent can pull them as needed.
        """
        raise NotImplementedError

    def reset(self):
        """
        To support joins, all nodes must have an interface to reset their
        state. This includes join nodes themselves, since they can be the
        inputs to other joins.
        """
        raise NotImplementedError
