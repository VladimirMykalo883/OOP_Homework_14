class Product:
    """Класс продукт представление продуктов.
    Атрибуты:
        name (str): Название продукта
        description (str): Описание продукта
        price (float): Цена продукта
        quantity (int): Количество продукта в наличии
    """

    name: str
    description: str
    price: float
    quantity: int

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта Product.

        Args:
            name: Название продукта
            description: Описание продукта
            price: Цена продукта
            quantity: Количество в наличии
        """
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
