def test_product_init(sample_product):
    """Проверка корректности инициализации объекта Product"""
    assert sample_product.name == "Телефон"
    assert sample_product.description == "Смартфон"
    assert sample_product.price == 50000.0
    assert sample_product.quantity == 10


def test_product_attributes_types(sample_product):
    """Проверка типов атрибутов Product"""
    assert isinstance(sample_product.name, str)
    assert isinstance(sample_product.description, str)
    assert isinstance(sample_product.price, float)
    assert isinstance(sample_product.quantity, int)
