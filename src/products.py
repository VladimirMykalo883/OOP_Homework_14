"""ДЗ 17_1"""

from src.base import BaseProduct, LogMixin


class Product(BaseProduct, LogMixin):
    """Класс продукт представление продуктов.
    Атрибуты:
        name (str): Название продукта
        description (str): Описание продукта
        __price (float): Цена продукта
        quantity (int): Количество продукта в наличии
    """

    name: str
    description: str
    __price: float
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

        super().__init__()
        if quantity == 0:
            raise ValueError("Товар с нулевым количеством не может быть добавлен")

        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    @property
    def price(self) -> float:
        """Геттер для цены. Возвращает текущую цену."""
        return self.__price

    @price.setter
    def price(self, new_price: float) -> None:
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        elif new_price < self.__price:
            # Запрос подтверждения для понижения цены
            if input(f"Понизить цену с {self.__price} до {new_price}? (y/n): ").lower() == "y":
                self.__price = new_price
                print(f"Цена успешно изменена на {new_price}")
            else:
                print("Изменение цены отменено")
        else:
            self.__price = new_price
            print(f"Цена успешно изменена на {new_price}")

    @classmethod
    def new_product(cls: type["Product"], product_data: dict, products: list["Product"] | None = None) -> "Product":
        """
        Создает новый объект класса Product из словаря с данными.
        Если товар с таким именем уже существует:
            - объединяет количество
            - выбирает максимальную цену
            - обновляет описание (если новое описание не пустое)
        Args:
            product_data: Словарь с данными продукта:
                - name (str): Название продукта
                - description (str): Описание продукта
                - price (float): Цена продукта
                - quantity (int): Количество продукта
            products: Список существующих продуктов для проверки дубликатов
        Returns:
            Product: Новый или обновленный объект класса Product
        """
        if products is None:
            products = []

        # Поиск товара с таким же именем
        for existing_product in products:
            if existing_product.name.lower() == product_data["name"].lower():
                # Объединение количества
                existing_product.quantity += product_data["quantity"]
                # Выбор максимальной цены
                existing_product.price = max(existing_product.price, product_data["price"])
                # Обновление описания, если новое не пустое
                if product_data["description"]:
                    existing_product.description = product_data["description"]
                return existing_product

        # Если дубликат не найден, создаем новый продукт
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __str__(self) -> str:
        return f"{self.name}, {int(self.price)} руб. Остаток: {self.quantity} шт."

    def __add__(self, other: "Product") -> float:
        if type(self) is not type(other):  # Исправлено на is not вместо !=
            raise TypeError("Можно складывать только объекты одинаковых классов")
        return (self.price * self.quantity) + (other.price * other.quantity)


class Smartphone(Product):
    """Класс для представления смартфонов"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color
        super().__init__(name, description, price, quantity)


class LawnGrass(Product):
    """Класс для представления газонной травы"""

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: str,
        color: str,
    ):
        self.country = country
        self.germination_period = germination_period
        self.color = color
        super().__init__(name, description, price, quantity)
