from src.category import Category
from src.products import Product


def test_category_init(phone: Product, laptop: Product) -> None:
    """Проверка корректности инициализации объекта Category"""
    category = Category("Электроника", "Техника", [phone, laptop])

    assert category.name == "Электроника"
    assert category.description == "Техника"
    assert len(category.products) == 2
    assert isinstance(category.products[0], Product)


def test_category_attributes_types(phone: Product) -> None:
    """Проверка типов атрибутов Category"""
    category = Category("Электроника", "Техника", [phone])

    assert isinstance(category.name, str)
    assert isinstance(category.description, str)
    assert isinstance(category.products, list)
    assert all(isinstance(p, Product) for p in category.products)


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
