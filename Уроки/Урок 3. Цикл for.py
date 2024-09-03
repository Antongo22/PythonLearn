# Цикл for

# Цикл от 1 до 11 с шагом 2
for i in range(1, 12, 2):
    print(i)

# i - переменная, которая хранит текущей итерации (действие), вместо i может быть любое число
# in - ключевое слово между переменной и множеством
# range - функция, которая генерирует последовательность чисел
# range(11) - генерируем последовательность чисел от 0 до 10
# range(1, 11) - генерируем последовательность чисел от 1 до 10
# range(1, 11, 2) - генерируем последовательность чисел от 1 до 10 с шагом 2

# Вложенные циклы
for i in range(1, 5):
    for j in range(1, i + 1):
        print("*", end="")
    print()
    
    
# Выведите на экран 10 раз фразу "You are welcome!"
# Выведите на экран n раз фразу "Silence is golden". Число n вводит пользователь.
# Выведите на экран прямоугольник из нулей. Количество строк вводит пользователь, количество столбцов равно 5.
#
# Вывести на экран фигуру из звездочек:
# *******
# *******
# *******
# *******
# (квадрат из n строк, в каждой строке n звездочек)
#1
# for i in range(11):
#     print("You are welcome!")
# #2
# n = int(input())
# for j in range(1,n+1):
#     print("Silence is golden")
# #3
# a = int(input())
# for f in range(1,6):
#     for t in range(1,a+1):
#         print("0", end="")
#     print()
# #4
# s = int(input())
# d = int(input())
# for k in range (1,s):
#     for h in range(1,d):
#         print("*", end="")
#     print()
# #Вывести на экран числа от 1000 до 9999 такие, что среди цифр есть цифра 3.
# #5
# for i in range(1000,9999):
#     if i%10==3 or i//10%10==3 or i//100%10==3 or i//1000==3:
#         print(i)
# Выведите на экран строки вида:
# *******
# ****
# *******
# ****
# *******
# ****
# (всего n строк, звездочек или 7, или 4 по очереди)
#6
# n = int(input())
# for i in range(1,n+1):
#     if i%2!=0:
#         for j in range(1,8):
#             print("*", end="")
#         print()
#     if i%2==0:
#         for h in range(1,5):
#             print("*", end="")
#         print()
# Вывести на экран:
# AAABBBAAABBBAAABBB
# BBBAAABBBAAABBBAAA
# AAABBBAAABBBAAABBB
# (таких строк n, в каждой строке m троек AAA)
#7
# d=0
# e=0
# n = int(input())
# m = int(input())
# for i in range(1,n+1):
#     if i%2!=0:
#         d = "AAABBB"*m
#         print(d)
#     if i%2==0:
#         e = "BBBAAA"*m
#         print(e)

# n = int(input())
# m = int(input())
# for i in range(1,n+1):
#     if i%2!=0:
#         for j in range(1,m+1):
#             print("AAABBB", end="")
#         print()
#     if i%2==0:
#         for f in range(1,m+1):
#             print("BBBAAA", end="")
#         print()
# Вывести на экран:
# AAAAAAAAAAAAAAAA
# ABBBBBBBBBBBBBBA
# ABBBBBBBBBBBBBBA
# ABBBBBBBBBBBBBBA
# AAAAAAAAAAAAAAAA
# (количество строк вводит пользователь, ширина прямоугольника в два раза больше высоты)
#8
# n = int(input())
# for i in range(1,n+1):
#     if i == 1 or i==n:
#         for j in range(1,2*n+1):
#             print("A", end="")
#         print()
#     else:
#         for h in range(1,2*n+1):
#             if h == 1 or h==2*n:
#                 print("A",end="")
#             else:
#                 print("B",end="")
#         print()
# Выведите на экран квадрат из нулей и единиц, причем нули находятся только на диагонали квадрата. Всего в квадрате сто цифр. Обе диагонали состоят из 0
#9
n = int(input())
for i in range(1,n+1):
    for j in range(1,n+1):
        if i==j or i+j==n+1:
            print("0", end = "")
        else:
            print("1", end = "")
    print()
