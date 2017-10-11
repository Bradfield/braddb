from collections import namedtuple

movies_file = 'movielens-database/movies.csv'
ratings_file = 'movielens-database/ratings.csv'

MovieRecord = namedtuple('MovieRecord', ('id', 'name', 'genres'))
RatingRecord = namedtuple('RatingRecord',
                          ('user_id', 'movie_id', 'rating', 'timestamp'))
