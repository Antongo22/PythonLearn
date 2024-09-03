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
my_list = [4, 2, 8, 5, 1]
reversed(my_list)
print(my_list)  # [1, 5, 8, 2, 4]


# Обратный порядок
my_list = [1, 2, 3, 4, 5]
my_list.reverse()
print(my_list)  # [5, 4, 3, 2, 1]


# Копирование.
original_list = [1, 2, 3]
copy_list = original_list.copy()
# или
copy_list = original_list[:]
copy_list[0] = 10
print(original_list)
print(copy_list)

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


# Двумерные массивы
my_array = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

# Для доступа к элементу нужно обратится по двум []
print(my_array[1][1])

# Заполнение двумерного массива
array = []
for i in range(10):
    array.append([j for j in range(10)])

print(array)

# Или
n = 5 # сколько будет вложенных массивов
m = 3 # сколько элиментов в каждом вложенном массиве
array = []
for i in range(n):
    array.append([0] * m)
    for j in range(m):
        array[i][j] = 0
print(array)

# Вывод двумерного массива
for item in array:
    for i in item:
        print(i, end='')
    print()
# или
for i in range(len(array)):
    for j in range(len((array[i]))):
        print(array[i][j], end='')
    print()


# Удаление всех дубликатов путём апмведения массива к множесиву (set)
s = [0, 1, 0, 2, 1, 2]
a = set(s)
print(a) # {0, 1, 2}
s = list(a)
# Приводим множество обратно к списку (list)
print(s) # [0, 1, 2]
# set - множество, которое хранит только уникальные значения



# Массиивы (Списки)
# Заполнить массив нулями, кроме первого и последнего элементов, которые должны быть равны единице.
# n = int(input())
# s = [0 for i in range(n)]
# s[0]=1
# s[-1]=1
# print(s)
import random

# Заполнить массив нулями и единицами, при этом данные значения чередуются, начиная с нуля.
# s = [0,1]
# n = int(input())
# a = s*n
# print(a)

# n = int(input())
# s = []
# for i in range(n) :
#     if i%2==0:
#         s.append(0)
#     if i%2==1:
#         s.append(1)
# print(s)

# Заполнить массив последовательными нечетными числами, начиная с единицы.
# n = int(input())
# s = [i for i in range(1,n+1, 2)]
# print(s)

# Сформировать массив из элементов арифметической прогрессии с заданным первым элементом x и разностью d.
# x = int(input())
# d = int(input())
# n = int(input())
# s = []
# while True:
#     for i in range(1,n+1):
#         f = x+(i-1)*d
#         a = f
#         s.append(a)
#     print(s)
#     break

# Сформировать возрастающий массив из четных чисел.
# n = int(input())
# s = [ i for i in range(0,n,2)]
# print(s)

# Сформировать убывающий массив из чисел, которые делятся на 3.
# n = int(input())
# s = [i for i in range(1,n+1) if i%3==0]
# s.sort(reverse=True)

# n = int(input())
# s = []
# i = 0
# while True:
#     i+=1
#     if i%3==0:
#         s.append(i)
#         if len(s)==n:
#             print(s)
#             break


# Создать массив из n первых чисел Фибоначчи.
# n = int(input())
# s = [0]
# if n == 0:
#     pass
# elif n == 1:
#     s.append(1)
# else:
#     s.append(1)
#     while n != len(s):
#         s.append(s[-1] + s[-2])
# print(s)

# Заполнить массив заданной длины различными простыми числами.
# Натуральное число, большее единицы, называется простым, если оно делится только на себя и на единицу.
# n = int(input())
# i = 1
# a = 0
# s = []
# while len(s)!=n:
#     i+=1
#     d = True
#     for b in range(2,i):
#         if i%b==0:
#             d = False
#             break
#     if d:
#         s.append(i)
#  print(s)

# Создать массив, каждый элемент которого равен квадрату своего номера.
# n = int(input())
# s = [0]
# i = 0
# f = 0
# while len(s)!=n:
#     i+=1
#     f = i**2
#     s.append(f)
# print(s)

# n = int(input())
# s = []
# f = 0
# for i in range(n+1):
#     f = i**2
#     s.append(f)
# print(s)

