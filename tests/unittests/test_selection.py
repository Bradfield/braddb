import unittest

from executor.executor import tree, execute
from executor.memscan import MemScan
from executor.selection import Selection


class TestSelection(unittest.TestCase):
    """
    Test the selection plan node, which is effectively a filter operation.
    """
    def test_select_various_predicates(self):
        predicates = [
            lambda r: r[0] % 2 == 1,  # odd values
            lambda r: r[1] % 2 == 1,  # odd squares
            lambda r: r[0] + r[1] == 30,  # just (5, 25)
            lambda r: r[1] == 'Reginald',  # no records
        ]
        records = [(n, n*n) for n in range(10)]
        for p in predicates:
            query = tree(
                [Selection(p),
                    [MemScan(records)]])
            result = list(execute(query))
            expected = [r for r in records if p(r)]
            self.assertListEqual(result, expected)
