# Поздравляю! Ты добралась до самого важного раздела, изучив который ты смело можешь говорить, что ты - программист.
# Но, не расслабляйся, это по совместительству и самый сложный раздел, но я в тебя верю.
# Что же такое ООП (Объектно-ориентированное программирование)?
# Объектно-ориентированное программирование – методология программирования,
# основанная на представлении программы в виде совокупности объектов,
# каждый из которых является экземпляром определенного класса, а классы образуют иерархию наследования

# Например, представим объект - человек. Характеристик у него много, но мы ограничемся: имени, возраста, цветом глаз,
# цветом волос, ростом и полом. Как ты догадалась, все эти данные можно поместить в переменные. Так же, человек может что-то делат.
# Для наглядности мы возьмём твои любимые действия: есть, спать и гулять с кем-то (этот кто-то я, кстати).
# Давай напишем такой класс в Python

class Person:
    # Параметр self можно заменить на любой другой, но принято так.
    # Он указывает на собственный элемент класса по умолчанию, его не нужно указывать при вызове методов.
    # Методы - функции, которые находятся внутри класса. Вызываются через точку, кроме уже встроенных в класс
    # Методы могут принимать параметры.

    count = 0 # общий экземпляр класса на всех экземплярах. Называются такие поля - статичными.

    # Для того, чтобы у класса был статичный метод, нужен специальный декоратор
    # Тут мы получаем общее количество созданных нами людей
    @staticmethod
    def static_count():
        return Person.count # такое обращение к статичным полям, тк они не имеют конкретного экземпляра

    # Конструктор класса. Всегда вызывается при создании класса, может как принимать параметры, так и не принимать. (встроенный)
    def __init__(self, name, age, eye_color, hair_color, height, sex):
        # В конструкторе мы задаем значения переменных экземпляра.
        # Если их задать вне конструктора, то эта переменная будет общая для всех экземпляров класса

        self.name = name # имя
        self.age = age # возраст
        self.eye_color = eye_color # цвет глаз
        self.hair_color = hair_color # цвет волос
        self.height = height # рост
        self.sex = sex # пол
        self.partner = None # вторая половинка. Изначально равна None

        Person.count += 1 # Прибавляем общее количество созданных нами людей

    # Методы - функции, которые находятся внутри класса. Вызываются через точку, кроме уже встроенных в класс
    # Методы могут принимать параметры.

    # Метод, который кормит имя человека
    def eat(self, food):
        print(f"{self.name} ест {food}.")

    # Метод, который отвечает за сон человека
    def sleep(self, time):
        print(f"{self.name} спит {time} часов.")

    # Метод, который отвечает за прогулку
    def walk(self, person):
        # Если человек, с которым гуляет наш экземпляр - он сам, то мы выведем сообщение о себе
        if person == self:
            print(f"{self.name} гуляет с собой. Возможно, у {self.name} нет друга(")
        # Если человек, с которым гуляет наш экземпляр - воторая половинка, то мы выведем сообщение о нем
        elif person == self.partner:
            print(f"{self.name} гуляет со второй половинкой, по имени {person} .")
        # Если человек, с которым гуляет наш экземпляр - не сам и не вторая половинка, то мы выведем сообщение о нем
        elif person.partner == None and self.partner == None:
            print(f"{self.name} гуляет с {person}.")
        else:
            print(f"{self.name} гуляет с {person}. {self.partner} ревнует!!!!")


    # Метод, который выведет нам полную информацию о человеке
    def info(self):
        print(f"Имя: {self.name}\nВозраст: {self.age}\nЦвет глаз: {self.eye_color}\nЦвет волос: {self.hair_color}\nРост: {self.height}\n")


    # Метод, который присваивает нашему человеку другую половинку и наоборот, чтобы было удомнее, а так же не было запутанностей
    def set_partner(self, person):
        if self.sex == person.sex:
            print(f"{self.name} и {person} не могут быть половинками, у нас такое запрещено!)")
            return

        if person.partner != None:
            print(f"{person} и {person.partner} расстались(")
            person.partner.partner = None # Если вторая половинка существует - удаляем ее

        if self.partner != None:
            print(f"{self} и {self.partner} расстались(")
            self.partner.partner = None # Если первая половинка существует - удаляем ее

        self.partner = person
        person.partner = self

        print(f"{self} и {person} стали половинками!")

    # Метод для вывода имен о человеке. Вызывается, когда мы хотим переобразовать объект в строку. (встроенный)
    def __str__(self):
        return self.name



# Тперь, давай создадим первый объект
person1 = Person("Настя", 17, "зеленый", "розово-фиолетовый", 170, "ж")
print(Person.count) # 1
person2 = Person("Антон", 18, "карие", "коричневые", 190, "м")
print(Person.count) # 2
person1.info() # Выводим информацию о 1-м человеке
person2.info() # Выводим информацию о 2-м человеке
person3 = Person("Гоша", 18, "карие", "коричневые", 180, "м")
print(Person.count) # 3
person3.info() # Выводим информацию о 3-м человеке

# Так мы получаем доступ к переменным объекта
print(person1.name) # Настя
print(person1.sex) # ж

# А вот так, как ты уже поняла вызываем функции
person1.sleep(5)
person1.eat("доширак")

# Тут вызывается __str__, который переобразует объект как строку
print(person1) # Настя



person1.walk(person2) # Настя гуляет с Антон
person3.walk(person2) # Гоша гуляет с Антон

person1.set_partner(person2) # задаём отношения между Настей и Антоном
person1.walk(person2) # Настя гуляет с Антон

person2.walk(person3) # Антон гуляет с Гоша. Настя ревнует!!!!

print()
person3.set_partner(person2) # задаём отношения между Гошей и Антон
print(person3.partner) # отношений нет, тк есть нельзя с одним и тем же полом

print()

person1.set_partner(person3) # задаём отношения между Настей и Гошей
print(person2.partner) # отношений нет, тк расстались

print()
person1.set_partner(person2) # задаём отношения между Настей и Антон




# Задачи

# 1. Создание простого класса "Car"
# Создайте класс Car с атрибутами: модель, год выпуска и цвет.
# Добавьте метод display_info(), который будет выводить информацию о машине.
# Создайте несколько объектов этого класса и выведите информацию о них с помощью метода display_info().

# 2. Класс "BankAccount"
# Создайте класс BankAccount с атрибутами: номер счета и баланс.
# Добавьте методы deposit(amount) для пополнения счета и withdraw(amount) для снятия средств.
# Метод withdraw должен проверять, достаточно ли средств на счете, и выводить сообщение, если их недостаточно.
# Создайте несколько объектов и протестируйте методы.

# 3. Класс "Student" с методом "get_grade"
# Создайте класс Student с атрибутами: имя и список оценок.
# Добавьте метод get_grade(), который возвращает средний балл студента.
# Создайте несколько объектов и выведите их средние оценки.

# 4. Класс "Library" с атрибутами "книги"
# Создайте класс Book с атрибутами: название, автор и количество страниц.
# Создайте класс Library с атрибутом books (список объектов Book).
# Добавьте методы для добавления книги в библиотеку и для отображения всех книг в библиотеке.
# Создайте несколько книг и добавьте их в библиотеку.

# 5. Класс "Employee" с вычислением зарплаты
# Создайте класс Employee с атрибутами: имя, ставка и отработанные часы.
# Добавьте метод calculate_salary(), который вычисляет заработную плату сотрудника.
# Создайте несколько объектов и выведите их заработную плату.
# Добавьте метод __str__(), который переопределяет стандартное строковое представление объекта.

