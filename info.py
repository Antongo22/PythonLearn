# Строки и Списки

# Списки в Python — это изменяемые упорядоченные коллекции объектов.
# Они позволяют хранить множество элементов в одном объекте, при этом элементы могут быть любого типа,
# и сам список может изменяться после создания (вы можете добавлять, удалять, изменять элементы).
#
# Списки в Python определяются с помощью квадратных скобок [], и элементы в них разделяются запятыми.

# Пустой список
empty_list = []

# Список с несколькими элементами
numbers = [1, 2, 3, 4, 5]

# Список с элементами разных типов
mixed_list = [1, "apple", 3.14, True]

# Список со списками (вложенные списки)
nested_list = [[1, 2], [3, 4], [5, 6]]

# Список с элементами, созданными с помощью функции range
range_list = list(range(1, 6))  # [1, 2, 3, 4, 5]

# Простое заполнение массивов
array = [i for i in range(10)] # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(array)

array = [i for i in range(10) if i % 2 == 0] # [0, 2, 4, 6, 8]
print(array)



my_list = [10, 20, 30, 40, 50]

# Первый элемент
print(my_list[0])  # 10

# Последний элемент
print(my_list[-1])  # 50

# Извлечение подсписка (срез)
print(my_list[1:4])  # [20, 30, 40]

# Каждый второй элемент списка
print(my_list[::2])  # [10, 30, 50]


my_list = [10, 20, 30, 40, 50]

# Изменение второго элемента
my_list[1] = 25
print(my_list)  # [10, 25, 30, 40, 50]

# Изменение нескольких элементов с помощью среза
my_list[2:4] = [35, 45]
print(my_list)  # [10, 25, 35, 45, 50]


# Основные операции со списками
my_list = [1, 2, 3, 4, 5]
print(len(my_list))  # 5

list1 = [1, 2]
list2 = [3, 4]
combined_list = list1 + list2
print(combined_list)  # [1, 2, 3, 4]

my_list = [1, 2]
repeated_list = my_list * 3
print(repeated_list)  # [1, 2, 1, 2, 1, 2]

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # [1, 2, 3, 4]

my_list = [1, 2, 4]
my_list.insert(2, 3)  # Вставляем 3 на позицию с индексом 2
print(my_list)  # [1, 2, 3, 4]


my_list = [1, 2, 3, 4, 5]
my_list.remove(3)
print(my_list)  # [1, 2, 4, 5]

my_list = [1, 2, 3, 4, 5]
removed_item = my_list.pop(2)  # Удаляет элемент с индексом 2
print(my_list)  # [1, 2, 4, 5]
print(removed_item)  # 3

my_list = [1, 2, 3, 4, 5]
last_item = my_list.pop()
print(my_list)  # [1, 2, 3, 4]
print(last_item)  # 5


my_list = [1, 2, 3, 4, 5]
my_list.clear()
print(my_list)  # []

my_list = [10, 20, 30, 40, 50]
print(my_list.index(30))  # 2 (индекс элемента 30)

my_list = [1, 2, 3, 2, 4, 2]
print(my_list.count(2))  # 3 (количество вхождений 2)


# Перебо элиментов списка
my_list = [10, 20, 30, 40, 50]
for item in my_list:
    print(item)

# Или же можно по индексам
my_list = [10, 20, 30, 40, 50]
for i in range(len(my_list)):
    print(my_list[i])

# Сортировка и обратный порядок
my_list = [4, 2, 8, 5, 1]
my_list.sort()
print(my_list)  # [1, 2, 4, 5, 8]

my_list = [4, 2, 8, 5, 1]
my_list.sort(reverse=True)
print(my_list)  # [8, 5, 4, 2, 1]

# Обратный порядок
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]


# Копирование.
original_list = [1, 2, 3]
copy_list = original_list.copy()
# или
copy_list = original_list[:]

# Если просто присвимть одно значение копирование не произойдет, а будет ссылка на тот же элимент
my_list = [1, 2, 3]
another_list = my_list
another_list[0] = 10
print(my_list)  # [10, 2, 3]

# Обмен значениями в массиве
my_list = [1, 2, 3]
my_list[0], my_list[2] = my_list[2], my_list[0]
print(my_list)  # [3, 2, 1]


# Обмен значениями
a = 10
b = 20
tmp = a
a = b
b = tmp
print(a)  # 20
print(b)  # 10





# Строки
# Одинарные кавычки
str1 = 'Hello, World!'

# Двойные кавычки
str2 = "Hello, World!"

