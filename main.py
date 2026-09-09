from datetime import date
from random import randint

# Данные пользователя
user_name = "Алексей"
favorite_genre = "Фантастика"
min_rating = 8.0

# Данные фильма (рейтинг и длительность пришли строками, как из внешнего API)
movie_title = "Интерстеллар"
movie_genre = "Фантастика"
release_year = 2014
rating_text = "8.6"
duration_text = "169"


def show_movie_card(title, year, genre, rating, duration_minutes):
    hours = duration_minutes // 60
    minutes = duration_minutes % 60
    movie_age = date.today().year - year
    print(f"Фильм: {title} ({year}), жанр: {genre}")
    print(f"Рейтинг: {rating}, длительность: {hours} ч {minutes} мин")
    print(f"Фильму {movie_age} лет")


def get_recommendation(genre, rating, favorite_genre, min_rating):
    genre_matches = genre == favorite_genre
    rating_is_high = rating >= min_rating
    if genre_matches and rating_is_high:
        return "Рекомендуем: любимый жанр и высокий рейтинг"
    elif genre_matches or rating_is_high:
        return "Можно посмотреть: совпало одно из условий"
    return "Не рекомендуем"


def get_evening_advice():
    dice = randint(1, 6)
    if dice > 3:
        return "Совет: сегодня отличный вечер для кино"
    return "Совет: лучше отложить просмотр на выходные"


# Преобразование типов
rating = float(rating_text)
duration_minutes = int(duration_text)

print(f"Пользователь: {user_name}")
show_movie_card(movie_title, release_year, movie_genre, rating, duration_minutes)
print(get_recommendation(movie_genre, rating, favorite_genre, min_rating))
print(get_evening_advice())
