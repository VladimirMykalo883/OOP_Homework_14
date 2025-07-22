<p align="center">
  <img src="https://img.icons8.com/clouds/500/bank-card-back-side.png" alt="bank operations logo" width="160"/>
</p>

<h1 align="center"># Проект по управлению продуктами и категориями</h1>

<p align="center">
  <strong>Этот проект реализует систему управления продуктами и категориями с использованием ООП в Python</strong><br>
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

## 🧰 Функциональные модули

### 🔍 products.py  инициация и создание класса Product

- - Класс `Product` для представления товаров с атрибутами:
  - Название
  - Описание
  - Цена
  - Количество в наличии

### 🔐Category - инициация и создание класса Product

- Класс `Category` для представления категорий товаров с атрибутами:
  - Название категории
  - Описание категории
  - Список товаров в категории
  - Автоматический подсчет количества категорий и товаров

###



###



###

###

###
---

## 🚀 Примеры использования







## 🧪 Тестирование

Запуск тестов и генерация отчёта покрытия:

poetry run pytest --cov=src --cov-report=html
start htmlcov/index.html  # открыть отчет в браузере (Windows)

### Структура тестов используется параметризация, фикстуры, Mock и Patch

tests/
├── test_products.py    # Создание, инициация класса Prolact
├── test_category.py    # Создание, инициация класса Category, подсчет категорий и количества товаров
├── conftest.py           # фикстуры: Функции
├──
├──
├──
├──
├──
├──              #

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
