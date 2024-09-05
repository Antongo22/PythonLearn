# Ты уже умеешь получать данные из текстового файла.
# Но, в реальности в txt файлах не хранят информацию, тк с большим объёмом работать неудобно
# Поэтому, есть специальные расширения, которые помогают удобно хранить и получать данны.
# Самые популярные это json и xml.
# Начнём с xml, тк в питоне с ним работают реже.

# XML (eXtensible Markup Language) — это язык разметки, который используется для хранения и передачи структурированных данных.
# XML похож на HTML, но он предназначен для описания данных и их структуры, а не для представления данных пользователю.
# Пример XML-документа:

"""
<company>
    <employee>
        <name>John Doe</name>
        <age>30</age>
        <department>IT</department>
    </employee>
    <employee>
        <name>Jane Smith</name>
        <age>25</age>
        <department>HR</department>
    </employee>
</company>
"""

# В этом примере `<company>` — это корневой элемент, который содержит два элемента `<employee>`,
# каждый из которых имеет свои дочерние элементы `<name>`, `<age>`, и `<department>`.

# Работа с XML в Python
# Python предоставляет несколько библиотек для работы с XML, таких как `xml.etree.ElementTree`, `lxml`, и `minidom`.
# Мы рассмотрим стандартную библиотеку `xml.etree.ElementTree`,
# которая встроена в Python и не требует дополнительной установки.

import xml.etree.ElementTree as ET

# Пример XML-документа в виде строки
xml_data = """
<company>
    <employee>
        <name>John Doe</name>
        <age>30</age>
        <department>IT</department>
    </employee>
    <employee>
        <name>Jane Smith</name>
        <age>25</age>
        <department>HR</department>
    </employee>
</company>
"""

# Парсинг XML из строки
root = ET.fromstring(xml_data)

# Просмотр корневого элемента
print(root.tag)  # Вывод: company

# Просмотр всех дочерних элементов
for employee in root:
    print(employee.tag)

# Чтение данных из XML
for employee in root.findall('employee'):
    name = employee.find('name').text
    age = employee.find('age').text
    department = employee.find('department').text
    print(f"Name: {name}, Age: {age}, Department: {department}")
print()

# Создание XML-документа
# Мы можем создавать XML-документы с помощью `ElementTree`.

root = ET.Element('company')  # Создание корневого элемента

# Добавление дочерних элементов
employee1 = ET.SubElement(root, 'employee')
ET.SubElement(employee1, 'name').text = 'Alice'
ET.SubElement(employee1, 'age').text = '28'
ET.SubElement(employee1, 'department').text = 'Marketing'

employee2 = ET.SubElement(root, 'employee')
ET.SubElement(employee2, 'name').text = 'Bob'
ET.SubElement(employee2, 'age').text = '35'
ET.SubElement(employee2, 'department').text = 'Sales'

# Преобразование дерева в строку
tree = ET.ElementTree(root)
tree.write('output.xml')  # Сохранение в файл

# Чтение XML из файла
tree = ET.parse('output.xml')  # Загрузка из файла
root = tree.getroot()
print(root.tag)  # Вывод: company
print()

# Изменение XML-документа
# Мы можем изменить существующий XML-документ, используя те же методы `find` и `findall`.

for employee in root.findall('employee'):
    department = employee.find('department')
    if department.text == 'Sales':
        department.text = 'Business Development'

tree.write('modified_output.xml')  # Сохранение измененного XML

# Удаление элементов из XML-документа
# Чтобы удалить элемент, мы можем использовать метод `remove`.

for employee in root.findall('employee'):
    age = employee.find('age')
    if int(age.text) > 30:
        root.remove(employee)

tree.write('reduced_output.xml')  # Сохранение после удаления


# Подведение итогов

# Парсинг XML: Используйте ET.fromstring() для загрузки XML из строки или ET.parse() для загрузки из файла.
# Извлечение данных: Используйте методы find(), findall() и text для извлечения данных из элементов.
# Создание XML: Используйте ET.Element() и ET.SubElement() для создания новых XML-документов.
# Изменение XML: Можно изменять значения текстов и атрибутов элементов с помощью find() и прямого присвоения.
# Удаление элементов: Используйте метод remove() для удаления элементов из XML-документа.



# Как работать с xml, примерно понятно. Теперь можно перейти к json.
# Его структура тебе знакома. Это по сути словарь, помещённый в файл.

# JSON (JavaScript Object Notation) — это легковесный формат обмена данными, удобный для чтения и написания как человеком, так и машиной.
# JSON широко используется для передачи данных между сервером и веб-приложением в формате "ключ-значение".

# Вот пример JSON-документа:

"""
{
  "company": {
    "employees": [
      {
        "name": "John Doe",
        "age": 30,
        "department": "IT"
      },
      {
        "name": "Jane Smith",
        "age": 25,
        "department": "HR"
      }
    ]
  }
}
"""

# В JSON есть несколько типов данных:
# 1. Объекты (ключ-значение) — {...}
# 2. Массивы — [...]
# 3. Строки — "..."
# 4. Числа — 1, 2.5, -3
# 5. Логические значения — true, false
# 6. Значение null

# Работа с JSON в Python
# В Python есть встроенная библиотека `json` для работы с JSON.

import json

# Пример JSON-документа в виде строки
json_data = """
{
  "company": {
    "employees": [
      {
        "name": "John Doe",
        "age": 30,
        "department": "IT"
      },
      {
        "name": "Jane Smith",
        "age": 25,
        "department": "HR"
      }
    ]
  }
}
"""

