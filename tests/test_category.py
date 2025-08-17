"""ДЗ_17_1"""

from unittest.mock import patch

import pytest

from src.category import Category
from src.products import LawnGrass, Product

# from tests.conftest import phone, laptop


def test_category_init(phone: Product, laptop: Product) -> None:
    """Проверка корректности инициализации объекта Category"""
    category = Category("Электроника", "Техника", [phone, laptop])
    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products.split("\n")) == 2  # Исправлено: обращение к products через экземпляр


def test_category_attributes_types(phone: Product) -> None:
    """Проверка типов атрибутов Category"""
    category = Category("Электроника", "Техника", [phone])

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, str)


def test_category_count() -> None:
    """Проверка подсчета количества категорий"""
    initial_count = Category.category_count
    _ = Category("Бытовая техника", "Техника для кухни", [])
    assert Category.category_count == initial_count + 1


def test_product_count(phone: Product, laptop: Product) -> None:
    """Проверка подсчета количества продуктов"""
    initial_count = Category.product_count
    _ = Category("Электроника", "Техника", [phone, laptop])
    assert Category.product_count == initial_count + 2


def test_empty_category_product_count() -> None:
    """Проверка, что пустая категория не увеличивает счетчик продуктов"""
    initial_count = Category.product_count
    _ = Category("Пустая", "Категория без продуктов", [])
    assert Category.product_count == initial_count


def test_add_product_with_price_confirmation(phone: Product) -> None:
    """Проверка добавления продукта с понижением цены и подтверждением"""
    category = Category("Тест", "Тестовая категория", [])
    cheap_phone = Product("Дешевый телефон", "Аналог", phone.price - 10000, 5)

    with patch("builtins.input", return_value="y"):
        category.add_product(cheap_phone)
        assert cheap_phone.name in category.products


def test_products_property_format(phone: Product) -> None:
    """Проверка формата вывода свойства products"""
    category = Category("Тест", "Тестовая категория", [phone])
    products_str = category.products

    assert phone.name in products_str
    assert str(int(phone.price)) in products_str
    assert f"Остаток: {phone.quantity} шт." in products_str


def test_add_product_updates_counters() -> None:
    """Проверка что add_product обновляет счетчики"""
    initial_count = Category.product_count
    category = Category("Тест", "Тестовая категория", [])
    product = Product("Тест", "Тест", 1000, 1)

    category.add_product(product)
    assert Category.product_count == initial_count + 1


def test_add_product_type_check(phone: Product) -> None:
    """Тест проверки типа при добавлении продукта"""
    category = Category("Test", "Test", [])

    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product("not a product")  # type: ignore


def test_category_with_different_products(phone: Product) -> None:
    """Тест работы категории с разными типами продуктов"""
    grass = LawnGrass("Grass", "Green", 20, 100, "USA", "14d", "Green")
    category = Category("Mixed", "Category", [phone, grass])

    assert len(category.products.split("\n")) == 2
    assert phone.name in category.products
    assert "Grass" in category.products


def test_category_middle_price_with_products(phone: Product, laptop: Product) -> None:
    category = Category("Тест", "Тест", [phone, laptop])
    print(f"Phone price: {phone.price}")  # Должно быть 50000.0
    print(f"Laptop price: {laptop.price}")  # Должно быть 100000.0
    print(f"Calculated avg: {category.middle_price}")  # Должно быть 75000.0
    assert category.middle_price() == 75000.0


def test_category_middle_price_empty() -> None:
    category = Category("Тест", "Тест", [])
    print(f"Empty category avg: {category.middle_price}")  # Должно быть 0.0
    assert category.middle_price() == 0.0
