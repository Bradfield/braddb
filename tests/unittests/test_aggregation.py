import unittest

from executor.executor import tree, execute
from executor.aggregation import Count, Average
from executor.memscan import MemScan
from executor.projection import Projection
from executor.selection import Selection


# For test records, use the first 10 numbers and their squares.
_RECORDS = [(n, n*n) for n in range(10)]

_PREDICATES = [
    lambda r: r[0] % 2 == 1,  # odd values
    lambda r: r[1] % 2 == 1,  # odd squares
    lambda r: r[0] + r[1] == 30,  # just (5, 25)
    lambda r: r[1] == 'Reginald',  # no records
]


class TestCount(unittest.TestCase):
    """
    Test count aggregation, which simply counts input records.
    """
    def test_count_all(self):
        """
        Test simply counting everything.
        """
        query = tree(
            [Count(),
                [MemScan(_RECORDS)]])
        result = list(execute(query))
        self.assertListEqual(result, [tuple([10])])

    def test_count_selected(self):
        """
        Test counting the output of a selection.
        """
        for p in _PREDICATES:
            query = tree(
                [Count(),
                    [Selection(p),
                        [MemScan(_RECORDS)]]])
            result = list(execute(query))
            expected = [tuple([len([r for r in _RECORDS if p(r)])])]
            self.assertListEqual(result, expected)


class TestAverage(unittest.TestCase):
    """
    Test the average aggregation, which simply takes the mean of input values.
    """
    def test_average_all(self):
        """
        Find the average of all numbers 0..9
        """
        query = tree(
            [Average(),
                [Projection(lambda r: [r[0]]),
                    [MemScan(_RECORDS)]]])
        result = list(execute(query))
        self.assertListEqual(result, [tuple([4.5])])

    def test_average_selected(self):
        """
        Find the average of only filtered numbers in the range 0..9
        """
        query = tree(
            [Average(),
                [Projection(lambda r: [r[0]]),
                    [Selection(lambda r: r[0] % 2 == 1),
                        [MemScan(_RECORDS)]]]])
        result = list(execute(query))
        self.assertListEqual(result, [tuple([5])])
