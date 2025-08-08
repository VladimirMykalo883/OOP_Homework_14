<p align="center">
  <img src="https://img.icons8.com/clouds/500/bank-card-back-side.png" alt="bank operations logo" width="160"/>
</p>

<h1 align="center"># Проект по управлению товарами и категориями</h1>

<p align="center">
  <strong>Этот проект реализует систему управления товарами, категориями и заказами с использованием ООП в Python</strong><br>
  <em>С  тестами и контролем качества</em>
</p>

<p align="center">
  <a href="https://www.python.org/"><img src="https://img.shields.io/badge/Python-3.12+-blue.svg" alt="Python"></a>
  <a href="https://python-poetry.org/"><img src="https://img.shields.io/badge/Poetry-1.8+-orange.svg" alt="Poetry"></a>
  <img src="https://img.shields.io/badge/Coverage-85%25-brightgreen.svg" alt="Coverage">
  <img src="https://img.shields.io/github/actions/workflow/status/Enigmatik007/bank_operations/tests.yml?branch=main&label=CI" alt="GitHub Actions">
</p>

---

## 📦 Установка

git clone https://github.com/VladimirMykalo883/OOP_Homework_14
cd homwork
poetry install

---

## 🧰 Функциональность.

### 🔍 Основные классы.

- - Класс `Product` для представления товаров с атрибутами:
  - Название
  - Описание
  - Цена                 (теперь является приватным атрибутом)
  - Количество в наличии
- - Базовый класс `Product` - представляет товар с названием, описанием, ценой и количеством
   - `Smartphone` - класс для смартфонов (наследуется от Product)
   - `LawnGrass` - класс для газонной травы (наследуется от Product)

- -  Класс 'Сategory' - инициация и создание класса Category
   - `Category` - содержит товары одной категории
   - Поддерживает добавление товаров и автоматический подсчет количества.

- -  Класс`Order` - представляет заказ на конкретный товар с указанием количества

### Дополнительные возможности.
    - **Логирование создания объектов** с помощью миксина `LogMixin`
    - **Абстрактные базовые классы**:
    - `BaseProduct` - базовый класс для всех продуктов
    - `BaseShopEntity` - базовый класс для сущностей магазина (Category и Order)
    - **Подтверждение изменения цены** при ее понижении
    - **Сложение продуктов** одного типа (по общей стоимости)

### ## Пример использования


# Создание продуктов
phone = Smartphone("iPhone", "Flagship", 100000, 10, 95.5, "15 Pro", 256, "Black")
grass = LawnGrass("Premium", "Green grass", 500, 100, "USA", "14d", "Green")

# Создание категории
electronics = Category("Electronics", "Devices", [phone])

# Создание заказа
order = Order(phone, 2)
print(order)  # Заказ: iPhone, Количество: 2, Итого: 200000 руб.


### 🧪 Тестирование

Запуск тестов и генерация отчёта покрытия:

poetry run pytest --cov=src --cov-report=html
start htmlcov/index.html  # открыть отчет в браузере (Windows)

### Структура тестов используется параметризация, фикстуры, Mock и Patch

tests/
├── test_products.py    # Создание, инициация класса Product.
├── test_category.py    # Создание, инициация класса Category, подсчет категорий и количества товаров.
├── conftest.py         # Фикстуры: Функции
├── test_base.py        # Тестирование дочерних классов Category и Order.
├── test_order.py       # Тесты создания заказов.
├──

Все тесты покрыты параметризацией и снабжены комментариями.

---

## ✅ Контроль качества

poetry run flake8 src/
poetry run black src/
poetry run isort src/

---
---

## 📌 Особенности

- ✅ Поддержка Python 3.12+
- 🧠 Полная типизация и валидация
- 🌀 Использование генераторов
- 🔒 Маскировка конфиденциальных данных
- 💯 Покрытие тестами > 85%
- 🧪 Параметризованные тесты и фикстуры
- 🔁 Интеграция с CI/CD через GitHub Actions
- 📦 Poetry как менеджер зависимостей

---
