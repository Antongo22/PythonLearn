# Урок 2. Усовные операторы

# if (условие) :
# действие
# else:
# действие

# if (условие) :
# действие
# elif (условие) :
# действие
# else:
# действие


# if (условие) :
# действие
# if (условие) :
# действие
# if (условие) :
# действие
# else:
# действие

# ______
# if (условие) :
# действие
# else:
# if (условие) :
# действие
# else:
# действие

# Одиновково

# if (условие) :
# действие
# elif (условие) :
# действие
# else:
# действие

# _____


# Пользователь вводит возраст, если больше или равно 18, то пропускаем, иначе нет
# Пользователь вводит число, если оно чётное, то пропускаем, иначе нет
# Пользователь вводит число, если оно кратно 5, проверяем на кратность 3, если нет, то пропускаем
# Пользователь вводит число, если чётно, то пропускаем, иначе проверяем на кратность 3
#1
# a = int(input())
# if a>=18:
#     print("Проходи")
# else:
#     print("Уходи")
# #2
# if a%2==0:
#     print("Четное")
# else:
#     print("Нечетное")
# #3
# if a%5==0 and a%3==0:
#     print("Проверка пройдена")
# else:
#     print("Проверка не пройдена")
# #4
# if a%2==0:
#     print("Четно")
# elif a%3==0:
#     print("Кратно 3")
# else:
#     print("Уходи")
# # Дано число. Если оно от -10 до 10 не включительно, то увеличить его на 5, иначе уменьшить на 10.
# # Пользователь вводит три числа. Если все числа больше 10 и первые два числа делятся на 3, то вывести yes, иначе no
# # Дано четыре числа, если первые два числа больше 5, третье число делится на 6, четвертое число не делится на 3, то вывести yes, иначе no.
# #5
# if a<10 and a>-10:
#     a+=5
# else:
#     a-=10
# print(a)
# #6
# b = int(input())
# c = int(input())
# if a>10 and b>10 and c>10 and a%3==0 and b%3==0:
#     print("yes")
# else:
#     print("no")
# #7
# d = int(input())
# if a>5 and b>5 and c%6==0 and d%3!=0:
#     print("yes")
# else:
#     print("no")
# # Дано три числа. Найти количество положительных чисел среди них.
# # Дана дата из трех чисел (день, месяц и год). Вывести yes, если такая дата существует (например, 12 02 1999 - yes, 22 13 2001 - no). Считать, что в феврале всегда 28 дней.
# # Дано трехзначное число. Переставьте первую и последнюю цифры.
# # Дано четырехзначное число. Определите, есть ли одинаковые цифры в нем.
# #8
# s = 0
# if a>0:
#     s+=1
# if b>0:
#     s+=1
# if c>0:
#     s+=1
# print(s)
#9
a = int(input())
b = int(input())
c = int(input())
if b<=7 and b%2!=0 and b>0 and c>=0 and a<=31:
    print("yes")
elif b<=7 and b%2==0 and b>0 and c>=0 and a<=30 and b!=2:
    print("yes")
elif b==2 and a==28 and c>=0:
    print("yes")
elif b>7 and b<=12 and b%2==0 and c>=0 and b>0 and a<=31:
    print("yes")
elif b>7 and b<=12 and b%2!=0 and c>=0 and b>0 and a<=30:
    print("yes")
else:
    print("no")

if b < 1 or b > 12:
    print("no")
else:
    max_day = 28

    if b == 2:
        max_day = 28
    elif b==4 or b==6 or b==9 or b==11:
        max_day = 30
    else:
        max_day = 31

    if a>0 and a<=max_day:
        print("yes")
    else:
        print("no")


#10
f = int(input())
k = f%10
n = f//100
m = f//10%10
e = k*100+m*10+n
print(e)
#11
g = int(input())
g1 = g//1000
g2 = g//100%10
g3 = g//10%10
g4 = g%10
if g1==g2 or g1==g3 or g1==g4 or g2==g3 or g2==g4 or g3==g4:
    print("yes")
else:
    print("no")
#Дано четырехзначное число. Поменяйте местами наименьшую и наибольшую цифры.
# Даны действительные положительные числа a, b, с. По трем сторонам с длинами а, Ь, с можно построить треугольник. Найти углы треугольника.
# Пользователь вводит целое число. Проверьте является ли это число четырехзначным, если является, то выведите строку "Успешно", иначе "Неудача".
#Итоговое задание - написать свой калькулятор
#14
h = int(input())
if h>=1000 and h<=9999:
    print("Успешно")
else:
    print("Неудача")
#15
l = input()
q = int(input())
w = int(input())
if l=="Сложение":
    print(q+w)
elif l=="Вычитание":
    print(q-w)
elif l=="Деление":
    print(q//w)
elif l=="Умножение":
    print(q*w)
elif l=="Возведение в степень":
    print(q**w)
else:
    print("Я вас не понимать")


