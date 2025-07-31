import pytest
from src.products import Product
from src.order import Order


@pytest.fixture
def sample_product():
    return Product("Test Product", "Description", 100.0, 10)


def test_order_creation(sample_product):
    """Тест создания заказа"""
    order = Order(sample_product, 3)

    assert order.product == sample_product
    assert order.quantity == 3
    assert order.total_cost == 300.0


def test_order_str(sample_product):
    """Тест строкового представления заказа"""
    order = Order(sample_product, 2)
    expected_str = "Заказ: Test Product, Количество: 2, Итого: 200.0 руб."
    assert str(order) == expected_str


def test_order_with_non_product():
    """Тест создания заказа с не-продуктом"""
    with pytest.raises(TypeError):
        Order("Not a product", 1)


def test_order_negative_quantity(sample_product):
    """Тест создания заказа с отрицательным количеством"""
    with pytest.raises(ValueError):
        Order(sample_product, -1)