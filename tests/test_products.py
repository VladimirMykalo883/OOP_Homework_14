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
