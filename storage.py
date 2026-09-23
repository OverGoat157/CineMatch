"""Загрузка и сохранение объектов проекта в JSON-файлах."""

import json

from models import Movie, Rating, User
from models.movies import find_movie_by_id
from models.users import find_user_by_id


def load_json(filename: str, default: list) -> list:
    """Прочитать JSON-файл. При ошибке вернуть default."""
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден, используются данные по умолчанию")
        return default
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён, используются данные по умолчанию")
        return default


def save_json(filename: str, data: list) -> None:
    """Записать данные в JSON-файл."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def load_movies(filename: str) -> list[Movie]:
    """Загрузить фильмы и превратить каждую запись в объект Movie."""
    return [Movie.from_data(data) for data in load_json(filename, [])]


def save_movies(filename: str, movies: list[Movie]) -> None:
    """Сохранить объекты Movie в JSON."""
    save_json(
        filename,
        [
            {
                "id": movie.id,
                "title": movie.title,
                "genre": movie.genre,
                "year": movie.year,
                "rating": movie.rating,
                "duration": movie.duration,
            }
            for movie in movies
        ],
    )


def load_users(filename: str) -> list[User]:
    """Загрузить пользователей и превратить записи в объекты User."""
    return [User.from_data(data) for data in load_json(filename, [])]


def save_users(filename: str, users: list[User]) -> None:
    """Сохранить объекты User в JSON."""
    save_json(
        filename,
        [
            {
                "id": user.id,
                "name": user.name,
                "favorite_genre": user.favorite_genre,
                "min_rating": user.min_rating,
            }
            for user in users
        ],
    )


def load_ratings(
    filename: str,
    movies: list[Movie],
    users: list[User],
) -> list[Rating]:
    """Загрузить оценки, восстановив ссылки на объекты Movie и User.

    Записи без существующего фильма или пользователя пропускаются.
    """
    ratings = []
    for data in load_json(filename, []):
        movie = find_movie_by_id(movies, data["movie_id"])
        user = find_user_by_id(users, data["user_id"])
        if movie is None or user is None:
            print(f"Оценка {data['id']} пропущена: нет связанных объектов")
            continue
        rating = Rating(data["id"], movie, user, data["score"])
        rating.is_cancelled = data["is_cancelled"]
        ratings.append(rating)
    return ratings


def save_ratings(filename: str, ratings: list[Rating]) -> None:
    """Сохранить объекты Rating в JSON, заменив ссылки на идентификаторы."""
    save_json(
        filename,
        [
            {
                "id": rating.id,
                "movie_id": rating.movie.id,
                "user_id": rating.user.id,
                "score": rating.score,
                "is_cancelled": rating.is_cancelled,
            }
            for rating in ratings
        ],
    )
