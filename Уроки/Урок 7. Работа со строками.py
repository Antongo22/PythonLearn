# Строки
# Одинарные кавычки
str1 = 'Hello, World!'

# Двойные кавычки
str2 = "Hello, World!"

# Где может пригодится
st1 = "Книга с названием 'ОЧЕНЬ ИНТЕРЕСНАЯ КНИГА'!"
st2 = 'Книга с названием "ОЧЕНЬ ИНТЕРЕСНАЯ КНИГА"!'

# Обратный слеш "\"

# Для кавычек '\"'
st3 = "Книга с названием \"ОЧЕНЬ ИНТЕРЕСНАЯ КНИГА\"!"
# Для переноса стоки '\n'
st4 = "Книга с названием \"ОЧЕНЬ\nИНТЕРЕСНАЯ\nКНИГА\"!"
# Для табуляции '\t'
st5 = "Книга с названием \"ОЧЕНЬ\tИНТЕРЕСНАЯ\tКНИГА\"!"
# Для возврата каретки '\r'
st6 = "Книга с названием \"ОЧЕНЬ\rИНТЕРЕСНАЯ\rКНИГА\"!"
# Для пустого символа '\0'
st7 = "Книга с названием \"ОЧЕНЬ\0ИНТЕРЕСНАЯ\0КНИГА\"!"

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


# Так же можно узнать сколько находится символов в стоке
str = "a.a.d.f"
print(str.count(".")) # 3
print(str.count("a")) # 2


# Методы строк
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


# Строки
# Палиндром:
# Напишите программу, которая проверяет, является ли введенная строка палиндромом (строка, читающаяся одинаково слева направо и справа налево).
#
# Пример:
# Ввод: "level"
# Вывод: "Да, это палиндром."
# n = input()
# f = len(n)
# k = 0
# for i in range(f):
#     if n[i]==n[-i-1]:
#         k+=1
# if k==f:
#     print("Yes")
# else:
#     print("No")

# Количество слов в строке:
# Напишите программу, которая подсчитывает количество слов в заданной строке.
#
# Пример:
# Ввод: "Hello, world! How are you?"
# Вывод: 5 слов
# n = input()
# print(n.count(" ")+1)
# f = len(n.split(" "))
# print(f)

# Замена подстроки:
# Напишите программу, которая заменяет все вхождения подстроки в строке на другую подстроку.
#
# Пример:
# Ввод: "Hello, world!", замените "world" на "Python"
# Вывод: "Hello, Python!"
# n = input()
# k = input()
# l = input()
# print(n.replace(k, l))

# Удаление гласных из строки:
# Напишите программу, которая удаляет все гласные буквы из заданной строки.
#
# Пример:
# Ввод: "This is a test"
# Вывод: "Ths s tst"
# n = input()
# n = n.replace("a","")
# n = n.replace("e","")
# n = n.replace("y","")
# n = n.replace("u","")
# n = n.replace("i","")
# n = n.replace("o","")
# print(n)

# n = input()
# f = "qwrtpsdfghjklzxcvbnm"
# s = []
# for i in range(len(n)):
#     for j in range(20):
#         if n[i]==f[j]:
#             h = n.replace(f[j],"")
#             s.append(f[j])
# n = "".join(s)
# print(n)

n = input()
f = 'aeyuio'
s = []
for i in range(len(n)):
    if n[i] not in f:
        s.append(n[i])
k = "".join(s)
print(k)
