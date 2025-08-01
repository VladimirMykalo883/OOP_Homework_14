"""ДЗ_16_1"""

import pytest

from src.category import Category
from src.products import Product, Smartphone


@pytest.fixture
def category() -> Category:
    """Фикстура для создания тестовой категории"""
    return Category("Тест", "Тестовая категория", [])


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для создания тестового продукта"""
    return Product("Test Product", "Description", 100.0, 10)


@pytest.fixture
def phone() -> Smartphone:
    """Фикстура для создания тестового смартфона"""
    return Smartphone("Телефон", "Смартфон", 50000.0, 10, 95.5, "Model X", 128, "Black")


@pytest.fixture
def laptop() -> Product:
    """Фикстура для создания тестового ноутбука"""
    return Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)
