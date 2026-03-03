import re
from typing import Any


def validate_name(value: Any):
    # 1. Проверка типа
    if not isinstance(value, str):
        raise TypeError("Название/имя должно быть строкой")

    value = value.strip()

    # 2. Проверка на пустоту
    if not value:
        raise ValueError("Название/имя не может быть пустым")

    # 3. Минимальная длина
    if len(value) < 2:
        raise ValueError("Название/имя должно содержать минимум 2 символа")

    # 4. Максимальная длина
    if len(value) > 100:
        raise ValueError("Название/имя слишком длинное (максимум 100 символов)")


def validate_price(value: Any):
    # 1. Проверка типа
    if not isinstance(value, (int, float)):
        raise TypeError("Цена должна быть числом")

    # 2. Проверка отрицательного значения
    if value < 0:
        raise ValueError("Цена не может быть отрицательной")

    # 3. Проверка на NaN / бесконечность
    if value != value or value == float("inf") or value == float("-inf"):
        raise ValueError("Цена содержит недопустимое числовое значение")


def validate_stock(value: Any):
    # 1. Тип
    if not isinstance(value, int):
        raise TypeError("Остаток должен быть целым числом")

    # 2. Отрицательные значения
    if value < 0:
        raise ValueError("Остаток не может быть отрицательным")



def validate_discount(value: Any):
    # 1. Тип
    if not isinstance(value, (int, float)):
        raise TypeError("Скидка должна быть числом")

    # 2. Диапазон
    if not 0 <= value <= 100:
        raise ValueError("Скидка должна быть в диапазоне 0–100")

    # 3. Проверка на NaN/inf
    if value != value or value == float("inf") or value == float("-inf"):
        raise ValueError("Некорректное значение скидки")


def validate_quantity(value: Any):
    # 1. Тип
    if not isinstance(value, int):
        raise TypeError("Количество должно быть целым числом")

    # 2. Положительность
    if value <= 0:
        raise ValueError("Количество должно быть больше 0")

    # 3. Ограничение сверху
    if value > 100_000:
        raise ValueError("Слишком большое количество")


def validate_email(value: Any):
    # 1. Тип
    if not isinstance(value, str):
        raise TypeError("Email должен быть строкой")

    value = value.strip()

    # 2. Пустота
    if not value:
        raise ValueError("Email не может быть пустым")

    # 3. Длина
    if len(value) > 254:
        raise ValueError("Email слишком длинный")

    # 4. Формат
    if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", value):
        raise ValueError("Неверный формат email")


def validate_address(value: Any):
    # 1. Тип
    if not isinstance(value, str):
        raise TypeError("Адрес должен быть строкой")

    value = value.strip()

    # 2. Пустота
    if not value:
        raise ValueError("Адрес не может быть пустым")

    # 3. Минимальная длина
    if len(value) < 5:
        raise ValueError("Адрес слишком короткий")

    # 4. Максимальная длина
    if len(value) > 200:
        raise ValueError("Адрес слишком длинный")


def validate_payment_method(value: Any):
    allowed = {"card", "cash", "paypal"}

    # 1. Тип
    if not isinstance(value, str):
        raise TypeError("Метод оплаты должен быть строкой")

    # 2. Проверка допустимых значений
    if value.lower() not in allowed:
        raise ValueError(f"Недопустимый метод оплаты. Допустимо: {', '.join(allowed)}")

    # 3. Проверка длины строки
    if len(value.strip()) < 3:
        raise ValueError("Некорректное название метода оплаты")


def validate_positive_amount(value: Any):
    # 1. Тип
    if not isinstance(value, (int, float)):
        raise TypeError("Сумма должна быть числом")

    # 2. Неотрицательность
    if value < 0:
        raise ValueError("Сумма не может быть отрицательной")

    # 3. Проверка на NaN/inf
    if value != value or value == float("inf") or value == float("-inf"):
        raise ValueError("Некорректное числовое значение")