# Тройные кавычки для многострочного текста
str3 = '''This is
a multi-line
string.'''

str4 = """This is another
multi-line string."""


str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # "Hello World"


str1 = "Hi!"
result = str1 * 3
print(result)  # "Hi!Hi!Hi!"


str1 = "Hello"
print(str1[0])  # 'H' (первый символ)
print(str1[-1])  # 'o' (последний символ)


str1 = "Hello, World!"
print(str1[0:5])  # "Hello" (символы с 0 по 4)
print(str1[7:])   # "World!" (символы с 7 до конца строки)
print(str1[:5])   # "Hello" (символы с начала до 4)
print(str1[::2])  # "Hlo ol!" (каждый второй символ)


str1 = "Hello, World!"
print(len(str1))  # 13 (количество символов в строке)


str1 = "Hello, World!"
print("World" in str1)  # True
print("Python" in str1)  # False


str1 = "Hello, World!"
print(str1.upper())  # "HELLO, WORLD!"
print(str1.lower())  # "hello, world!"
print(str1.capitalize())  # "Hello, world!"
print(str1.title())  # "Hello, World!"

# Проверка на то, что строка КАПСОМ
if str1.isupper():
    print("Строка КАПСОМ")

# Проверка на то, что строка маленькими буквами
if str1.islower():
    print("Строка маленькими буквами")


str1 = "Hello, World!"
print(str1.find("World"))  # 7 (начальный индекс подстроки "World")
print(str1.replace("World", "Python"))  # "Hello, Python!"

str1 = "apple,banana,cherry"
fruits = str1.split(",")  # ['apple', 'banana', 'cherry']

fruits = ['apple', 'banana', 'cherry']
str1 = ", ".join(fruits)
print(str1)  # "apple, banana, cherry"

str1 = "  Hello, World!  "
print(str1.strip())  # "Hello, World!" (удаление пробелов с обеих сторон)
print(str1.lstrip())  # "Hello, World!  " (удаление пробелов слева)
print(str1.rstrip())  # "  Hello, World!" (удаление пробелов справа)


str1 = "Hello123"
print(str1.isalpha())  # False (содержит не только буквы)
print(str1.isdigit())  # False (содержит не только цифры)
print(str1.isalnum())  # True (содержит буквы и цифры)


name = "Alice"
age = 25
greeting = f"Hello, {name}! You are {age} years old."
print(greeting)  # "Hello, Alice! You are 25 years old."


greeting = "Hello, {}! You are {} years old.".format("Alice", 25)
print(greeting)  # "Hello, Alice! You are 25 years old."


# Неизменяемость строк
# Строки в Python неизменяемы, что означает, что вы не можете изменить символы в существующей строке.
# Любые операции, которые кажутся изменяющими строку, на самом деле создают новую строку.

str1 = "Hello"
# Следующая операция создаст новую строку
str2 = str1.replace("H", "J")
print(str1)  # "Hello" (оригинальная строка не изменилась)
print(str2)  # "Jello" (новая строка)






# Работа с файлами
# Открытие и закрытие файлов

file = open("filename.txt", "r")  # Открыть файл для чтения
# После работы необходимо закрыть
file.close()

# "r" (read) — Открытие файла для чтения. Если файл не существует, возникает ошибка.
# "w" (write) — Открытие файла для записи. Если файл существует, его содержимое будет удалено. Если файл не существует, он будет создан.
# "a" (append) — Открытие файла для добавления данных в конец. Если файл не существует, он будет создан.
# "r+" — Открытие файла для чтения и записи.

# Чтение всего файла целиком:
file = open("filename.txt", "r")
content = file.read()
print(content)
file.close()

# Чтение построчно:
file = open("filename.txt", "r")
for line in file:
    print(line, end='')  # end='' убирает дополнительный перевод строки
file.close()


# Чтение определенного количества символов:
file = open("filename.txt", "r")
content = file.read(10)  # Читает первые 10 символов
print(content)
file.close()

# Запись в файл

#Запись строки:
file = open("filename.txt", "w")
file.write("Hello, world!")
file.close()


# Запись нескольких строк:
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]

file = open("filename.txt", "w")
file.writelines(lines)
file.close()


# Работа с файлом с использованием with
# Использование with позволяет автоматически закрывать файл после завершения работы с ним, даже если в процессе работы возникла ошибка.

with open("filename.txt", "r") as file:
    content = file.read()
    print(content)
# Здесь файл уже закрыт


# Проверка существования файла:
import os

if os.path.exists("filename.txt"):
    print("Файл существует.")
