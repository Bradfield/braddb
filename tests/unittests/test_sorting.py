import unittest

from sorting import external_sort


class TestExternalSorting(unittest.TestCase):
    """
    Do a simple out-of-core sort of records with single integers.
    """
    def test_external_sort(self):
        records = [(1,), (4,), (2,), (3,), (1,), (5,), (3,), (6,), (9,)]
        result = external_sort(
            iter(records),
            lambda r: r[0],
            max_records_per_file=2
        )
        self.assertListEqual(list(result), sorted(records))


if __name__ == '__main__':
    unittest.main()
