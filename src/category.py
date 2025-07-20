from typing import List

from src.products import Product


class Category:
    """Класс для представления категории товаров.

    Атрибуты класса:
        category_count (int): Общее количество категорий
        product_count (int): Общее количество продуктов во всех категориях

    Атрибуты экземпляра:
        name (str): Название категории
        description (str): Описание категории
        products (List[Product]): Список продуктов в категории
    """

    name: str
    description: str
    products: list
    category_count: int
    product_count: int

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: List[Product]):
        """
        Инициализация объекта Category.
        Args:
            name: Название категории
            description: Описание категории
            products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)