# Создать массив, на четных местах в котором стоят единицы,
# а на нечетных местах - числа, равные остатку от деления своего номера на 5.
# n = int(input())
# s = []
#
# for i in range(n) :
#     if i%2==0:
#         s.append(1)
#     else:
#         print(i)
#         s.append(i%5)
# print(s)

# Найдите наименьший четный элемент массива.
# import random
# n = int(input())
# f = 0
# a = [random.randint(1, 100) for i in range(n)]
# min = 100
#
# for i in a:
#     if i%2==0 and i<min:
#         min=i
# print(a,min)

# Среди элементов с нечетными номерами найдите наибольший элемент массива, который делится на 3.
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# max = 0
# for i in range(1, len(s),2):
#     for j in s:
#         if j>max and j%3==0:
#             max=j
# print(s,max)

# Дан массив и число p. Найдите два различных числа в массиве,
# сумма которых наиболее близка к p. (использовать math)
# import random
# import math
# p = math.pi
# k = 0
# a = 0
# g = 100
# n = int(input()) #кол-во символов
# s = [random.randint(1,5) for i in range (n)]
# for j in s:
#     for f in s:
#         g1 = abs((j + f) - math.pi)
#         if g1<g:
#             g = g1
#             k = j
#             a = f
# print(s)
# print(k,a)

#Найдите сумму чисел массива, которые расположены до первого четного числа массива.
# Если четных чисел в массиве нет, то найти сумму всех чисел за исключением крайних.
# import random
# n = int(input())
# arr = [random.randint(1,10) for i in range(n)]
# sum =  0
# is_no = False
#
# for j in arr:
#     if j%2==0 and not is_no:
#         print(j)
#         is_no = True
#         break
#     sum += j
#
# print(arr)
# if is_no:
#     print(sum)
# else:
#     print(sum - arr[0] - arr[-1])

# Минимальный и максимальный элемент массива:
# Напишите программу, которая находит и выводит минимальный и максимальный элементы в заданном массиве целых чисел.
#
# Пример:
# Ввод: [4, 1, 7, 0, 3, 5]
# Вывод: Минимальный: 0, Максимальный: 7
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# min = 100
# max = 0
# for j in s:
#     if max<j:
#         max=j
#     if min>j:
#         min = j
# print(s)
# print(f"Минимальный элемент: {min}. Макстмальный элемент: {max}")

# Сортировка массива по возрастанию и убыванию:
# Реализуйте программу, которая сортирует массив по возрастанию и убыванию. Выведите оба варианта сортировки.
#
# Пример:
# Ввод: [4, 2, 9, 1, 5, 6]
# Вывод: По возрастанию: [1, 2, 4, 5, 6, 9], По убыванию: [9, 6, 5, 4, 2, 1]
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# a = s.copy()
# s.sort()
# a.sort(reverse=True)
# print(f"По возрастанию:{s} . По убыванию: {a}.")

# Сумма и среднее значение элементов массива:
# Напишите программу, которая вычисляет сумму всех элементов массива и среднее значение этих элементов.
#
# Пример:
# Ввод: [10, 20, 30, 40, 50]
# Вывод: Сумма: 150, Среднее: 30.0
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range (n)]
# sum = 0
# for j in s:
#     sum+=j
# g = sum/len(s)
# print(s)
# print(f"Сумма:{sum}. Среднее:{g}.")



# Сдвиг элементов массива:
# Напишите программу, которая сдвигает все элементы массива на одну позицию вправо. Последний элемент массива должен стать первым.
#
# Пример:
# Ввод: [1, 2, 3, 4, 5]
# Вывод: [5, 1, 2, 3, 4]
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range (n)]
# print(s)
# d = [s[-1]]
# a = s.pop(-1)
# print(d+s)

# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# d = []
# h = [s[-1]]
# print(s)
# print(h)
# for i in s:
#     if i==s[-1]:
#         continue
#     else:
#         d.append(i)
# print(h+d)

