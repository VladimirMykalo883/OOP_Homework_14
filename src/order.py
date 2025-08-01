from src.base import BaseClass
from src.products import Product


class Order(BaseClass):
    """Класс для представления заказа"""

    def __init__(self, product: Product, quantity: int) -> None:
        if not isinstance(product, Product):
            raise TypeError("Можно заказывать только продукты")
        if quantity < 0 or product.price < 0:
            raise ValueError(" Количество не может быть отрицательным")
        self.product = product
        self.quantity = quantity
        self.total_cost = product.price * quantity
        super().__init__()

    def __str__(self) -> str:
        return f"Заказ: {self.product.name}, " f"Количество: {self.quantity}, " f"Итого: {self.total_cost} руб."
