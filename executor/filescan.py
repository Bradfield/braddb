import csv

from .base import PlanNode


class FileScan(PlanNode):
    """
    Read from disk and yield records individually to parent.
    """
    def __init__(self, table_name, record_type):
        self.record_type = record_type
        self.fp = open(table_name, 'r')
        # TODO eventually move away from CSV as the data file format
        self.reader = csv.reader(self.fp)
        next(self.reader)  # consume first row - column names

    def __next__(self):
        row = next(self.reader)
        return self.record_type(*row)

    def __del__(self):
        self.fp.close()
