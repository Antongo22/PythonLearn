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

# with open("Test1.txt","r", encoding='utf8') as f:  encoding='utf8' - чтобы читал русский


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
        
        
        
# Файлы

# Чтение и вывод содержимого файла:
# Напишите программу, которая открывает текстовый файл, читает его содержимое и выводит его на экран.
#
# Подсказка: Используйте режим "r" для открытия файла и метод read() для чтения всего содержимого.
# Дополнительное задание: Сделайте так, чтобы файл закрывался автоматически после завершения работы с ним.
# with open("Test.txt","r") as f:
#     s = f.read()
#     print(s)

# Запись строки в файл:
# Напишите программу, которая запрашивает у пользователя строку и записывает ее в текстовый файл. Если файл уже существует, его содержимое должно быть удалено.
#
# Подсказка: Используйте режим "w" для записи в файл.
# n = input()
# with open("Test.txt","w") as f:
#     f.write(n)

# Добавление текста в файл:
# Напишите программу, которая запрашивает у пользователя строку и добавляет эту строку в конец текстового файла, не удаляя его предыдущего содержимого.
#
# Подсказка: Используйте режим "a" для добавления текста в файл.
# with open("Test.txt","a") as f:
#     f.write("test")

# Подсчет строк в файле:
# Напишите программу, которая открывает текстовый файл и подсчитывает количество строк в нем.
#
# Подсказка: Используйте цикл для построчного чтения файла, и переменную-счетчик для подсчета строк.
# s = 0
# with open("Test.txt","r+") as f:
#     for i in f:
#         s+=1
# print(s)

# Копирование содержимого одного файла в другой:
# Напишите программу, которая читает содержимое одного текстового файла и записывает его в другой файл.
#
# Подсказка: Откройте первый файл в режиме чтения ("r"), прочитайте его содержимое,
# затем откройте второй файл в режиме записи ("w") и запишите содержимое в него.
with open("Test.txt","r") as f:
    s = f.read()
with open("Test1.txt","w") as f:
    f.write(s)
