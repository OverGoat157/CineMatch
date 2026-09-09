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

# Преобразование типов и арифметические операции
rating = float(rating_text)
duration_minutes = int(duration_text)
hours = duration_minutes // 60
minutes = duration_minutes % 60
movie_age = date.today().year - release_year

print(f"Пользователь: {user_name}")
print(f"Фильм: {movie_title} ({release_year}), жанр: {movie_genre}")
print(f"Рейтинг: {rating}, длительность: {hours} ч {minutes} мин")
print(f"Фильму {movie_age} лет")

# Ветвление: подходит ли фильм пользователю
genre_matches = movie_genre == favorite_genre
rating_is_high = rating >= min_rating

if genre_matches and rating_is_high:
    verdict = "Рекомендуем: любимый жанр и высокий рейтинг"
elif genre_matches or rating_is_high:
    verdict = "Можно посмотреть: совпало одно из условий"
else:
    verdict = "Не рекомендуем"

print(verdict)

# Случайный совет на вечер
dice = randint(1, 6)
if dice > 3:
    print("Совет: сегодня отличный вечер для кино")
else:
    print("Совет: лучше отложить просмотр на выходные")