# Заполнить двуменый массив нулями, диагонали еденицами. Красиво вывести
# Или
# n = int(input())
# s = []
# f = 0
# g = n
# for i in range(n):
#     s.append([0] * n)
#     for j in range(n):
#         s[i][j] = 0
# for i in range(n):
#     for j in range(n):
#         if i==j:
#             s[i][j]=1
#         elif i+j==n+1:
#             s[n-i][n-j]=1
#         if i+j==n-1 and (i==0 or j==0):
#             s[i][j]=1
# for i in range(len(s)):
#     for j in range(len((s[i]))):
#         print(f'{s[i][j]} ', end='')
#     print()
# Задача 2: Заполнение матрицы числами по возрастанию
# Создайте двумерный массив размером m x n и заполните его числами по возрастанию, начиная с 1.
#
# Пример:
# Для m = 2 и n = 3 результат должен быть:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# n = int(input())
# m = int(input())
# s = []
# f = 0
# for i in range(n):
#     s.append([0]* m)
#     for j in range(m):
#         f += 1
#         s[i][j] = f
# print(s)

# Задача 3: Подсчет суммы элементов в строке
# Дан двумерный массив размером m x n. Найдите и выведите сумму элементов в каждой строке. После сделать подсчёт по столбцам
#
# Пример:
# Для массива:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Результат должен быть: 6, 15, 24.
# import random
# m = int(input())
# n = int(input())
# s = []
# f = 0
# c = []
# for i in range(n):
#     b = 0
#     s.append([0]* m)
#     for j in range(m):
#         s[i][j] = random.randint(1,100)
#         c = s[i]
#         b += c[j]
#     print(b)
# print(s)

# Задача 4: Транспонирование матрицы
# Дана матрица размером m x n. Создайте новую матрицу, которая является транспонированной версией исходной, то есть замените строки на столбцы.
#
# Пример:
# Для матрицы:
# [
#   [1, 2, 3],
#   [4, 5, 6]
# ]
# Результат должен быть:
# [
#   [1, 4],
#   [2, 5],
#   [3, 6]
# ]
# m = int(input())
# n = int(input())
# s = []
# f = 0
# k = 0
# h = 0
# for i in range(n):
#     s.append([0]* m)
#     for j in range(m):
#         f += 1
#         s[i][j] = f
# print(s)
# k = m
# m = n
# n = k
# h = []
# for i in range(m):
#     h.append([0]* n)
#     for j in range(n):
#         h[i][j] = s
# print(h)
# Задача 5: Сумма всех элементов двумерного массива
# Дан двумерный массив размером m x n. Найдите сумму всех элементов в массиве.
# Пример:
# Для массива:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
# Результат должен быть: 45.
# import random
# m = int(input())
# n = int(input())
# s = []
# b = 0
# for i in range(n):
#     s.append([0]* m)
#     for j in range(m):
#         s[i][j] = random.randint(1,10)
#         b += s[i][j]
# print(b)
# print(s)

# Дан массив, сделать его сортировку по возрастанию.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# for i in range(n):
#     print(s)
#     for j in range(n-1-i):
#         if s[j]>s[j+1]:
#             f = s[j]
#             s[j]=s[j+1]
#             s[j+1]=f
# print(s)

# import random
# n = int(input())
# s = [random.randint(1,5) for i in range (n)]
# d = []
# for i in s:
#     if s.count(i)>1:
#         d.append(i)
# print(s)
# print(d)

# Задача 1: Заполнение массива числами от 1 до n
# Создайте массив из n элементов, где каждый элемент равен своему индексу + 1.
# n = int(input())
# s = []
# for i in range(1,n+1):
#     s.append(i)
# print(s)

# Задача 2: Вывод элементов массива в обратном порядке
# Дан массив чисел. Выведите элементы массива в обратном порядке.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# f = []
# print(s)
# for i in range(1, n+1):
#     f.append(s[-i])
# print(f)

# Задача 3: Подсчет суммы элементов массива
# Дан массив чисел. Найдите и выведите сумму всех элементов массива.
# import random
# n = int(input())
# s = [random.randint(1,10) for i in range(n)]
# f = 0
# print(s)
# for i in range(n):
#     f += s[i]
# print(f)

