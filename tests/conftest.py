"""ДЗ_16_1"""

import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def phone() -> Product:
    """Фикстура для создания тестового телефона"""
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def laptop() -> Product:
    """Фикстура для создания тестового ноутбука"""
    return Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)


@pytest.fixture(autouse=True)
def reset_category_count() -> None:
    """Фикстура для сброса счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