else:
    print("Файл не найден.")


# Удаление файла:
import os

if os.path.exists("filename.txt"):
    os.remove("filename.txt")
    print("Файл удален.")
else:
    print("Файл не найден.")

# Пример: Чтение и запись в файл
with open("input.txt", "r") as infile:
    lines = infile.readlines()

with open("output.txt", "w") as outfile:
    for line in lines:
        outfile.write(line.upper())


# Словари

# Словари (или dict — от английского "dictionary") в Python — это структура данных,
# которая позволяет хранить пары "ключ — значение".
# Это означает, что для каждого элемента в словаре есть уникальный ключ,
# с помощью которого можно получить доступ к соответствующему значению.
# Словари очень удобны для хранения и быстрого поиска данных по ключу.

my_dict = {} # Создание пустого словаря

my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
} # Создание словаря с элементами

my_dict = dict(name="Alice", age=25, city="New York") # Создание словаря с элементами через функцию dict()


# Доступ к элементам словаря
my_dict = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

print(my_dict["name"]) # "Alice"
print(my_dict["age"]) # 25
print(my_dict["city"]) # "New York"


# Если попытаться обратиться к несуществующему ключу, будет вызвана ошибка KeyError. Чтобы этого избежать, можно использовать метод get:
print(my_dict.get("country", "Not Found"))  # Вывод: Not Found


# Добавление и изменение элементов
my_dict["email"] = "alice@example.com"  # Добавление новой пары
my_dict["age"] = 26  # Изменение существующего значения


# Удаление элемента по ключу:
del my_dict["age"]

# Удалиние и возврат элимента
age = my_dict.pop("age")
print(age)  # Вывод: 26

# Очистка всего словаря
my_dict.clear()

# Проверка наличия ключа:
if "name" in my_dict:
    print("Ключ 'name' существует")

# Перебор ключей и значений:
for key in my_dict:
    print(key, my_dict[key])

# Или использовать методы items(), keys(), values()
for key, value in my_dict.items():
    print(f"{key}: {value}")

# Получение всех ключей или всех значений:
keys = my_dict.keys()      # Возвращает список всех ключей
values = my_dict.values()  # Возвращает список всех значений


# Подсчет количества вхождений элементов
text = "hello world"
char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)

# Словари часто используются для хранения настроек и конфигураций:
config = {
    "host": "localhost",
    "port": 8080,
    "debug": True
}


# Вложенные словари

students = {
    "Alice": {"age": 25, "city": "New York"},
    "Bob": {"age": 22, "city": "Los Angeles"}
}

print(students["Alice"]["city"])  # Вывод: New York


# Полезные методы словарей

my_dict.update({"country": "USA", "city": "Boston"}) # update() — обновляет словарь, добавляя пары из другого словаря
my_dict.setdefault("age", 30) # setdefault() — возвращает значение ключа, если ключ существует,
# или устанавливает значение по умолчанию и возвращает его, если ключ не существует






# Обработка ошибок
# Иерархия исключений

# BaseException
# +-- SystemExit
# +-- KeyboardInterrupt
# +-- Exception
#   +-- ArithmeticError
#     | +-- FloatingPointError
#     | +-- OverflowError
#     | +-- ZeroDivisionError
#   +-- EOFError
#   +-- ImportError
#     +-- ModuleNotFoundError
#   +-- LookupError
#     | +-- IndexError
#     | +-- KeyError
#   +-- NameError
#   +-- OSError
#     | +-- FileExistsError
#     | +-- FileNotFoundError
#     | +-- NotADirectoryError
#   +-- ReferenceError
#   +-- RuntimeError
#   +-- SyntaxError
#     | +-- IndentationError
#   +-- SystemError
#   +-- TypeError
#   +-- ValueError
#   +-- Warning


