from movies import (
    add_movie,
    filter_movies_by_genre,
    find_movies,
    sort_movies,
)


def make_movies():
    movies = []
    add_movie(movies, "Интерстеллар", "Фантастика", 2014, 8.6, 169)
    add_movie(movies, "Побег из Шоушенка", "Драма", 1994, 9.3, 142)
    add_movie(movies, "Матрица", "Фантастика", 1999, 8.7, 136)
    return movies


def test_add_movie_assigns_next_id():
    movies = make_movies()
    movie = add_movie(movies, "Начало", "Фантастика", 2010, 8.8, 148)
    assert movie["id"] == 4
    assert len(movies) == 4


def test_find_movies_ignores_case():
    movies = make_movies()
    found = find_movies(movies, "матрица")
    assert [movie["title"] for movie in found] == ["Матрица"]


def test_filter_movies_by_genre():
    movies = make_movies()
    titles = [m["title"] for m in filter_movies_by_genre(movies, "Драма")]
    assert titles == ["Побег из Шоушенка"]


def test_sort_movies_by_rating_desc():
    movies = make_movies()
    ratings = [movie["rating"] for movie in sort_movies(movies)]
    assert ratings == [9.3, 8.7, 8.6]