# Задача 4: Подсчет количества четных элементов в массиве
# Дан массив чисел. Посчитайте и выведите количество четных элементов в массиве.
# import random
# n = int(input())
# f = 0
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# for i in range(n):
#     if s[i]%2==0:
#         f+=1
# print(f)

# Задача 5: Найти минимальный элемент в массиве
# Дан массив чисел. Найдите и выведите минимальный элемент в массиве.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# min = 100
# print(s)
# for i in range(n):
#     if min>s[i]:
#         min=s[i]
# print(min)

# Задача 6: Найти максимальный элемент в массиве
# Дан массив чисел. Найдите и выведите максимальный элемент в массиве.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# max = 0
# print(s)
# for i in range(n):
#     if max<s[i]:
#         max=s[i]
# print(max)

# Задача 7: Подсчет количества элементов больше заданного числа
# Дан массив чисел и число k. Посчитайте и выведите количество элементов массива, которые больше k.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# k = int(input())
# print(s)
# f = 0
# for i in range(n):
#     if k<s[i]:
#         f+=1
# print(f)

# Задача 8: Умножение всех элементов массива на 2
# Дан массив чисел. Умножьте каждый элемент массива на 2 и выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# b = []
# f = 0
# for i in range(n):
#     f = s[i]*2
#     b.append(f)
# print(b)

# Задача 9: Замена всех отрицательных элементов на нули
# Дан массив чисел. Замените все отрицательные элементы массива на нули и выведите результат.
# import random
# n = int(input())
# s = [random.randint(-100,100) for i in range(n)]
# print(s)
# for i in range(n):
#     if s[i]<0:
#         s[i]=0
# print(s)


# Задача 10: Подсчет количества элементов, равных заданному числу
# Дан массив чисел и число k. Посчитайте и выведите количество элементов массива, равных k.
# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# k = int(input())
# f = 0
# print(s)
# for i in range(n):
#     if s[i]==k:
#         f+=1
# print(f)

# Задача 11: Перестановка первого и последнего элемента массива
# Дан массив чисел. Поменяйте местами первый и последний элемент массива, затем выведите массив.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# b = []
# print(s)
# for i in range(n+1):
#     if i==0:
#         b.append(s[-1])
#     elif i>0 and i<n-1:
#         b.append(s[i])
#     elif i==n:
#         b.append(s[0])
# print(b)
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# max = 0
# min = 100
# f = 0
# k = 0
# for i in range (n):
#     if min > s[i]:
#         min=s[i]
#         f = i
#     if max < s[i]:
#         max=s[i]
#         k = i
# s[f]=max
# s[k]=min
# print(s)

# Задача 12: Сдвиг элементов массива влево на одну позицию
# Дан массив чисел. Сдвиньте все элементы массива влево на одну позицию, а последний элемент поместите на место первого. Выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# f = s[0]
# for i in range(n):
#     if i<n-1:
#         s[i]=s[i+1]
#     if i==n-1:
#         s[i]=f
# print(s)

# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# f = s[n-1]
# print(f)
# for i in range(n-1, -1, -1):
#     if i > 0:
#         s[i]=s[i-1]
# s[0] = f
# print(s)

# Задача 13: Сумма четных и нечетных элементов массива
# Дан массив чисел. Найдите и выведите сумму всех четных и сумму всех нечетных элементов массива.
# import random
# n = int(input())
# s = [random.randint(1,10) for i in range(n)]
# print(s)
# k = 0
# f = 0
# for i in range(n):
#     if s[i]%2==0:
#         k+=s[i]
#     else:
#         f+=s[i]
# print(k,f)

# Задача 14: Поменять местами элементы массива с четными и нечетными индексами
# Дан массив чисел. Поменяйте местами элементы массива с четными и нечетными индексами, затем выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# for i in range(1,n,2):
#     f = s[i-1]
#     s[i-1]=s[i]
#     s[i] = f
# print(s)


# Задача 15: Объединение двух массивов
# Даны два массива чисел одинаковой длины.
# Объедините их в один массив так, чтобы элементы чередовались, и выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# f = [random.randint(1,100) for i in range(n)]
# print(s)
# print(f)
# k = []
# for i in range(n):
#     k.append(s[i])
#     k.append(f[i])
#print(k)

