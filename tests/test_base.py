import pytest

from src.base import BaseClass
from src.category import Category
from src.order import Order


def test_base_class_abstract() -> None:
    """Тест, что BaseClass нельзя инстанцировать"""
    with pytest.raises(TypeError):
        BaseClass()  # Ожидаем ошибку для абстрактного класса


def test_category_inherits_base() -> None:
    """Тест, что Category наследует BaseClass"""
    assert issubclass(Category, BaseClass)
    category = Category("Test", "Test", [])
    assert isinstance(category, BaseClass)


def test_order_inherits_base() -> None:
    """Тест, что Order наследует BaseClass"""
    assert issubclass(Order, BaseClass)
