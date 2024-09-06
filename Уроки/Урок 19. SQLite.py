# Ну, с хранениями данных в файлах мы вроде разобрались.
# Но, на больших объёмах будет проблема - это медленно и занимает много места.
# А как мы ещё можем хранить данные? Правильно, в таблицах!
# Для работы с такими таблицами есть свои разные системы и свой язык - SQL.
# То, где данные хранится, называется - База Данных (БД).
# А программа для работы с этой БД называется - Система Управления Базами Данных (СУБД).
# Но, это очень огромная тема, и всю её мы тут явно не поместим, и к тому же нужно будет уметь работать ещё и с СУБД.
# Но, что если мы хотим прямо сейчас? На помощь нам идёт SQLite, которому не обязательно СУБД.
# Однако, чтобы удобно просматривать данные, лучше всё же скачать "DB Browser for SQLite".
# Итак, для начало изучим основу SQL (языка).

# В SQL есть несколько основных операторов, которые используются для выполнения задач
# по работе с данными в таблицах базы данных. Начнем с самых важных из них:

# 1. Создание таблицы
# Оператор CREATE TABLE используется для создания новой таблицы в базе данных.

# SQL:
# CREATE TABLE users (
#     id INTEGER PRIMARY KEY,    -- Уникальный идентификатор пользователя
#     name TEXT NOT NULL,        -- Имя пользователя, обязательное поле
#     age INTEGER,               -- Возраст пользователя, необязательное поле
#     email TEXT UNIQUE          -- Email пользователя, уникальное поле
# );

# 2. Вставка данных
# Оператор INSERT INTO используется для добавления новых строк (записей) в таблицу.

# SQL:
# INSERT INTO users (name, age, email) VALUES ('Alice', 30, 'alice@example.com');

# 3. Запрос данных
# Оператор SELECT используется для извлечения данных из одной или нескольких таблиц.

# SQL:
# SELECT * FROM users;  # Извлечение всех записей из таблицы users
# SELECT name, email FROM users WHERE age > 25;  # Извлечение имен и email пользователей старше 25 лет

# 4. Обновление данных
# Оператор UPDATE используется для изменения существующих записей в таблице.

# SQL:
# UPDATE users SET age = 31 WHERE name = 'Alice';  # Обновление возраста пользователя с именем Alice

# 5. Удаление данных
# Оператор DELETE используется для удаления существующих записей в таблице.

# SQL:
# DELETE FROM users WHERE age < 18;  # Удаление всех пользователей младше 18 лет

# 6. Удаление таблицы
# Оператор DROP TABLE используется для удаления существующей таблицы вместе со всеми данными в ней.

# SQL:
# DROP TABLE users;  # Удаление таблицы users

# 7. Дополнительные операторы
# Есть много других полезных операторов SQL, таких как:
# - ALTER TABLE: изменение структуры существующей таблицы (добавление или удаление столбцов)
# - JOIN: объединение данных из двух или более таблиц
# - ORDER BY: сортировка данных по определенному столбцу
# - GROUP BY: группировка данных на основе определенных столбцов

# Пример использования JOIN:
# SQL:
# SELECT users.name, orders.amount
# FROM users
# JOIN orders ON users.id = orders.user_id;  # Получение списка имен пользователей и сумм их заказов

# Пример использования ORDER BY:
# SQL:
# SELECT * FROM users ORDER BY age DESC;  # Извлечение всех пользователей и сортировка по возрасту в порядке убывания

# Пример использования GROUP BY:
# SQL:
# SELECT age, COUNT(*) FROM users GROUP BY age;  # Подсчет количества пользователей для каждого возраста

# 8. Фильтрация данных
# Ключевое слово WHERE позволяет фильтровать записи на основе условий.

# SQL:
# SELECT * FROM users WHERE age BETWEEN 20 AND 30;  # Извлечение пользователей в возрасте от 20 до 30 лет

# Таким образом, SQL предоставляет мощные инструменты для управления данными в реляционных базах данных.
# Это всего лишь краткий обзор, но он дает представление о том, как использовать SQL для выполнения
# основных операций с данными. На практике, знание SQL поможет вам работать с данными гораздо эффективнее!


# Работа с SQLite в Python выполняется с помощью встроенного модуля sqlite3.
# Давай рассмотрим основные операции с базами данных SQLite.

