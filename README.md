# 🌐 REST API для управления товарами (ДЗ №16)

Учебное приложение на Flask, реализующее REST API для обработки HTTP-запросов (GET, POST, PUT, DELETE).

## 🛠️ Технологии
* Python 3
* Flask
* JSON

## 🚀 Как запустить
1. Установите Flask: `pip install flask`
2. Запустите сервер: `python main.py`
3. Сервер будет доступен по адресу: `http://127.0.0.1:5000`

## 📋 Эндпоинты API

| Метод | URL | Описание | Путевой параметр |
| :--- | :--- | :--- | :--- |
| **GET** | `/api/items` | Получить список всех товаров | Нет |
| **GET** | `/api/items/<id>` | Получить один товар по ID | Да |
| **POST** | `/api/items` | Создать новый товар | Нет |
| **PUT** | `/api/items/<id>` | Обновить данные товара | Да |
| **DELETE** | `/api/items/<id>` | Удалить товар | Да |

## 🧪 Пример тестирования (через curl или Postman)

**Создание товара (POST):**

curl -X POST http://127.0.0.1:5000/api/items \

-H "Content-Type: application/json" \

-d '{"name": "Монитор", "price": 300}'

Обновление товара (PUT):

curl -X PUT http://127.0.0.1:5000/api/items/3 \

-H "Content-Type: application/json" \

-d '{"price": 250}'