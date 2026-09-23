"""Оценки пользователя и рекомендации."""

from random import randint

from movies import sort_movies

RECOMMENDED = "Рекомендуем: любимый жанр и высокий рейтинг"


def get_recommendation(
    genre: str,
    rating: float,
    favorite_genre: str,
    min_rating: float,
) -> str:
    """Вернуть вердикт, подходит ли фильм пользователю (функция из ПР1)."""
    genre_matches = genre == favorite_genre
    rating_is_high = rating >= min_rating
    if genre_matches and rating_is_high:
        return RECOMMENDED
    elif genre_matches or rating_is_high:
        return "Можно посмотреть: совпало одно из условий"
    return "Не рекомендуем"


def get_evening_advice() -> str:
    """Вернуть случайный совет на вечер (функция из ПР1)."""
    dice = randint(1, 6)
    if dice > 3:
        return "Совет: сегодня отличный вечер для кино"
    return "Совет: лучше отложить просмотр на выходные"


def is_rated(ratings: list[dict], movie_id: int) -> bool:
    """Проверить, оценён ли фильм."""
    return any(rating["movie_id"] == movie_id for rating in ratings)


def rate_movie(ratings: list[dict], movie_id: int, score: int) -> dict:
    """Поставить фильму оценку от 1 до 10.

    Повторная оценка и оценка вне диапазона вызывают ValueError.
    """
    if not 1 <= score <= 10:
        raise ValueError("Оценка должна быть от 1 до 10")
    if is_rated(ratings, movie_id):
        raise ValueError("Фильм уже оценён")
    rating = {"movie_id": movie_id, "score": score}
    ratings.append(rating)
    return rating


def cancel_rating(ratings: list[dict], movie_id: int) -> bool:
    """Удалить оценку фильма. Вернуть True, если оценка была."""
    for rating in ratings:
        if rating["movie_id"] == movie_id:
            ratings.remove(rating)
            return True
    return False


def recommend_movies(
    movies: list[dict],
    ratings: list[dict],
    user: dict,
) -> list[dict]:
    """Подобрать неоценённые фильмы под вкус пользователя."""
    suitable = []
    for movie in movies:
        if is_rated(ratings, movie["id"]):
            continue
        verdict = get_recommendation(
            movie["genre"],
            movie["rating"],
            user["favorite_genre"],
            user["min_rating"],
        )
        if verdict == RECOMMENDED:
            suitable.append(movie)
    return sort_movies(suitable)
