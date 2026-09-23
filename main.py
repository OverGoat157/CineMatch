"""Точка запуска CineMatch: меню консольного приложения."""

from models import Movie, Rating, User
from models.movies import (
    add_movie,
    count_by_genre,
    filter_movies_by_genre,
    find_movie_by_id,
    find_movies,
    show_movies,
    sort_movies,
)
from models.ratings import (
    cancel_rating,
    get_evening_advice,
    rate_movie,
    recommend_movies,
    show_ratings,
)
from models.users import add_user, find_user_by_id, show_users
from storage import (
    load_movies,
    load_ratings,
    load_users,
    save_movies,
    save_ratings,
    save_users,
)
from utils import input_float, input_int

MOVIES_FILE = "data/movies.json"
USERS_FILE = "data/users.json"
RATINGS_FILE = "data/ratings.json"

MENU = """
1. Показать фильмы
2. Найти фильм по названию
3. Фильмы по жанру
4. Добавить фильм
5. Показать пользователей
6. Добавить пользователя
7. Сменить пользователя
8. Оценить фильм
9. Отменить оценку
10. Показать оценки
11. Рекомендации
12. Статистика по жанрам
0. Выход
"""


def choose_movie(movies: list[Movie]) -> Movie | None:
    """Запросить id фильма и вернуть найденный объект."""
    movie = find_movie_by_id(movies, input_int("ID фильма: "))
    if movie is None:
        print("Фильм не найден")
    return movie


def choose_user(users: list[User]) -> User | None:
    """Запросить id пользователя и вернуть найденный объект."""
    user = find_user_by_id(users, input_int("ID пользователя: "))
    if user is None:
        print("Пользователь не найден")
    return user


def add_new_movie(movies: list[Movie]) -> None:
    """Сценарий добавления фильма с сохранением каталога."""
    movie = add_movie(
        movies,
        input("Название: "),
        input("Жанр: "),
        input_int("Год выпуска: "),
        input_float("Рейтинг: "),
        input_int("Длительность, мин: "),
    )
    save_movies(MOVIES_FILE, movies)
    print(f"Добавлен фильм: {movie.title}")


def add_new_user(users: list[User]) -> None:
    """Сценарий добавления пользователя с сохранением списка."""
    user = add_user(
        users,
        input("Имя: "),
        input("Любимый жанр: "),
        input_float("Минимальный рейтинг: "),
    )
    save_users(USERS_FILE, users)
    print(f"Добавлен пользователь: {user.name}")


def rate_new_movie(
    movies: list[Movie],
    ratings: list[Rating],
    user: User,
) -> None:
    """Сценарий оценки фильма текущим пользователем."""
    movie = choose_movie(movies)
    if movie is None:
        return
    try:
        rate_movie(ratings, movie, user, input_int("Оценка от 1 до 10: "))
    except ValueError as error:
        print(error)
        return
    save_ratings(RATINGS_FILE, ratings)
    print("Оценка сохранена")


def cancel_user_rating(
    movies: list[Movie],
    ratings: list[Rating],
    user: User,
) -> None:
    """Сценарий отмены оценки текущего пользователя."""
    movie = choose_movie(movies)
    if movie is None:
        return
    if cancel_rating(ratings, movie, user):
        save_ratings(RATINGS_FILE, ratings)
        print("Оценка отменена")
    else:
        print("Активная оценка не найдена")


def main() -> None:
    """Загрузить объекты и запустить цикл меню."""
    movies = load_movies(MOVIES_FILE)
    users = load_users(USERS_FILE)
    ratings = load_ratings(RATINGS_FILE, movies, users)
    if not users:
        users.append(User(1, "Гость", "", 8.0))
    user = users[0]
    print("=== CineMatch ===")

    while True:
        print(f"Текущий пользователь: {user.name}")
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
            add_new_movie(movies)
        elif choice == 5:
            show_users(users)
        elif choice == 6:
            add_new_user(users)
        elif choice == 7:
            user = choose_user(users) or user
        elif choice == 8:
            rate_new_movie(movies, ratings, user)
        elif choice == 9:
            cancel_user_rating(movies, ratings, user)
        elif choice == 10:
            show_ratings(ratings)
        elif choice == 11:
            show_movies(recommend_movies(movies, ratings, user))
            print(get_evening_advice())
        elif choice == 12:
            for genre, count in count_by_genre(movies).items():
                print(f"{genre}: {count}")
        elif choice == 0:
            print("До встречи!")
            break
        else:
            print("Нет такого пункта меню")


if __name__ == "__main__":
    main()
