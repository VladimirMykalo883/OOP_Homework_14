"""ДЗ_16_2"""

from src.base import BaseShopEntity
from src.category import Category
from src.order import Order


def test_category_inherits_base() -> None:
    category = Category("Test", "Test", [])
    assert isinstance(category, BaseShopEntity)
    assert issubclass(Category, BaseShopEntity)  # Замените на ваш реальный базовый класс


def test_order_inherits_base() -> None:
    """Тест, что Order наследует BaseShopEntity"""
    assert issubclass(Order, BaseShopEntity)