# Задача 1: Поиск второго максимального элемента
# Дан массив чисел. Найдите и выведите второй по величине элемент массива.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# max1 = 0
# max2 = 0
# for i in range(n):
#     if max1<s[i]:
#         max1 = s[i]
# s.remove(max1)
# for j in range(n-1):
#     if max2<s[j]:
#         max2 = s[j]
# print(max1)
# print(max2)

# Задача 3: Сортировка массива пузырьком
# Реализуйте сортировку массива чисел методом пузырька и выведите отсортированный массив.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# for i in range(n):
#     for j in range(n-i-1):
#         if s[j]>s[j+1]:
#             f = s[j]
#             s[j]=s[j+1]
#             s[j+1] = f
# print(s)

# Задача 4: Объединение и сортировка двух массивов
# Даны два отсортированных массива чисел. Объедините их в один отсортированный массив и выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# f = [random.randint(1,100) for i in range(n)]
# g = n*2
# print(s)
# print(f)
# a = s + f
# for i in range(g):
#     for j in range(g-i-1):
#         if a[j]>a[j+1]:
#             b = a[j]
#             a[j]=a[j+1]
#             a[j+1] = b
# print(a)

# Задача 5: Перемешивание элементов массива
# Дан массив чисел. Перемешайте его элементы в случайном порядке и выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,100) for i in range(n)]
# print(s)
# random.shuffle(s)
# print(s)

# import random
# n = int(input())
# s = [i for i in range(n)]
# print(s)
# for i in range(n):
#     g = random.randint(1, n - 1)
#     print(g)
#     f = s[i]
#     s[i]=s[g]
#     s[g] = f
# print(s)

# Задача 6: Удаление всех вхождений элемента из массива
# Дан массив чисел и число k. Удалите из массива все вхождения числа k и выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# k = int(input())
# f = s.count(k)
# l = 0
# while f!=l:
#     s.remove(k)
#     l+=1
# print(s)

# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# k = int(input())
# f = s.count(k)
# for i in range(f):
#     s.remove(k)
# print(s)

# Задача 7: Нахождение всех пар с заданной суммой
# Дан массив чисел и число k. Найдите все пары элементов массива, сумма которых равна k.
# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# k = int(input())
# for i in range(n):
#     for j in range(i+1,n):
#         if s[i]+s[j]==k :
#             print(s[i],s[j])

# Задача 8: Подсчет частоты элементов
# Дан массив чисел. Подсчитайте и выведите, сколько раз каждый элемент встречается в массиве.
# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# h = []
# for i in range(n):
#     for j in range(i+1,n+1):
#         k = s[i]
#         f = s.count(k)
#         if h.count(k)>0:
#             continue
#         h.append(k)
#         print(f'{k} - {f}')

# Задача 9: Проверка на палиндром
# Дан массив чисел. Проверьте, является ли массив палиндромом (читается одинаково слева направо и справа налево).
# import random
# n = int(input())
# s = [random.randint(1,3) for i in range(n)]
# print(s)
# f = 0
# for i in range(n):
#     if s[i]==s[-i-1]:
#         f+=1
# if f==n:
#     print("Yes")
# else:
#     print("No")

# Задача 10: Удаление дубликатов из массива
# Дан массив чисел. Удалите из него все дубликаты, оставив только уникальные элементы, и выведите результат.
# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# h = []
# for i in range(n):
#      for j in range(i+1,n+1):
#         k = s[i]
#         f = s.count(k)
#         if h.count(k)>0:
#             continue
#         h.append(k)
# print(h)

# Задача 11: Разделение массива на положительные и отрицательные числа
# Дан массив чисел. Разделите его на два массива: один с положительными числами, другой с отрицательными. Выведите оба массива.
# import random
# n = int(input())
# s = [random.randint(-5,5) for i in range(n)]
# print(s)
# f = []
# k = []
# for i in range(n):
#     if s[i]>=0:
#         f.append(s[i])
#     else:
#         k.append(s[i])
# print(f)
# print(k)


# Задача 15: Обратная сортировка массива
# Дан массив чисел. Отсортируйте его в порядке убывания и выведите результат.

# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# for i in range(n):
#     for j in range(n-1-i):
#         if s[j]<s[j+1]:
#             f = s[j]
#             s[j] = s[j+1]
#             s[j+1] = f
# print(s)

# Задача 1: Поиск всех уникальных тройек с заданной суммой
# Дан массив чисел и число k. Найдите все уникальные тройки элементов массива, сумма которых равна k.
# import random
# n = int(input())
# s = [random.randint(1,5) for i in range(n)]
# print(s)
# k = int(input())
# for i in range(n-1):
#     for j in range(1+i,n):
#         for f in range(1+j,n):
#             if s[i]+s[j]+s[f]==k:
#                 print(s[i],s[j],s[f])

# Задача 3: Упаковка массива с подсчетом
# Дан массив чисел, состоящий из повторяющихся элементов. Преобразуйте его в массив, в котором элементы упакованы вместе с их количеством (например, [1,1,1,2,2,3] -> [(1,3),(2,2),(3,1)]).
import random
n = int(input())
s = [random.randint(1,5) for i in range(n)]
print(s)
h = []
for i in range(n):
    for j in range(i+1,n+1):
        k = s[i]
        f = s.count(k)
        if h.count(k)>0:
            continue
        h.append(k)
        print(f'[({f},{k})]', end=" ")

# Задача 4: Найти элемент, который встречается более чем n/2 раз
# Дан массив из n элементов. Найдите элемент, который встречается более чем n/2 раз (элемент большинства).

# Задача 5: Разделение массива на группы с равными суммами
# Дан массив чисел. Определите, можно ли разделить его на две группы с одинаковой суммой элементов.

# Задача 6: Максимальная длина подмассива с заданной суммой
# Дан массив чисел и число k. Найдите максимальную длину подмассива, сумма элементов которого равна k.

# Задача 7: Поиск недостающего числа в последовательности
# Дан массив чисел от 1 до n с одним отсутствующим числом. Найдите недостающее число.

# Задача 8: Подсчет количества инверсий в массиве
# Дан массив чисел. Подсчитайте количество инверсий в массиве (пары элементов, где предыдущий элемент больше последующего).

# Задача 9: Нахождение максимального произведения подмассива
# Дан массив чисел. Найдите подмассив с максимальным произведением элементов.

# Задача 10: Обратный массив по парам
# Дан массив чисел. Разбейте его на пары и поменяйте каждую пару местами (например, [1,2,3,4] -> [2,1,4,3]).

# Задача 11: Объединение массивов с удалением дубликатов
# Даны два массива чисел. Объедините их в один массив, удалив все дубликаты, и выведите результат.

# Задача 12: Подсчет всех возможных подмассивов
# Дан массив чисел. Подсчитайте количество всех возможных подмассивов.

# Задача 13: Поиск первого неповторяющегося элемента
# Дан массив чисел. Найдите и выведите первый элемент, который не повторяется.

# Задача 14: Перестановка массива для максимальной суммы
# Дан массив чисел. Переставьте его элементы так, чтобы сумма разностей между соседними элементами была максимальной.

# Задача 15: Перемещение всех нулей в конец массива
# Дан массив чисел. Переместите все нули в конец массива, сохранив порядок остальных элементов.

# Задача 16: Подсчет чисел, больших чем все элементы справа
# Дан массив чисел. Подсчитайте количество элементов, которые больше всех элементов, находящихся справа от них.

# Задача 17: Подсчет всех возможных комбинаций элементов
# Дан массив чисел. Подсчитайте количество всех возможных комбинаций элементов, где порядок не имеет значения.

# Задача 18: Проверка, можно ли массив сделать палиндромом
# Дан массив чисел. Определите, можно ли его элементы переставить так, чтобы получился палиндром.

# Задача 19: Преобразование массива в "зигзагообразный" порядок
# Дан массив чисел. Переставьте его элементы так, чтобы они чередовались между возрастанием и убыванием (например, [1,3,2,5,4] -> [1,3,2,5,4]).

# Задача 20: Минимальная длина подмассива с суммой >= k
# Дан массив чисел и число k. Найдите минимальную длину подмассива, сумма элементов которого больше или равна k.
