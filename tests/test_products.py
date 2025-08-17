"""ДЗ_17_1"""

from typing import Any
from unittest.mock import patch

import pytest
from _pytest.capture import CaptureFixture

from src.base import LogMixin
from src.category import Category
from src.products import LawnGrass, Product, Smartphone


def test_product_init(phone: Product) -> None:
    """Проверка корректности инициализации объекта Product"""
    assert phone.name == "Телефон"
    assert phone.description == "Смартфон"
    assert phone.price == 50000.0
    assert phone.quantity == 10


def test_product_attributes_types(phone: Product) -> None:
    """Проверка типов атрибутов Product"""
    assert isinstance(phone.name, str)
    assert isinstance(phone.description, str)
    assert isinstance(phone.price, float)
    assert isinstance(phone.quantity, int)


def test_new_product_class_method() -> None:
    """Проверка создания продукта через класс-метод new_product."""
    product_data = {
        "name": "Тестовый продукт",
        "description": "Описание тестового продукта",
        "price": 1000.0,
        "quantity": 10,
    }
    product = Product.new_product(product_data)
    assert product.name == "Тестовый продукт"
    assert product.description == "Описание тестового продукта"
    assert product.price == 1000.0
    assert product.quantity == 10


def test_price_decrease_confirmation(phone: Product) -> None:
    """Проверка подтверждения понижения цены"""
    with patch("builtins.input", return_value="y"):
        phone.price = 45000.0
        assert phone.price == 45000.0


def test_price_increase_no_confirmation(phone: Product) -> None:
    """Проверка, что повышение цены не требует подтверждения"""
    original_price = phone.price
    phone.price = original_price + 1000.0
    assert phone.price == original_price + 1000.0


def test_negative_price_rejection(phone: Product) -> None:
    """Проверка отклонения отрицательной цены"""
    original_price = phone.price
    phone.price = -1000.0
    assert phone.price == original_price


def test_zero_price_rejection(phone: Product) -> None:
    """Проверка отклонения нулевой цены"""
    original_price = phone.price
    phone.price = 0
    assert phone.price == original_price


def test_price_setter_output_increase(capsys: CaptureFixture, phone: Product) -> None:
    """Проверка вывода при повышении цены"""
    phone.price = 55000.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 55000.0" in captured.out


def test_price_setter_output_decrease(capsys: CaptureFixture, phone: Product) -> None:
    """Проверка вывода при понижении цены с подтверждением"""
    with patch("builtins.input", return_value="y"):
        phone.price = 45000.0
        captured = capsys.readouterr()
        assert "Цена успешно изменена на 45000.0" in captured.out


def test_price_setter_output_negative(capsys: CaptureFixture, phone: Product) -> None:
    """Проверка вывода при отрицательной цене"""
    phone.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_smartphone_creation_with_correct_types() -> None:
    """Тест создания смартфона с правильными типами"""
    phone = Smartphone(
        name="iPhone",
        description="Smartphone",
        price=1000.0,
        quantity=5,
        efficiency=76.5,
        model="13 Pro",
        memory=128,
        color="Black",
    )
    assert isinstance(phone, Smartphone)


def test_lawn_grass_creation() -> None:
    """Тест создания объекта LawnGrass"""
    grass = LawnGrass(
        name="Premium Grass",
        description="Luxury lawn grass",
        price=25.50,
        quantity=100,
        country="USA",
        germination_period="14 days",
        color="Dark Green",
    )

    assert grass.name == "Premium Grass"
    assert grass.country == "USA"
    assert grass.germination_period == "14 days"
    assert isinstance(grass, Product)


def test_add_same_type_products() -> None:
    """Тест сложения объектов одинакового типа"""
    phone1 = Smartphone("Phone1", "Desc", 1000, 2, 46.8, "M1", 64, "Black")
    phone2 = Smartphone("Phone2", "Desc", 1500, 3, 69.7, "M2", 128, "White")
    assert phone1 + phone2 == 1000 * 2 + 1500 * 3


def test_add_different_type_products() -> None:
    """Тест сложения объектов разного типа"""
    phone = Smartphone("Phone", "Desc", 1000, 1, 78.6, "M1", 64, "Black")
    product = Product("Product", "Desc", 500, 2)
    with pytest.raises(TypeError):
        _ = phone + product


def test_add_product_to_category_type_check(category: Category) -> None:
    """Проверка типа при добавлении в категорию"""
    with pytest.raises(TypeError, match="Можно добавлять только объекты Product или его наследников"):
        category.add_product(123)  # type: ignore


def test_smartphone_addition() -> None:
    """Тест сложения объектов Smartphone"""
    phone1 = Smartphone("Phone1", "Desc", 1000, 2, 49.7, "M1", 64, "Black")
    phone2 = Smartphone("Phone2", "Desc", 1500, 3, 57.4, "M2", 128, "White")

    total = phone1 + phone2
    assert total == 1000 * 2 + 1500 * 3


def test_lawn_grass_addition() -> None:
    """Тест сложения объектов LawnGrass"""
    grass1 = LawnGrass("Grass1", "Desc", 20, 50, "USA", "14d", "Green")
    grass2 = LawnGrass("Grass2", "Desc", 25, 30, "CAN", "10d", "Dark Green")

    total = grass1 + grass2
    assert total == 20 * 50 + 25 * 30


def test_mixed_class_addition() -> None:
    """Тест попытки сложения разных классов"""
    phone = Smartphone("Phone", "Desc", 1000, 1, 87.6, "M1", 64, "Black")
    grass = LawnGrass("Grass", "Desc", 20, 5, "USA", "14d", "Green")

    with pytest.raises(TypeError):
        _ = phone + grass


def test_log_mixin(capsys: CaptureFixture) -> None:
    """Тест логирования создания объекта"""

    class TestClass(LogMixin):
        def __init__(self, param1: Any, param2: Any):
            self.param1 = param1
            self.param2 = param2
            super().__init__()

    TestClass("value1", "value2")
    captured = capsys.readouterr()

    assert "Создан объект TestClass" in captured.out
    assert "param1=value1" in captured.out
    assert "param2=value2" in captured.out


def test_product_zero_quantity_raises_error() -> None:
    """Тест, что создание продукта с нулевым количеством вызывает ошибку"""
    with pytest.raises(ValueError, match="Товар с нулевым количеством не может быть добавлен"):
        Product("Test", "Desc", 100.0, 0)
