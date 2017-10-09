import unittest

from executor.executor import tree, execute
from executor.memscan import MemScan
from executor.projection import Projection


class TestProjection(unittest.TestCase):
    """
    Test the projection plan node, which is effectively a map operation.
    """
    def test_project_various(self):
        mapping_functions = [
            lambda r: [r[1]],  # project to a single column
            lambda r: [r[1], r[0]],  # switch columns
            lambda r: [r[0] + r[1]],  # sums of fields
            lambda r: [r[1] > 8],  # results of boolean operations
        ]
        records = [(n, n*n) for n in range(10)]
        for f in mapping_functions:
            query = tree(
                [Projection(f),
                    [MemScan(records)]])
            result = list(execute(query))
            expected = [tuple(f(r)) for r in records]
            self.assertListEqual(result, expected)
