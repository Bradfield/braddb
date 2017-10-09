import unittest

from executor.aggregation import Average, Count
from executor.distinct import Distinct
from executor.filescan import FileScan
from executor.executor import execute, tree
from executor.projection import Projection
from executor.selection import Selection
from executor.sort import Sort
from hacky_hardcoded_schema import (
    MovieRecord,
    movies_file,
    RatingRecord,
    ratings_file,
)


class TestBasicSingleTableQueries(unittest.TestCase):
    """
    Test the examples given in the project instructions.
    """

    def test_select_by_id(self):
        """
        What is the name of the movie with id 5000?
        """
        query = tree([
            Projection(lambda r: tuple([r.name])), [
                Selection(lambda r: r.id == '5000'), [
                    FileScan(movies_file, MovieRecord)]]])
        self.assertListEqual(['Medium Cool (1969)'],
                             [r[0] for r in execute(query)])

    def test_average_rating(self):
        """
        What is the average rating for movie with id 5000?

        WARNING: super slow
        """
        query = tree([
            Average(), [
                Projection(lambda r: tuple([float(r.rating)])), [
                    Selection(lambda r: r.movie_id == '5000'), [
                        FileScan(ratings_file, RatingRecord)]]]])
        self.assertAlmostEqual(3.5, next(execute(query))[0], places=2)

    def test_count_rated_movies(self):
        """
        How many distinct movies have a rating?

        WARNING: super slow
        """
        query = tree([
            Count(), [
                Distinct(), [
                    Sort(lambda r: r[0]), [
                        Projection(lambda r: tuple([r.movie_id])), [
                            FileScan(ratings_file, RatingRecord)]]]]])
        # TODO: shouldn't this be 26744?
        self.assertEqual(26745, next(execute(query))[0])
