# Магические методы в Python
# Это методы, которые начинаются и заканчиваются двумя подчеркиваниями (__).
# Они позволяют перегружать операторы и встроенные функции, чтобы делать ваши классы более мощными.

# Перегрузка операторов сравнения
class Gamer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __eq__(self, person):
        return self.age == person.age

    def __lt__(self, person):
        return self.age < person.age

    def __gt__(self, person):
        return self.age > person.age


john = Gamer('John', 25)
pete = Gamer('Pete', 33)
mike = Gamer('Mike', 25)

print(john == mike)  # True
print(mike > john)   # False
print(john < pete)   # True
print()

# Деструктор
# Специальный метод __del__(self), который вызывается при удалении объекта.
# В деструкторе можно определить действия, которые надо выполнить при удалении объекта.
class Person:
    def __init__(self, name):
        self.name = name
        print("Создан человек с именем", self.name)

    def __del__(self):
        print("Удален человек с именем", self.name)


tom = Person("Tom")
print()

# Магические методы для строкового представления объектов
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    # Магический метод для "читаемого" строкового представления
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # Магический метод для "официального" строкового представления. Используется чтобы получить прям полную информацию
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"


book = Book("1984", "George Orwell")
print(book)  # Вызывается __str__
print(repr(book))  # Вызывается __repr__
print()

# Магические методы для арифметических операций
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(2, 3)
v2 = Vector(1, 4)
print(v1 + v2)  # Вывод: Vector(3, 7)
print(v1 - v2)  # Вывод: Vector(1, -1)
print()

# Магические методы для индексации и доступа
class CustomList:
    def __init__(self, *args):
        self.data = list(args)

    def __getitem__(self, index):
        return self.data[index]

    def __setitem__(self, index, value):
        self.data[index] = value

    def __delitem__(self, index):
        del self.data[index]

    def __str__(self):
        return str(self.data)


lst = CustomList(1, 2, 3, 4, 5)
print(lst[2])  # Вывод: 3
lst[2] = 10
print(lst)  # Вывод: [1, 2, 10, 4, 5]
del lst[2]
print(lst)  # Вывод: [1, 2, 4, 5]
print()

# Магические методы для функции len и логических проверок
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __bool__(self):
        return len(self.items) > 0


collection = MyCollection([1, 2, 3])
print(len(collection))  # Вывод: 3
print(bool(collection))  # Вывод: True
empty_collection = MyCollection([])
print(bool(empty_collection))  # Вывод: False
print()

# Магические методы для контекстных менеджеров (with)
class Resource:
    def __enter__(self):
        print("Ресурс открыт")
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        print("Ресурс закрыт")


with Resource() as res:
    print("Внутри блока with")

# Вывод:
# Ресурс открыт
# Внутри блока with
# Ресурс закрыт



# Задачи

# Задача 1: Перегрузка операторов сравнения
# Создайте класс `Rectangle`, который будет представлять прямоугольник с атрибутами длина и ширина.
# Переопределите операторы `==`, `<`, и `>` для сравнения площади прямоугольников.
# Напишите несколько примеров использования этих операторов для объектов класса `Rectangle`.

# Задача 2: Перегрузка арифметических операторов
# Создайте класс `ComplexNumber` для работы с комплексными числами.
# Реализуйте методы `__add__`, `__sub__`, `__mul__` и `__truediv__` для перегрузки операторов +, -, *, / соответственно.
# Напишите несколько примеров использования этих операторов для объектов класса `ComplexNumber`.

# Задача 3: Магические методы строкового представления
# Создайте класс `Car` с атрибутами модель и год выпуска. Реализуйте методы `__str__` и `__repr__`.
# `__str__` должен возвращать удобочитаемую строку для пользователя, а `__repr__` — строку, которую можно использовать для создания аналогичного объекта.
# Проверьте вывод обоих методов для нескольких объектов класса `Car`.

# Задача 4: Магические методы индексации и доступа
# Создайте класс `Matrix`, представляющий двумерную матрицу. Реализуйте магические методы `__getitem__`, `__setitem__`, и `__delitem__`
# для доступа, изменения и удаления элементов матрицы. Проверьте работу этих методов на примере.

# Задача 5: Магические методы длины и логических проверок
# Создайте класс `Queue` для работы с очередью. Реализуйте магические методы `__len__` и `__bool__`.
# `__len__` должен возвращать количество элементов в очереди, а `__bool__` — True, если очередь не пуста, и False, если пуста.
# Проверьте работу этих методов на примере.

# Задача 6: Контекстный менеджер
# Создайте класс `FileHandler`, который будет использоваться для открытия и закрытия файлов.
# Реализуйте магические методы `__enter__` и `__exit__` для управления открытием и закрытием файлов.
# Напишите пример использования этого класса в блоке `with`.

# Задача 7: Деструктор
# Создайте класс `UserSession`, который будет симулировать сеанс пользователя в приложении.
# Реализуйте деструктор `__del__`, который будет автоматически завершать сеанс при удалении объекта.
# Создайте несколько объектов `UserSession` и посмотрите, как вызывается деструктор.

# Задача 8: Перегрузка оператора приведения типа
# Создайте класс `Temperature` для представления температуры в градусах Цельсия.
# Реализуйте магический метод `__float__`, который будет возвращать значение температуры в градусах по Фаренгейту.
# Напишите пример использования приведения объекта `Temperature` к типу `float`.

# Задача 9: Перегрузка оператора вызова
# Создайте класс `Polynomial`, представляющий многочлен. Реализуйте магический метод `__call__`, чтобы можно было вычислить значение многочлена при заданном `x`.
# Напишите несколько примеров создания объектов класса `Polynomial` и вызова их с различными значениями `x`.

# Задача 10: Перегрузка оператора вхождения
# Создайте класс `WordCollection`, представляющий коллекцию слов.
# Реализуйте магический метод `__contains__`, чтобы можно было проверять, содержится ли слово в коллекции, используя оператор `in`.
# Проверьте работу метода на нескольких примерах.


# Финальное задание. Напиши игру тамагочи, где у тебя будут 3 животных - собака, кошка и хомяк.
# Пользователь может выбрать с каким животным играть
# После каждого действия, животное теряет очки еды и интереса. Важно - держать их стабильно.
# Животное может и играть, если выполнено действие еды, то очки за ход еды не снимаются.
# Каждый ход идёт подсчёт очков. После проигрыша игра предлагает сыграть ещё или закончить.
# По мере игры, очков снимается всё больше, чтобы пользователь рано или поздно гарантированно проиграл.