import sqlite3  # Подключаем модуль sqlite3

# 1. Создание или подключение к базе данных
# Если база данных не существует, она будет создана автоматически.
# Если файл базы данных существует, будет установлено соединение с ним.

connection = sqlite3.connect('example.db')  # Создаем или подключаемся к базе данных 'example.db'

# 2. Создание курсора
# Курсор используется для выполнения SQL-запросов и получения результатов.

cursor = connection.cursor()

# 3. Создание таблицы
# Для создания таблицы в SQLite используем SQL-оператор CREATE TABLE.
# Если таблица уже существует, то выведется ошибка, поэтому используем IF NOT EXISTS.

cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,  -- Уникальный идентификатор пользователя
    name TEXT NOT NULL,      -- Имя пользователя, обязательное поле
    age INTEGER,             -- Возраст пользователя, необязательное поле
    email TEXT UNIQUE        -- Email пользователя, уникальное поле
)
''')

# 4. Вставка данных в таблицу
# Используем SQL-оператор INSERT INTO для добавления новых записей в таблицу.

cursor.execute('''
INSERT INTO users (name, age, email) VALUES (?, ?, ?)
''', ('Alice', 30, 'alice@example.com'))  # Параметры передаем в виде кортежа

# 5. Сохранение изменений
# После выполнения операций вставки, обновления или удаления данных,
# нужно сохранить изменения с помощью commit().

connection.commit()

# 6. Извлечение данных из таблицы
# Используем SQL-оператор SELECT для получения данных из таблицы.

cursor.execute('SELECT * FROM users')  # Извлекаем все записи из таблицы users
rows = cursor.fetchall()  # Получаем все строки результата запроса

# Выводим извлеченные данные
for row in rows:
    print(row)

# 7. Обновление данных в таблице
# Используем SQL-оператор UPDATE для изменения существующих данных в таблице.

cursor.execute('''
UPDATE users SET age = ? WHERE name = ?
''', (31, 'Alice'))  # Обновляем возраст пользователя с именем Alice

connection.commit()  # Сохраняем изменения

# 8. Удаление данных из таблицы
# Используем SQL-оператор DELETE для удаления записей из таблицы.

cursor.execute('''
DELETE FROM users WHERE age < ?
''', (18,))  # Удаляем всех пользователей младше 18 лет

connection.commit()  # Сохраняем изменения

# 9. Закрытие соединения
# После завершения всех операций с базой данных, важно закрыть соединение.

connection.close()

# 10. Обработка исключений
# Желательно обернуть все операции с базой данных в блок try-except для обработки ошибок.

try:
    connection = sqlite3.connect('example.db')
    cursor = connection.cursor()
    # Выполнение операций с базой данных...
except sqlite3.Error as e:
    print(f'Ошибка при работе с базой данных: {e}')
finally:
    if connection:
        connection.close()  # Гарантированно закрываем соединение


# Так же работа с бд поддерживает with



# Задание 1: Создание таблицы и добавление данных
# 1. Создайте таблицу 'products' с колонками: id (PRIMARY KEY), name (TEXT), price (REAL).
# 2. Добавьте в таблицу 3 записи с данными о продуктах (например, 'Apple', 'Banana', 'Orange') и их ценами.


# Задание 2: Извлечение данных с условием
# 1. Извлеките все записи из таблицы 'products', где цена больше 1.3.
# 2. Выведите их на экран.

# Задание 3: Обновление данных в таблице
# 1. Обновите цену для продукта 'Banana' до 1.5.
# 2. Извлеките все записи, чтобы убедиться в изменении.

# Задание 4: Удаление данных из таблицы
# 1. Удалите все записи из таблицы 'products', где цена меньше 1.6.
# 2. Выведите оставшиеся записи.

# Задание 5: Работа с несколькими таблицами (JOIN)
# 1. Создайте таблицу 'orders' с колонками: id (PRIMARY KEY), product_id (INTEGER), quantity (INTEGER).
# 2. Добавьте 3 записи в таблицу 'orders' с указанием 'product_id' и 'quantity'.
# 3. Используя INNER JOIN, извлеките названия продуктов и их количество из таблицы 'orders'.
# INNER JOIN используется в SQL для объединения строк из двух или более таблиц на основе связанного между ними столбца.
# Он возвращает только те строки, у которых есть совпадение в обоих объединяемых таблицах.