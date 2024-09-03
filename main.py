import random

a = 3
a1 = 3
s = []
f = 0
b = 0
b1 = 0
l = 0
p = 0
while True:
    try:
        n = int(input("Введите количество игроков: "))
        if n==1 or n==2:
            break
        else:
            print("Введите количество игроков заново")
    except ValueError:
        print("Ошибка: Введено не число!")
for i in range(a):
    s.append(['-'] * a1)
    for j in range(a):
        s[i][j] = '-'
for i in range(len(s)):
    for j in range(len((s[i]))):
        print(f'{s[i][j]} ', end='')
    print()
if n == 2:
    while True:
        while True:
            try:
                n, k = map(int, input("Введите значение сначала по оси у, а потом по оси х(0,1,2): ").split())
                if n == 0 or n == 1 or n == 2:
                    if k == 0 or k == 1 or k == 2:
                        if s[n][k] != 0 and s[n][k] != "x":
                            break
                        else:
                            print("Введите значение заново")
                    else:
                        print("Введите значение заново")
                else:
                    print("Введите значение заново")
            except ValueError:
                print("Ошибка: Введено не число!")
        f += 1
        if f % 2 == 0:
            s[n][k] = "x"
        else:
            s[n][k] = 0
        for i in s:
            for j in i:
                print(j, end=" ")
            print()
        p += 1
        if (s[0][0] == 0 and s[1][1] == 0 and s[2][2] == 0) or (s[2][0] == 0 and s[1][1] == 0 and s[0][2] == 0):
            print("Победил 1 игрок!")
            l = 1
            break
        elif (s[0][0] == "x" and s[1][1] == "x" and s[2][2] == "x") or (
                s[2][0] == "x" and s[1][1] == "x" and s[0][2] == "x"):
            print("Победил 2 игрок!")
            l = 1
            break
        for b in range(a):
            if s[b][0] == 0 and s[b][1] == 0 and s[b][2] == 0:
                print("Победил 1 игрок!")
                l = 1
                break
            elif s[b][0] == "x" and s[b][1] == "x" and s[b][2] == "x":
                print("Победил 2 игрок!")
                l = 1
                break
        for b1 in range(a1):
            if s[0][b1] == 0 and s[1][b1] == 0 and s[2][b1] == 0:
                l = 1
                print("Победил 1 игрок!")
                break
            elif s[0][b1] == "x" and s[1][b1] == "x" and s[2][b1] == "x":
                l = 1
                print("Победил 2 игрок!")
                break
        if l == 1:
            break
        if p == 9:
            print("Ничья!")
            break
if n == 1:
    while True:
        while True:
            try:
                n, k = map(int, input("Введите значение сначала по оси у, а потом по оси х(0,1,2): ").split())
                if n == 0 or n == 1 or n == 2:
                    if k == 0 or k == 1 or k == 2:
                        if s[n][k] != 0 and s[n][k] != "x":
                            break
                        else:
                            print("Введите значение заново")
                    else:
                        print("Введите значение заново")
                else:
                    print("Введите значение заново")
            except ValueError:
                print("Ошибка: Введено не число!")
        s[n][k] = 0
        while True:
            t = random.randint(0, 2)
            t1 = random.randint(0, 2)
            if s[t][t1] != 0 and s[t][t1] != "x":
                break
        s[t][t1] = "x"
        for i in s:
            for j in i:
                print(j, end=" ")
            print()
        if (s[0][0] == 0 and s[1][1] == 0 and s[2][2] == 0) or (s[2][0] == 0 and s[1][1] == 0 and s[0][2] == 0):
            print("Победил 1 игрок!")
            l = 1
            break
        elif (s[0][0] == "x" and s[1][1] == "x" and s[2][2] == "x") or (s[2][0] == "x" and s[1][1] == "x" and s[0][2] == "x"):
            print("Бот")
            l = 1
            break
        for b in range(a):
            if s[b][0] == 0 and s[b][1] == 0 and s[b][2] == 0:
                print("Победил игрок!")
                l = 1
                break
            elif s[b][0] == "x" and s[b][1] == "x" and s[b][2] == "x":
                print("Бот")
                l = 1
                break
        for b1 in range(a1):
            if s[0][b1] == 0 and s[1][b1] == 0 and s[2][b1] == 0:
                l = 1
                print("Победил игрок!")
                break
            elif s[0][b1] == "x" and s[1][b1] == "x" and s[2][b1] == "x":
                l = 1
                print("Бот!")
                break
        if l == 1:
            break
        if p == 9:
            print("Ничья!")
            break
        elif s[t][t1]==0 or s[t][t1]=="x":
            continue