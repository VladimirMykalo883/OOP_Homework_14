from typing import Generator, List

import pytest

from src.category import Category
from src.products import Product


@pytest.fixture
def sample_product() -> Product:
    """Фикстура для создания тестового продукта"""
    return Product("Телефон", "Смартфон", 50000.0, 10)


@pytest.fixture
def another_product() -> Product:
    """Фикстура для создания другого тестового продукта"""
    return Product("Ноутбук", "Игровой ноутбук", 100000.0, 5)


@pytest.fixture
def sample_products(sample_product, another_product) -> List[Product]:
    """Фикстура для создания списка тестовых продуктов"""
    return [sample_products(), another_product]


@pytest.fixture
def sample_category(sample_products) -> Category:
    """Фикстура для создания тестовой категории"""
    return Category("Электроника", "Техника для дома", sample_products)


@pytest.fixture(autouse=True)
def reset_category_count() -> Generator[None, None, None]:
    """Фикстура для сброса счетчиков перед каждым тестом"""
    Category.category_count = 0
    Category.product_count = 0
    yield
    Category.category_count = 0
    Category.product_count = 0
