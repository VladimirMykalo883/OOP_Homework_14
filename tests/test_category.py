import pytest

from src.category import Category
from src.products import Product


def test_category_init() -> None:
    """Проверка корректности инициализации объекта Category"""
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    category = Category("Электроника", "Техника", [product1, product2])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2
    assert isinstance(category.products[0], Product)


def test_category_attributes_types() -> None:
    """Проверка типов атрибутов Category"""
    product = Product("Телефон", "Смартфон", 50000.0, 10)
    category = Category("Электроника", "Техника", [product])

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, list)
    assert all(isinstance(p, Product) for p in category.products)


def test_category_count() -> None:
    """Проверка подсчета количества категорий"""
    initial_count = Category.category_count
    _ = Category("Бытовая техника", "Техника для кухни", [])
    assert Category.category_count == initial_count + 1


def test_product_count() -> None:
    """Проверка подсчета количества продуктов"""
    initial_count = Category.product_count
    product1 = Product("Телефон", "Смартфон", 50000.0, 10)
    product2 = Product("Ноутбук", "Игровой", 100000.0, 5)
    _ = Category("Электроника", "Техника", [product1, product2])

    assert Category.product_count == initial_count + 2


def test_empty_category_product_count() -> None:
    """Проверка, что пустая категория не увеличивает счетчик продуктов"""
    initial_count = Category.product_count
    _ = Category("Пустая", "Категория без продуктов", [])
    assert Category.product_count == initial_count