# Загрузка JSON из строки
data = json.loads(json_data)

# Доступ к данным
print(data['company']['employees'][0]['name'])  # Вывод: John Doe

# Перебор всех сотрудников
for employee in data['company']['employees']:
    print(f"Name: {employee['name']}, Age: {employee['age']}, Department: {employee['department']}")
print()

# Загрузка JSON из файла
# Создадим JSON-файл для примера.
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)  # Запись данных в файл с отступами для читабельности

# Чтение JSON из файла
with open('data.json', 'r') as file:
    data_from_file = json.load(file)

print(data_from_file['company']['employees'][1]['name'])  # Вывод: Jane Smith
print()

# Запись JSON в строку
json_string = json.dumps(data, indent=4)
print(json_string)  # Вывод JSON-данных в виде строки
print()

# Создание JSON-данных с нуля
new_data = {
    "company": {
        "employees": [
            {"name": "Alice", "age": 28, "department": "Marketing"},
            {"name": "Bob", "age": 35, "department": "Sales"}
        ]
    }
}

# Запись нового JSON в файл
with open('new_data.json', 'w') as file:
    json.dump(new_data, file, indent=4)

# Изменение JSON-данных
# Пример изменения значения в JSON-объекте

new_data['company']['employees'][0]['department'] = 'Digital Marketing'

# Запись измененного JSON в файл
with open('modified_data.json', 'w') as file:
    json.dump(new_data, file, indent=4)

# Удаление данных из JSON
# В JSON удаление элемента происходит с использованием функции del

del new_data['company']['employees'][1]  # Удаление второго сотрудника

# Запись JSON после удаления в файл
with open('reduced_data.json', 'w') as file:
    json.dump(new_data, file, indent=4)

print("JSON data modified and saved to 'modified_data.json' and 'reduced_data.json'.")


# Подведение итогов
# Загрузка JSON: Используйте json.loads() для загрузки JSON из строки и json.load() для загрузки из файла.
# Запись JSON: Используйте json.dumps() для преобразования данных в строку JSON и json.dump() для записи в файл.
# Доступ к данным: JSON объекты можно обрабатывать как вложенные словари и списки.
# Изменение и удаление данных: Изменяйте значения ключей, используя стандартные методы Python для словарей, и удаляйте элементы с помощью del.
# Форматирование JSON: Используйте параметр indent в json.dumps() и json.dump() для более читабельного формата.


# Задачи
# Задания по работе с XML и JSON в Python

# 1. XML Задания

# Задание 1: Парсинг XML и вывод всех отделов сотрудников
# Напишите программу, которая будет парсить XML-документ и выводить названия всех отделов сотрудников.

xml_data = """
<company>
    <employee>
        <name>John Doe</name>
        <age>30</age>
        <department>IT</department>
    </employee>
    <employee>
        <name>Jane Smith</name>
        <age>25</age>
        <department>HR</department>
    </employee>
    <employee>
        <name>Emily Davis</name>
        <age>40</age>
        <department>Finance</department>
    </employee>
</company>
"""


# Задание 2: Создание XML-документа
# Создайте XML-документ, который будет содержать информацию о нескольких продуктах (имя, цена, категория).
# Сохраните его в файл `products.xml`.


# Задание 3: Изменение XML-документа
# Напишите программу, которая будет загружать XML-файл, созданный в Задании 2, и увеличивать цену всех продуктов на 10%.
# Сохраните измененный файл под новым именем `updated_products.xml`.


# Задание 4: Удаление элемента из XML
# Напишите программу, которая будет удалять всех сотрудников старше 35 лет из `xml_data`.
# Сохраните результат в новом XML-файле `filtered_employees.xml`.


# Задание 5: Создание и изменение XML-документа
# Создайте XML-документ, представляющий собой каталог книг (название, автор, год публикации).
# Затем измените автора одной из книг и сохраните результат в `updated_books.xml`.



# 2. JSON Задания

# Задание 1: Загрузка и доступ к JSON
# Дано JSON-данные о студентах и их оценках. Загрузите их и выведите средний балл для каждого студента.

json_data = """
{
  "students": [
    {"name": "Alice", "grades": [85, 92, 78]},
    {"name": "Bob", "grades": [79, 94, 88]},
    {"name": "Charlie", "grades": [95, 87, 92]}
  ]
}
"""

# Задание 2: Создание JSON-файла
# Напишите программу, которая создает JSON-файл `movies.json` с данными о фильмах (название, год, жанр, рейтинг).


# Задание 3: Изменение JSON-данных
# Загрузите JSON-файл `movies.json`, добавьте новый фильм и сохраните изменения под именем `updated_movies.json`.


# Задание 4: Удаление элементов из JSON
# Загрузите JSON-данные из `movies.json` и удалите все фильмы с рейтингом ниже 7.0.
# Сохраните измененный список фильмов в файл `filtered_movies.json`.


# Задание 5: Чтение и изменение JSON из файла
# Напишите программу, которая будет читать JSON-файл с данными о сотрудниках (имя, должность, зарплата).
# Увеличьте зарплату каждого сотрудника на 10% и сохраните изменения в новый файл `updated_salaries.json`.

# Финальное задание. Хранить в любом из форматов тест на любую тему. Написать программу,
# которая будет тестировать поьлзователя. Решить с использованием ООП.