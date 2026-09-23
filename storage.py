"""Сохранение и загрузка данных проекта в JSON-файлах."""

import json


def load_json(filename: str, default):
    """Загрузить данные из JSON-файла.

    Если файла нет или он повреждён, вернуть default.
    """
    try:
        with open(filename, encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Файл {filename} не найден, используются данные по умолчанию")
        return default
    except json.JSONDecodeError:
        print(f"Файл {filename} повреждён, используются данные по умолчанию")
        return default


def save_json(filename: str, data) -> None:
    """Сохранить данные в JSON-файл."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, ensure_ascii=False, indent=2)
