from unittest.mock import patch

from src.category import Category
from src.products import Product


def test_category_init(phone: Product, laptop: Product) -> None:
    """Проверка корректности инициализации объекта Category"""
    category = Category("Электроника", "Техника", [phone, laptop])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products.split("\n")) == 2  # Проверяем через свойство products
    assert "Телефон" in category.products
    assert "Ноутбук" in category.products


def test_category_attributes_types(phone: Product) -> None:
    """Проверка типов атрибутов Category"""
    category = Category("Электроника", "Техника", [phone])

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, str)
    assert isinstance(category.products, str)  # Теперь это строка с отформатированным выводом


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

    with patch("builtins.input", return_value="y"):
        # Создаем продукт с более низкой ценой
        cheap_phone = Product("Дешевый телефон", "Аналог", phone.price - 10000, 5)
        category.add_product(cheap_phone)
        assert cheap_phone.name in category.products


def test_products_property_format(phone: Product) -> None:
    """Проверка формата вывода свойства products"""
    category = Category("Тест", "Тестовая категория", [phone])
    products_str = category.products

    assert phone.name in products_str
    assert str(int(phone.price)) in products_str  # Проверяем цену без десятичных
    assert f"Остаток: {phone.quantity} шт." in products_str


def test_add_product_updates_counters() -> None:
    """Проверка что add_product обновляет счетчики"""
    initial_count = Category.product_count
    category = Category("Тест", "Тестовая категория", [])
    product = Product("Тест", "Тест", 1000, 1)

    category.add_product(product)
    assert Category.product_count == initial_count + 1


def test_category_str(phone: Product, laptop: Product):
    """Проверка строкового представления Category"""
    category = Category("Тест", "Тестовая категория", [phone, laptop])
    expected = "Тест, количество продуктов: 15 шт."  # 10 + 5
    assert str(category) == expected
