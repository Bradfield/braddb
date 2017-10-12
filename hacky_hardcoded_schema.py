from collections import namedtuple

from access.schema import Schema, Int32, Char, Float32

MovieRecord = namedtuple('MovieRecord', ('id', 'name', 'genres'))
RatingRecord = namedtuple('RatingRecord',
                          ('user_id', 'movie_id', 'rating', 'timestamp'))

movie_schema = Schema((
    ('id', Int32()),
    ('name', Char(100)),
    ('genres', Char(100)),
))

rating_schema = Schema((
    ('user_id', Int32()),
    ('movie_id', Int32()),
    ('rating', Float32()),
    ('timestamp', Int32()),
))
