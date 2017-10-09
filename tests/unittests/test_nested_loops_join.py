import unittest

from executor.executor import tree, execute
from executor.memscan import MemScan
from executor.nested_loops_join import NestedLoopsJoin


class TestNestedLoopsJoin(unittest.TestCase):
    """
    Test our most basic join: nested loops with optional theta function.
    """
    R_RECORDS = (
        (0, 'a'),
        (1, 'b'),
        (1, 'c'),
        (2, 'c'),
    )
    S_RECORDS = (
        ('a', 'apple'),
        ('b', 'banana'),
        ('b', 'burger'),
    )

    def test_cartesian_product(self):
        """
        When the theta function simply returns True, we achieve cross product.
        """
        query = tree(
            [NestedLoopsJoin(lambda r, s: True),
                [MemScan(self.R_RECORDS)],
                [MemScan(self.S_RECORDS)]])
        result = list(execute(query))
        expected = [r + s for r in self.R_RECORDS for s in self.S_RECORDS]
        self.assertListEqual(result, expected)

    def test_self_join(self):
        """
        It's fine for a table to be joined to itself.
        """
        query = tree(
            [NestedLoopsJoin(lambda r, s: True),
                [MemScan(self.R_RECORDS)],
                [MemScan(self.R_RECORDS)]])
        result = list(execute(query))
        expected = [r + s for r in self.R_RECORDS for s in self.R_RECORDS]
        self.assertListEqual(result, expected)

    def test_equijoin(self):
        """
        The join condition can be that the value in one field equals another.
        """
        query = tree(
            [NestedLoopsJoin(lambda r, s: r[1] == s[0]),
                [MemScan(self.R_RECORDS)],
                [MemScan(self.S_RECORDS)]])
        result = list(execute(query))
        expected = [
            (0, 'a', 'a', 'apple'),
            (1, 'b', 'b', 'banana'),
            (1, 'b', 'b', 'burger')
        ]
        self.assertListEqual(result, expected)

    def test_inequality(self):
        """
        The join condition can be an inequality.
        """
        query = tree(
            [NestedLoopsJoin(lambda r, s: r[0] > s[0]),
                [MemScan(self.R_RECORDS)],
                [MemScan(self.R_RECORDS)]])
        result = list(execute(query))
        expected = [
            (1, 'b', 0, 'a'),
            (1, 'c', 0, 'a'),
            (2, 'c', 0, 'a'),
            (2, 'c', 1, 'b'),
            (2, 'c', 1, 'c'),
        ]
        self.assertListEqual(result, expected)

    def test_three_way(self):
        """
        The input to a join can be a join.
        """
        query = tree(
            [NestedLoopsJoin(lambda r, s: r[3] == s[0]),
                [NestedLoopsJoin(lambda r, s: r[0] > s[0]),
                    [MemScan(self.R_RECORDS)],
                    [MemScan(self.R_RECORDS)]],
                [MemScan(self.S_RECORDS)]])
        result = list(execute(query))
        expected = [
            (1, 'b', 0, 'a', 'a', 'apple'),
            (1, 'c', 0, 'a', 'a', 'apple'),
            (2, 'c', 0, 'a', 'a', 'apple'),
            (2, 'c', 1, 'b', 'b', 'banana'),
            (2, 'c', 1, 'b', 'b', 'burger'),
        ]
        self.assertListEqual(result, expected)
