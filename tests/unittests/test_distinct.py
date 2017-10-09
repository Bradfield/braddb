import unittest

from executor.executor import tree, execute
from executor.distinct import Distinct
from executor.memscan import MemScan


class TestDistinct(unittest.TestCase):
    """
    Test that distinct can filter records with repeated values.
    """
    def test_distinct_sorted(self):
        """
        Typical case: expect input to be sorted.
        """
        records = [tuple([n]) for n in (0, 0, 1, 2, 2, 2, 3, 3)]
        query = tree(
            [Distinct(),
                [MemScan(records)]])
        result = list(execute(query))
        self.assertListEqual(result, [tuple([n]) for n in (0, 1, 2, 3)])

    def test_distinct_unsorted(self):
        """
        Distinct is not expected to handle out-of-order repeated values.
        """
        records = [tuple([n]) for n in (0, 1, 1, 0, 0, 1, 1, 1)]
        query = tree(
            [Distinct(),
                [MemScan(records)]])
        result = list(execute(query))
        self.assertListEqual(result, [tuple([n]) for n in (0, 1, 0, 1)])
