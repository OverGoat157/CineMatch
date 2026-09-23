"""Безопасный ввод чисел с повтором запроса при ошибке."""


def input_int(prompt: str) -> int:
    """Запросить целое число, повторяя запрос при некорректном вводе."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Введите целое число")


def input_float(prompt: str) -> float:
    """Запросить дробное число, повторяя запрос при некорректном вводе."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Введите число, например 8.5")
