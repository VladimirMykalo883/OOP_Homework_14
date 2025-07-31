from src.base import BaseClass
from src.products import Product


class Order(BaseClass):
    """Класс для представления заказа"""
    def __init__(self, product: Product, quantity: int):
        if not isinstance(product, Product):
            raise TypeError("Можно заказывать только продукты")
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity
        super().__init__()

    def __str__(self):
        return (f"Заказ: {self.product.name}, "
                f"Количество: {self.quantity}, "
                f"Итого: {self.total_cost} руб.")
