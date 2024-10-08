# Кортежи
# Это неизменяемая упорядоченная коллекция объектов в Python.
# Кортежи не могут быть изменены после их создания.
# Кортежи используются для хранения множества элементов в одном объекте, особенно когда важна неизменяемость данных.

# Пустой кортеж
empty_tuple = ()
# Кортеж с несколькими элементами
tuple1 = (1, 2, 3)
# Кортеж с элементами разных типов
tuple2 = (1, "apple", 3.14)
# Кортеж с вложенными структурами данных
tuple3 = (1, (4, 5))
# Кортеж с одним элементом (обязательно добавить запятую)
single_element_tuple = (42,)

# Доступ к элементам кортежа
my_tuple = (10, 20, 30, 40)
# Доступ к первому элементу
print(my_tuple[0])  # 10
# Доступ к последнему элементу
print(my_tuple[-1])  # 40
# Доступ к срезу кортежа (от второго до третьего элемента включительно)
print(my_tuple[1:3])  # (20, 30)


# Основные операции с кортежами
my_tuple = (1, 2, 3)
print(len(my_tuple))  # Длина кортежа

tuple1 = (1, 2)
tuple2 = (3, 4)
combined_tuple = tuple1 + tuple2 # Объединение кортежей
print(combined_tuple)  # (1, 2, 3, 4)

my_tuple = (1, 2)
repeated_tuple = my_tuple * 3 # Повторение
print(repeated_tuple)  # (1, 2, 1, 2, 1, 2)

my_tuple = (1, 2, 3) # Проверка на наличие
print(3 in my_tuple)  # True
print(4 in my_tuple)  # False

my_tuple = (1, 2, 3) # Итерация
for item in my_tuple:
    print(item)
# Вывод:
# 1
# 2
# 3



# Работа с random и math
import random
a = random.randint(0, 10)
b = random.randint(0, 10)
c = random.randint(0, 10)
d = random.randint(0, 10)
print(a, b, c, d)

