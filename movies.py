"""Функции для работы с каталогом фильмов."""

from datetime import date


def add_movie(
    movies: list[dict],
    title: str,
    genre: str,
    year: int,
    rating: float,
    duration: int,
) -> dict:
    """Добавить фильм в каталог и вернуть его запись."""
    movie_id = max((movie["id"] for movie in movies), default=0) + 1
    movie = {
        "id": movie_id,
        "title": title,
        "genre": genre,
        "year": year,
        "rating": rating,
        "duration": duration,
    }
    movies.append(movie)
    return movie


def get_movie(movies: list[dict], movie_id: int) -> dict | None:
    """Найти фильм по идентификатору."""
    for movie in movies:
        if movie["id"] == movie_id:
            return movie
    return None


def find_movies(movies: list[dict], query: str) -> list[dict]:
    """Найти фильмы, в названии которых есть подстрока query."""
    query = query.lower()
    return [movie for movie in movies if query in movie["title"].lower()]


def filter_movies_by_genre(movies: list[dict], genre: str):
    """Генератор фильмов заданного жанра."""
    for movie in movies:
        if movie["genre"].lower() == genre.lower():
            yield movie


def sort_movies(movies: list[dict], key: str = "rating") -> list[dict]:
    """Вернуть фильмы, отсортированные по полю key по убыванию."""
    return sorted(movies, key=lambda movie: movie[key], reverse=True)


def count_by_genre(movies: list[dict]) -> dict[str, int]:
    """Посчитать количество фильмов в каждом жанре."""
    stats: dict[str, int] = {}
    for movie in movies:
        stats[movie["genre"]] = stats.get(movie["genre"], 0) + 1
    return stats


def format_movie_card(movie: dict) -> str:
    """Собрать строку карточки фильма (сценарий из ПР1)."""
    hours = movie["duration"] // 60
    minutes = movie["duration"] % 60
    movie_age = date.today().year - movie["year"]
    return (
        f"{movie['id']}. {movie['title']} ({movie['year']}), "
        f"жанр: {movie['genre']}, рейтинг: {movie['rating']}, "
        f"{hours} ч {minutes} мин, фильму {movie_age} лет"
    )
