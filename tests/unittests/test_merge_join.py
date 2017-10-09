import unittest

from executor.executor import tree, execute
from executor.memscan import MemScan
from executor.merge_join import MergeJoin


class TestMergeJoin(unittest.TestCase):
    """
    Test a join of larger relations, where sorted inputs are merged together.
    """
    R_RECORDS = (
        (0, 'a'),
        (1, 'b'),
        (1, 'c'),
        (2, 'c'),
        (3, 'd')
    )
    S_RECORDS = (
        ('a', 'apple'),
        ('b', 'banana'),
        ('b', 'burger'),
        ('d', 'domato'),
    )

    def test_equijoin(self):
        """
        The a simple join by field field value.
        """
        query = tree(
            [MergeJoin(lambda r: r[1], lambda s: s[0]),
                [MemScan(self.R_RECORDS)],
                [MemScan(self.S_RECORDS)]])
        result = list(execute(query))
        expected = [
            (0, 'a', 'a', 'apple'),
            (1, 'b', 'b', 'banana'),
            (1, 'b', 'b', 'burger'),
            (3, 'd', 'd', 'domato'),
        ]
        self.assertListEqual(result, expected)

    def test_self_join(self):
        """
        It's fine for a table to be joined to itself.
        """
        query = tree(
            [MergeJoin(lambda r: r[0], lambda s: s[0]),
                [MemScan(self.S_RECORDS)],
                [MemScan(self.S_RECORDS)]])
        result = list(execute(query))
        expected = [
            ('a', 'apple', 'a', 'apple'),
            ('b', 'banana', 'b', 'banana'),
            ('b', 'banana', 'b', 'burger'),
            ('b', 'burger', 'b', 'banana'),
            ('b', 'burger', 'b', 'burger'),
            ('d', 'domato', 'd', 'domato'),
        ]
        self.assertListEqual(result, expected)

    def test_three_way(self):
        """
        The input to a join can be a join.
        """
        query = tree(
            [MergeJoin(lambda r: r[1], lambda s: s[0]),
                [MemScan(self.R_RECORDS)],
                [MergeJoin(lambda r: r[0], lambda s: s[0]),
                    [MemScan(self.S_RECORDS)],
                    [MemScan(self.S_RECORDS)]]])
        result = list(execute(query))
        expected = [
            (0, 'a', 'a', 'apple', 'a', 'apple'),
            (1, 'b', 'b', 'banana', 'b', 'banana'),
            (1, 'b', 'b', 'banana', 'b', 'burger'),
            (1, 'b', 'b', 'burger', 'b', 'banana'),
            (1, 'b', 'b', 'burger', 'b', 'burger'),
            (3, 'd', 'd', 'domato', 'd', 'domato'),
        ]
        self.assertListEqual(result, expected)
