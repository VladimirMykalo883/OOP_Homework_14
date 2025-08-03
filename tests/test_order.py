import pytest

from src.order import Order
from src.products import Product


@pytest.fixture
def sample_product() -> Product:
    return Product("Test", "Desc", 100.0, 5)


def test_order_creation(sample_product: Product) -> None:  # Добавлены аннотации
    order = Order(sample_product, 3)
    assert order.total_cost == 300.0


def test_order_str(sample_product: Product) -> None:  # Добавлена аннотация типа
    """Тест строкового представления заказа"""
    order = Order(sample_product, 2)
    expected_str = f"Заказ: {sample_product.name}, Количество: 2, Итого: {sample_product.price * 2} руб."
    assert str(order) == expected_str  # Теперь сравнение будет точным


def test_order_with_non_product() -> None:
    """Тест создания заказа с не-продуктом"""
    with pytest.raises(TypeError):
        Order("Not a product", 1)


def test_order_negative_quantity(sample_product) -> None:
    """Тест создания заказа с отрицательным количеством"""
    with pytest.raises(ValueError):
        Order(sample_product, -1)


def test_order_with_invalid_product() -> None:
    with pytest.raises(TypeError):
        Order("invalid product", 1)  # Проверка TypeError для строки