# BaseException
# Базовый класс всех исключений
# KeyboardInterrupt
# Возбуждается нажатием клавишей прерывания
# SystemExit
# Завершение программы
# Exception
# Базовый класс для всех исключений, не связанных с завершением программы
# StandardError
# Базовый класс всех исключений, наследующих класс Exception
# ArithmeticError
# Базовый класс исключений, возбуждаемых арифметическими операциями
# FloatingPointError
# Ошибка операции с плавающей точкой
# ZeroDivisionError
# Деление или деления по модулю на ноль
# AttributeError
# Возбуждается при обращении к несуществующему атрибуту
# EnvironmentError
# Ошибка, обусловленная внешними причинами
# IOError
# Ошибка ввода-вывода при работе с файлами
# OSError
# Ошибка операционной системы
# EOFError
# Возбуждается по достижении конца файла
# ImportError
# Ошибка в инструкции import
# LookupError
# Ошибка обращения по индексу или ключу
# IndexError
# Ошибка обращения по индексу за пределами последовательности
# KeyError
# Ошибка обращения к несуществующему ключу словаря
# NameError
# Не удалось отыскать локальное или глобальное имя
# UnboundLocalError
# Ошибка обращения к локальной переменной, которой еще не было присвоено значение
# ReferenceError
# Ошибка обращения к объекту, который уже был уничтожен
# RuntimeError
# Универсальное исключение
# NotImplementedError
# Обращение к нереализованному методу или функции
# SyntaxError
# Синтаксическая ошибка
# IndentationError
# Ошибка оформления отступов
# SystemError
# Нефатальная системная ошибка в интерпретаторе
# TypeError
# Попытка выполнить операцию над аргументом недопустимого типа
# ValueError
# Недопустимый тип


# Обработка исключений
try:
    x = int(input("Введите число: "))
    result = 10 / x
    print(f"Результат: {result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введено не число!")


# Использование else и finally

# else: Этот блок выполняется, если код в try завершился успешно, т.е. не вызвал исключения.
#
# finally: Этот блок выполняется в любом случае — и если было исключение, и если его не было.
# Его часто используют для очистки ресурсов (например, закрытия файлов).

try:
    x = int(input("Введите число: "))
    result = 10 / x
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except ValueError:
    print("Ошибка: Введено не число!")
else:
    print(f"Результат: {result}")
finally:
    print("Завершение работы программы.")


# Перехват нескольких исключений
try:
    x = int(input("Введите число: "))
    result = 10 / x
except (ZeroDivisionError, ValueError):
    print("Ошибка: Некорректный ввод!")


# Исключение без указания типа
try:
    x = int(input("Введите число: "))
    result = 10 / x
except:
    print("Произошла ошибка!")



# Генерация собственных исключений


a = 10
b = 10
try:
    if b == 0:
        raise ValueError("Делитель не может быть равен нулю.")
    print(a / b)
except ValueError as e:
    print(f"Ошибка: {e}")

# Заключение
# Обработка ошибок — это способ делать ваши программы более устойчивыми к непредвиденным ситуациям,
# что особенно важно в реальных приложениях.
# Применяя обработку ошибок, вы можете предусмотреть разные сценарии работы программы и
# корректно реагировать на возможные сбои, обеспечивая тем самым ее надежность и стабильность.



# Функции
# Функции — это блок кода, который может быть вызван из других функций.
# Функции могут принимать аргументы и возвращать значения. Могут и не принимать

# для того, чтобы определить функцию, необходимо использовать ключевое слово def и дальше в скобках передать парметры
def my_func(name):
    print(f"Hello, {name}!")

# Эта функция ничего не возвращяет, а просто приветсвует пользователя

# Вызов функции
my_func("World")
my_func("Python")

# Однако, функции могут возвращять значения
def get_name():
    return input("Введите имя: ")

name = get_name()
print(f"Hello, {name}!")
# Тут в функции мы получаем имя пользователя и возвращяем его

# Можно и совместить!
def get_sum(a, b):
    print(a + b)
    return a + b

sum = get_sum(10, 20)
# Тут функция и выводит результат и возвращяет его

# В функции можно вызывать другие функции
def get_name():
    return input("Введите имя: ")

def get_age():
    return input("Введите возраст: ")

def show_info():
    return f"Hello, {get_name()}! You are {get_age()} years old."

print(show_info())

# В функции можно вызывать саму себя!
def sum(a, b):
    print(a, b)
    if a > 100:
        return a + b
    else:
        return sum(a + 1, b)

print(sum(1, 2))

# Тут мы прибавляем к первому числу второе, пока оно не станет больше 100

# Очень важно продумывать выход из функции, иначе будет ошибка переполнения памяти

# Аргументы по умолчанию
# Функции могут иметь аргументы по умолчанию, которые используются, если при вызове функции соответствующие аргументы не были переданы.
def power(base, exponent=2):
    return base ** exponent

print(power(3))     # Возвращает 9, так как exponent по умолчанию равен 2
print(power(3, 3))  # Возвращает 27

# Именованные и позиционные аргументы
# При вызове функции можно использовать именованные аргументы для явного указания значений параметров.
# Это улучшает читаемость кода и позволяет указывать аргументы в произвольном порядке.

def profile(name, age, city):
    print(f"Name: {name}, Age: {age}, City: {city}")

