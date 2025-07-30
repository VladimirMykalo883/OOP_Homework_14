''' ДЗ_16_1'''
from unittest.mock import patch

from src.products import Product


def test_product_init(phone: Product):
    """Проверка корректности инициализации объекта Product"""
    assert phone.name == "Телефон"
    assert phone.description == "Смартфон"
    assert phone.price == 50000.0
    assert phone.quantity == 10


def test_product_attributes_types(phone: Product):
    """Проверка типов атрибутов Product"""
    assert isinstance(phone.name, str)
    assert isinstance(phone.description, str)
    assert isinstance(phone.price, float)
    assert isinstance(phone.quantity, int)
from unittest.mock import patch

from src.products import Product


def test_product_init(phone: Product):
    """Проверка корректности инициализации объекта Product"""
    assert phone.name == "Телефон"
    assert phone.description == "Смартфон"
    assert phone.price == 50000.0
    assert phone.quantity == 10


def test_product_attributes_types(phone: Product):
    """Проверка типов атрибутов Product"""
    assert isinstance(phone.name, str)
    assert isinstance(phone.description, str)
    assert isinstance(phone.price, float)
    assert isinstance(phone.quantity, int)


def test_new_product_class_method():
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


def test_price_decrease_confirmation(phone: Product):
    """Проверка подтверждения понижения цены"""
    with patch("builtins.input", return_value="y"):
        phone.price = 45000.0


def test_price_increase_no_confirmation(phone: Product):
    """Проверка что повышение цены не требует подтверждения"""
    original_price = phone.price
    phone.price = original_price + 1000.0
    assert phone.price == original_price + 1000.0



def test_negative_price_rejection(phone: Product):
    """Проверка отклонения отрицательной цены"""
    original_price = phone.price
    phone.price = -1000.0
    assert phone.price == original_price  # Цена не должна измениться


def test_zero_price_rejection(phone: Product):
    """Проверка отклонения нулевой цены"""
    original_price = phone.price
    phone.price = 0
    assert phone.price == original_price  # Цена не должна измениться


def test_price_setter_output(capsys, phone: Product):
    """Проверка вывода сообщений при изменении цены"""
    # Тест обычного изменения цены (без понижения)
    phone.price = 55000.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 55000.0" in captured.out

    # Тест понижения цены с подтверждением
    with patch("builtins.input", return_value="y"):
        phone.price = 45000.0
        captured = capsys.readouterr()
        assert "Цена успешно изменена на 45000.0" in captured.out

    # Тест отрицательной цены
    phone.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out


def test_new_product_class_method():
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


def test_price_decrease_confirmation(phone: Product):
    """Проверка подтверждения понижения цены"""
    with patch("builtins.input", return_value="y"):
        phone.price = 45000.0


def test_price_increase_no_confirmation(phone: Product):
    """Проверка что повышение цены не требует подтверждения"""
    original_price = phone.price
    phone.price = original_price + 1000.0
    assert phone.price == original_price + 1000.0


def test_negative_price_rejection(phone: Product):
    """Проверка отклонения отрицательной цены"""
    original_price = phone.price
    phone.price = -1000.0
    assert phone.price == original_price  # Цена не должна измениться


def test_zero_price_rejection(phone: Product):
    """Проверка отклонения нулевой цены"""
    original_price = phone.price
    phone.price = 0
    assert phone.price == original_price  # Цена не должна измениться


def test_price_setter_output(capsys, phone: Product):
    """Проверка вывода сообщений при изменении цены"""
    # Тест обычного изменения цены (без понижения)
    phone.price = 55000.0
    captured = capsys.readouterr()
    assert "Цена успешно изменена на 55000.0" in captured.out

    # Тест понижения цены с подтверждением
    with patch("builtins.input", return_value="y"):
        phone.price = 45000.0
        captured = capsys.readouterr()
        assert "Цена успешно изменена на 45000.0" in captured.out

    # Тест отрицательной цены
    phone.price = -1000
    captured = capsys.readouterr()
    assert "Цена не должна быть нулевая или отрицательная" in captured.out
