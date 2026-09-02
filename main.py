from datetime import date
from random import choice

user_name = "Алексей"
movie_title = "Интерстеллар"
genre = "Фантастика"
release_year = 2014
rating = 8.6
watch_date = date(2026, 9, 2)
is_recommended = True

random_movies = ["Побег из Шоушенка", "Криминальное чтиво", "Матрица", "Бойцовский клуб", "Начало"]

def get_recommendation_status(is_recommended):
    if is_recommended:
        return "Рекомендуем к просмотру!"
    return "Фильм не вошел в вашу подборку"

def get_random_movie(movies_list):
    return choice(movies_list)

print(f"👤 Пользователь: {user_name}")
print(f"🎬 Фильм: {movie_title}")
print(f"📂 Жанр: {genre}")
print(f"📅 Год выпуска: {release_year}")
print(f"⭐ Рейтинг: {rating}")
print(f"📆 Дата просмотра: {watch_date}")
print(get_recommendation_status(is_recommended))

print(f"\n🎲 Случайный фильм на сегодня: {get_random_movie(random_movies)}")
print("🍿 Приятного просмотра!")