profile(age=25, name="Bob", city="New York")


# Переменное количество аргументов
# Функции могут принимать переменное количество аргументов с помощью *args и **kwargs.
# *args используется для передачи произвольного количества позиционных аргументов в виде кортежа.
def print_numbers(*args):
    for number in args:
        print(number)

print_numbers(1, 2, 3, 4, 5)


# **kwargs используется для передачи произвольного количества именованных аргументов в виде словаря.
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=30, city="Paris")


# Лямбда-функции
square = lambda x: x ** 2 # Пишется ключевое слово lambda, после параметры функции, а затем выражение
print(square(4))  # Вывод: 16
# Лямбда-функции — это небольшие анонимные функции, которые определяются с помощью ключевого слова lambda.
# Они обычно используются для коротких функций, которые не требуют имени.


# Вложенные функции
# Функции могут быть определены внутри других функций. Вложенные функции имеют доступ к переменным внешних функций.
def outer_function(x):
    def inner_function(y):
        return y * y
    return inner_function(x) + 1

print(outer_function(3))  # Вывод: 10



# Функции как объекты
# Функции в Python являются объектами первого класса, что означает,
# что их можно передавать как аргументы другим функциям, возвращать из функций и присваивать переменным.
def add(a, b):
    return a + b

def apply_function(func, x, y):
    return func(x, y)

result = apply_function(add, 5, 3)  # result будет равен 8


# Декораторы
# Декораторы — это функции, которые модифицируют поведение других функций.
# Они часто используются для добавления функциональности, такой как логирование или проверка прав доступа.
def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print("Wrapper executed")
        return original_function(*args, **kwargs)
    return wrapper_function

@decorator_function
def display():
    return "Display function executed"

print(display())  # Вывод: Wrapper executed \n Display function executed

# Ууу, сложна! Но, давай разберём как оно работает
def decorator_function(func):
    def wrapper_function():
        print("До вызова функции")
        func()
        print("После вызова функции")
    return wrapper_function

def function_to_be_used():
    print("Эта функция будет вызвана")

function_to_be_used = decorator_function(function_to_be_used)

function_to_be_used() # До вызова функции \n Эта функция будет вызвана \n После вызова функции

# Тут мы просто как аргумент функции передаём другую функцию, да, так можно!
# Но, возникает проблема, если мы хотим, чтобы функция вызывала другую функцию,
# то придётся функцию-декоратор каждый раз настраивать плд вызываемую функцию, а это не вариант!
# Для решения этой проблемы мы передаём *args, **kwargs как аргументы декоратора, для того,
# чтобы наш декоратор был универсальным


def decorator_function1(func):
    def wrapper_function(*args, **kwargs):
        print("До вызова функции")
        func(*args, **kwargs)
        print("После вызова функции")
    return wrapper_function

def function_to_be_used1(title):
    print(title)

function_to_be_used = decorator_function1(function_to_be_used1)

function_to_be_used("Text") # До вызова функции \n Text \n После вызова функции

# Уже лучше! Но, что если функция будет что-то возвращять
def decorator_function2(func):
    def wrapper_function(*args, **kwargs):
        print("До вызова функции")
        answer = func(*args, **kwargs)
        print("После вызова функции")
        return answer
    return wrapper_function

def function_to_be_used2(title):
    print("Вызвано")
    return "Hello " + title

function_to_be_used = decorator_function1(function_to_be_used2)

print(function_to_be_used("Text")) # До вызова функции \n Вызвано \n После вызова функции \n Hello Text

# Отлично! Но, чтобы было удобнее, мы напишем так -

def decorator_function3(func):
    def wrapper_function(*args, **kwargs):
        print("До вызова функции")
        answer = func(*args, **kwargs)
        print("После вызова функции")
        return answer
    return wrapper_function

@decorator_function3
def function_to_be_used3(title):
    print("Вызвано")
    return "Hello " + title


print(function_to_be_used3("Text")) # До вызова функции \n Вызвано \n После вызова функции \n Hello Text

# По сути - то же самое, просто удобнее


# так же можно возвращать несколько параметров

def return_tuple(a, b):
    return b, a

a, b = return_tuple(1, 2)
print(a, b)

# Функции в Python — это основной инструмент для организации кода, улучшения его читаемости и
# повторного использования. Они позволяют абстрагировать логику и выполнять операции с аргументами,
# возвращая результаты. Функции могут быть простыми или сложными, поддерживать переменное количество аргументов
# и работать как объекты первого класса, что делает их мощным инструментом в вашем арсенале программиста.
