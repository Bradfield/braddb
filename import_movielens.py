"""
The movielens database is provided in CSV, but we'd like to use our own
binary on-disk representation. This script converts from one to the other.

The tables covered at this point are movies and ratings.
"""

import csv

from access.heap import heap_write
from hacky_hardcoded_schema import movie_schema, rating_schema

movies_file = 'movielens-database/movies.csv'
ratings_file = 'movielens-database/ratings.csv'

movies = ('movies', movie_schema, lambda r: (int(r[0]), r[1][:80], r[2][:80]))
ratings = (
    'ratings',
    rating_schema,
    lambda r: (int(r[0]), int(r[1]), float(r[2]), int(r[3]))
)

if __name__ == '__main__':
    for name, schema, t_conv in (movies, ratings):
        filename = 'movielens-database/{}.csv'.format(name)
        with open(filename, 'r+') as f:
            reader = csv.reader(f)
            next(reader)  # consume first row - column names

            # rows = []
            # tids = []

            for csv_row in reader:
                row = t_conv(csv_row)
                serialized = schema.serialize(row)
                # rows.append(movie_schema.deserialize(serialized))
                block_number, offset = heap_write(name, serialized)
                # tids.append((block_number, offset))

            # # read back to verify
            # for i, tid in enumerate(tids):
            #     block_number, offset = tid
            #     row_bytes = heap_read(
            #         name,
            #         schema.width,
            #         block_number,
            #         offset
            #     )
            #     deserialized = schema.deserialize(row_bytes)
            #     assert rows[i] == deserialized
