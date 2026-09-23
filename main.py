"""Точка запуска CineMatch: меню консольного приложения."""

from movies import (
    add_movie,
    count_by_genre,
    filter_movies_by_genre,
    find_movies,
    format_movie_card,
    get_movie,
    sort_movies,
)
from ratings import (
    cancel_rating,
    get_evening_advice,
    rate_movie,
    recommend_movies,
)
from storage import load_json, save_json
from utils import input_float, input_int

MOVIES_FILE = "data/movies.json"
RATINGS_FILE = "data/ratings.json"
USER_FILE = "data/user.json"
DEFAULT_USER = {"name": "Гость", "favorite_genre": "", "min_rating": 8.0}

MENU = """
1. Показать фильмы
2. Найти фильм по названию
3. Фильмы по жанру
4. Добавить фильм
5. Оценить фильм
6. Отменить оценку
7. Показать оценки
8. Рекомендации
9. Статистика по жанрам
0. Выход
"""


def show_movies(movies: list[dict]) -> None:
    """Вывести карточки фильмов."""
    if not movies:
        print("Фильмов нет")
    for movie in movies:
        print(format_movie_card(movie))


def show_ratings(movies: list[dict], ratings: list[dict]) -> None:
    """Вывести оценки пользователя с названиями фильмов."""
    if not ratings:
        print("Оценок нет")
    for rating in ratings:
        movie = get_movie(movies, rating["movie_id"])
        title = movie["title"] if movie else "неизвестный фильм"
        print(f"{title}: {rating['score']}")


def main() -> None:
    """Загрузить данные и запустить цикл меню."""
    movies = load_json(MOVIES_FILE, [])
    ratings = load_json(RATINGS_FILE, [])
    user = load_json(USER_FILE, DEFAULT_USER)
    print(f"=== CineMatch. Пользователь: {user['name']} ===")

    while True:
        print(MENU)
        choice = input_int("Выберите действие: ")

        if choice == 1:
            show_movies(sort_movies(movies))
        elif choice == 2:
            show_movies(find_movies(movies, input("Название: ")))
        elif choice == 3:
            genre = input("Жанр: ")
            show_movies(list(filter_movies_by_genre(movies, genre)))
        elif choice == 4:
            movie = add_movie(
                movies,
                input("Название: "),
                input("Жанр: "),
                input_int("Год выпуска: "),
                input_float("Рейтинг: "),
                input_int("Длительность, мин: "),
            )
            save_json(MOVIES_FILE, movies)
            print(f"Добавлен фильм: {movie['title']}")
        elif choice == 5:
            movie_id = input_int("ID фильма: ")
            if get_movie(movies, movie_id) is None:
                print("Фильм не найден")
                continue
            try:
                rate_movie(ratings, movie_id, input_int("Оценка от 1 до 10: "))
            except ValueError as error:
                print(error)
            else:
                save_json(RATINGS_FILE, ratings)
                print("Оценка сохранена")
        elif choice == 6:
            if cancel_rating(ratings, input_int("ID фильма: ")):
                save_json(RATINGS_FILE, ratings)
                print("Оценка отменена")
            else:
                print("Оценка не найдена")
        elif choice == 7:
            show_ratings(movies, ratings)
        elif choice == 8:
            show_movies(recommend_movies(movies, ratings, user))
            print(get_evening_advice())
        elif choice == 9:
            for genre, count in count_by_genre(movies).items():
                print(f"{genre}: {count}")
        elif choice == 0:
            print("До встречи!")
            break
        else:
            print("Нет такого пункта меню")


if __name__ == "__main__":
    main()
