# 🗃 Database Crash Course
Ускоренный курс по базам данных за 30 минут

Database Shield
License

🚀 Экспресс-старт
Что внутри:

Основы SQL и NoSQL за 15 минут

5 практических примеров

Шпаргалки для работы

Тестовые задания

# Для начала работы (PostgreSQL):
sudo apt install postgresql
sudo -u postgres psql -c "CREATE DATABASE quickstart;"
📌 Ядро курса
1. SQL за 5 минут
Создаем таблицу:

CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  name VARCHAR(50),
  email VARCHAR(100) UNIQUE
);

CRUD операции:
- Вставка
INSERT INTO users (name, email) VALUES ('Anna', 'anna@mail.com');

-- Чтение
SELECT * FROM users WHERE name LIKE 'A%';

-- Обновление
UPDATE users SET email = 'new@mail.com' WHERE id = 1;

-- Удаление
DELETE FROM users WHERE id = 1;

2. NoSQL за 5 минут (MongoDB)
javascript
// Вставка документа
db.users.insertOne({
  name: "Alex",
  age: 25,
  skills: ["JS", "Python"]
});

// Поиск
db.users.find({ age: { $gt: 20 } });

;
🧪 Практика
Задание 1: Создайте таблицу products с полями:

id (первичный ключ)

name (текст)

price (число)

in_stock (булево)

Решение:

sql
CREATE TABLE products (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100) NOT NULL,
  price DECIMAL(10,2),
  in_stock BOOLEAN DEFAULT FALSE
);
📚 Шпаргалки
SQL vs NoSQL
Операция	SQL	NoSQL
Вставка	INSERT INTO...	db.collection.insertOne()
Поиск	SELECT...WHERE	db.collection.find()
Обновление	UPDATE...SET	db.collection.updateOne()
💡 Полезные команды
bash
# PostgreSQL
psql -U username -d dbname  # Вход в консоль
\dt                         # Показать таблицы

# MongoDB
mongo                       # Вход в консоль
show collections            # Показать коллекции
🏆 Что дальше?
Изучите JOIN-операции (SQL)

Попробуйте агрегации в MongoDB

Поэкспериментируйте с индексами

