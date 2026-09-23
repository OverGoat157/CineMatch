import pytest

from ratings import cancel_rating, is_rated, rate_movie, recommend_movies


def test_rate_movie():
    ratings = []
    rate_movie(ratings, 1, 9)
    assert is_rated(ratings, 1)


def test_duplicate_rating_forbidden():
    ratings = []
    rate_movie(ratings, 1, 9)
    with pytest.raises(ValueError):
        rate_movie(ratings, 1, 7)


def test_score_out_of_range():
    with pytest.raises(ValueError):
        rate_movie([], 1, 11)


def test_cancel_rating():
    ratings = []
    rate_movie(ratings, 1, 9)
    assert cancel_rating(ratings, 1)
    assert not is_rated(ratings, 1)


def test_recommend_movies_skips_rated_and_unsuitable():
    movies = [
        {"id": 1, "title": "A", "genre": "Драма", "rating": 9.0},
        {"id": 2, "title": "B", "genre": "Драма", "rating": 7.0},
        {"id": 3, "title": "C", "genre": "Драма", "rating": 8.5},
    ]
    user = {"favorite_genre": "Драма", "min_rating": 8.0}
    ratings = [{"movie_id": 1, "score": 10}]
    recommended = recommend_movies(movies, ratings, user)
    assert [movie["id"] for movie in recommended] == [3]