# random(): Возвращает случайное число с плавающей точкой в диапазоне от 0.0 до 1.0.
# uniform(a, b): Возвращает случайное число с плавающей точкой в диапазоне от a до b.
# randint(a, b): Возвращает случайное целое число из диапазона от a до b включительно.
# randrange(start, stop[, step]): Возвращает случайное число из последовательности, начиная с start и заканчивая stop (не включая stop) с шагом step.
# choice(seq): Возвращает случайное число из последовательности seq.
# shuffle(seq): Перемешивает элименты последовательности seq
a = random.choice((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(a)

s = [0, 1, 2, 3]
random.shuffle(s)
print(s)

# Работа с math
import math
a = math.sqrt(4) # корень
b = math.pow(2, 3) # степень
c = math.pi # число Пи
d = math.e # число E
print(a, b, c, d)

# A.is_integer() - проверка, целое ли число



#Напишите программу, которая загадывает случайное число от 1 до 100.
# Пользователь должен угадать это число.
# Программа должна продолжать запрашивать у пользователя числа, пока он не угадает правильно.
# Если пользователь вводит число меньше загаданного, программа выводит сообщение "Загаданное число больше".
# Если больше — "Загаданное число меньше". Если пользователь угадывает, программа выводит "Поздравляем!
# Вы угадали число!" и завершает работу.
import random
a = random.randint(1,100)
while True:
    n = int(input())
    if n==a:
        print("Молодец, ты угадал число")
        break
    elif n!=a:
        if n>a:
            print("Загаданное число меньше")
        elif n<a:
            print("Загаданное число больше")


# Написать игру камень ножницы бумага с использованием кортежей.
# Играют до 3 побед, пользователь может повторно играть без перезапуска программы
import random

while True:
    s = 0  # победа пользователя
    c = 0  # победа компьютера
    while s!=3 and c!=3:
        a = random.choice(("камень", "ножницы", "бумага"))
        b = input("Введите камень, ножницы или бумагу: ")
        print(f"Компьютер выбрал: {a}")
        if a==b:
            print("Ничья")
        elif (b =="камень" and a=="ножницы") or (b=="ножницы" and a=="бумага") or (b=="бумага" and a=="камень"):
            s+=1
            print("Победа")
        else:
            c+=1
            print("Поражение")

    print()

    if s==3:
        print("Вы победили")
    else:
        print("Вы проиграли")

    print()
    n = int(input("Введите 1, чтобы продолжить. Введите 0, чтобы закончить"))
    if n==1:
        continue
    break


# Вывести 3 случайных числа от 0 до 100 без повторений.
# Найдите количество прямоугольных треугольников с целочисленными сторонами, меньшими 100.
#1
# import random
# while True:
#     a = random.randint(0,100)
#     b = random.randint(0,100)
#     c = random.randint(0,100)
#     if a==b or b==c or c==a:
#         continue
#     print(a,b,c)
#     break
# s = 0
#
# for a in range(1,100):
#     for b in range(a,100):
#         c = (a**2 + b **2) ** 0.5
#
#         if c.is_integer() and c < 100:
#             print(f"{a}^2 + {b}^2 = {c}^2")
#             s +=1
#
# print(s)

# Глухая бабушка
# Что бы вы ни говорили бабуле (чтобы вы ни вводили с консоли), она должна отвечать:
# АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!,
# если только вы не кричите ей (вводите слова заглавными буквами).
#
# Если вы кричите, она вас слышит (или по крайней мере думает, что слышит) и вопит в ответ:
#
# НЕТ, НИ РАЗУ С 1938 ГОДА!.
# Чтобы сделать вашу программу действительно правдоподобной, пусть бабуля кричит каждый раз другой год:
# например, любой случайный год между 1930 и 1950.
#
# Для того, чтобы остановить разговор с бабулей, надо прокричать ПОКА!
# Примерный диалог с бабушкой может выглядеть так:
#
# ЧЕГО СКАЗАТЬ-ТО ХОТЕЛ, МИЛОК?!
# > который час?
# АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!
# > я спрашиваю: который час?
# АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!
# > КОТОРЫЙ ЧАС?
# НЕТ, НИ РАЗУ С 1944 ГОДА!
# > хорошая погода сегодня
# АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!
# > ХОРОШАЯ ПОГОДА!!!
# НЕТ, НИ РАЗУ С 1933 ГОДА!
# > ПОКА!
# ДО СВИДАНИЯ, МИЛЫЙ!
# Улучшите вашу программу (на максимальный балл):
# Что если бабуля не хочет, чтобы вы уходили? Когда вы кричите ПОКА!, она может притвориться, что не слышит вас.
#
# Измените ваш код так, чтобы вам нужно было прокричать ПОКА! три раза подряд.
# Удостоверьтесь в правильности вашей программы:
# если вы прокричите ПОКА! три раза, но в одной строке, вы должны и дальше разговаривать с бабулей.
# Примерный диалог в изменённой программе может выглядеть так:
# > ПОКА!
# НЕТ, НИ РАЗУ С 1934 ГОДА!
# > ПОКА! ПОКА! ПОКА!
# НЕТ, НИ РАЗУ С 1946 ГОДА!
# > ПОКА!
# НЕТ, НИ РАЗУ С 1943 ГОДА!
# > ПОКА!
# НЕТ, НИ РАЗУ С 1941 ГОДА!
# > ПОКА!
# ДО СВИДАНИЯ, МИЛЫЙ!
import random
s = 0
while True:
    a = random.randint(1930,1950)
    b = input("ЧЕГО ХОТЕЛ СКАЗАТЬ, МИЛОК? : ")

    if b=="ПОКА!":
        print(f"НЕТ, НИ РАЗУ С {a} ГОДА!")
        s+=1
    else:
        s = 0
        if b.islower() :
            print("АСЬ?! ГОВОРИ ГРОМЧЕ, ВНУЧЕК!")
        if b.isupper():
            print(f"НЕТ, НИ РАЗУ С {a} ГОДА!")

    if s == 3:
        print("ДО СВИДАНИЯ, МИЛЫЙ!")
        break
