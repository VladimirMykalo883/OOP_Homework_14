from src.products import Product


class Category:
    """Класс для представления категории товаров.

    Атрибуты класса:
        category_count (int): Общее количество категорий
        product_count (int): Общее количество продуктов во всех категориях

    Атрибуты экземпляра:
        name (str): Название категории
        description (str): Описание категории
        __products (List[Product]): Приватный список продуктов в категории
    """

    name: str
    description: str
    __products: list
    category_count: int
    product_count: int

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list[Product]):
        """
        Инициализация объекта Category.
        Args:
            name: Название категории
            description: Описание категории
            products: Список продуктов в категории
        """
        self.name = name
        self.description = description
        self.__products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product) -> None:
        """Добавляет продукт в категорию."""
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self) -> str:
        """Возвращает список товаров в виде строки в заданном формате."""
        products_list = []
        for product in self.__products:
            products_list.append(f"{product.name}, {int(product.price)} руб. Остаток: {product.quantity} шт.")
        return "\n".join(products_list)
