# Регулярное выражение – это последовательность символов, используемая для поиска и замены текста в строке или файле.

# Для выполнения операций сопоставления с шаблонами регулярных выражений и замены фрагментов строк используется модуль re.
# Модуль поддерживает операции как со строками Юникода, так и со строками байтов.

# Шаблоны регулярных выражений определяются как строки, состоящие из смеси текста и последовательностей специальных символов.
# В шаблонах часто используются специальные символы и символ обратного слэша, поэтому они обычно оформляются, как «сырые» строки, такие как

some_text = r'здесь регулярное выражение'

# Синтаксис шаблонов
# Ниже приводится список основных последовательностей специальных символов, которые используются в шаблонах регулярных выражений:

# .
# Соответствует любому символу, кроме символа перевода строки.
#
# ^
# Соответствует позиции начала строки.
#
# $
# Соответствует позиции конца строки.
#
# *
# Ноль или более повторений предшествующего выражения.
#
# +
# Одно или более повторений предшествующего выражения.
#
# ?
# Ноль или одно повторение предшествующего выражения.
#
# {m}
# Соответствует точно m повторениям предшествующего выражения.
#
# {m, n}
# Соответствует от m до n повторений предшествующего выражения.
#
# {m,}
# От m до бесконечности.
#
# [...]
# Соответствует любому символу, присутствующему в множестве, таком как [abcdef]или [a-zA-z]. Специальные символы, такие как *, утрачивают свое специальное значение внутри множества.
#
# [^...]
# Соответствует любому символу, не присутствующему в множестве, таком как [^0-9].
#
# A|B
# Соответствует либо A, либо B, где A и B являются регулярными выражениями.
#
# (...)
# Подстрока, соответствующая регулярному выражению в круглых скобках, интерпретируется как группа и сохраняется.
# Содержимое группы может быть получено с помо-щью метода group() объектов класса MatchObject,
# которые возвращаются операцией поиска совпадений.
# Стандартные экранированные последовательности, такие как "\n" и "\t", точно так же интерпретируются и в регулярных выражениях
# (например, выражению r"\n+" будет соответствовать один или более символов перевода строки).
# Кроме того, литералы символов, которые в регулярных выражениях имеют специальное значение, можно указывать,
# предваряя их символом обратного слэша. Например, выражению r"\*" соответствует символ *.
# Дополнительно ряд экранированных последовательностей, начинающихся символом обратного слэша, соответствуют специальным символам:

# \число
# Соответствует фрагменту текста, совпавшему с группой с указанным номером. Группы нумеруются от 1 до 99, слева направо.
#
# \A
# Соответствует только началу строки.
# \b
# Соответствует пустой строке в позиции начала или конца слова. Под словом подразумевается последовательность алфавитно-цифровых символов, завершающаяся пробельным или любым другим не алфавитно-цифровым символом.
#
# \B
# Соответствует пустой строке не в позиции начала или конца слова.
#
# \d
# Соответствует любой десятичной цифре. То же, что и выражение [0-9].
#
# \D
# Соответствует любому нецифровому символу. То же, что и выражение [^0-9].
#
# \s
# Соответствует любому пробельному символу. То же, что и выражение [\t\n\r\f\v ].
#
# \S
# Соответствует любому не пробельному символу. То же, что и выражение [^\t\n\r\f\v ].
#
# \w
# Соответствует любому алфавитно-цифровому символу.
#
# \W
# Соответствует любому символу, не относящемуся к множеству \w.
#
# \Z
# Соответствует только концу строки.
#
# \
# Соответствует самому символу обратного слэша.


# Специальные символы \d, \D, \s, \S, \w и \W интерпретируются иначе при сопоставлении со строками Юникода.
# В данном случае они совпадают со всеми символами Юникода, соответствующими описанным свойствам.
# Например, \d совпадает со всеми символами Юникода, которые классифицируются как цифры, будь то европейские,
# арабские или индийские цифры, каждые из которых занимают различные диапазоны символов Юникода.


# Флаги

# A или ASCII
# Сопоставление выполняется только с 8-битными символами ASCII.
#
# I или IGNORECASE
# Сопоставление выполняется без учета регистра символов.
#
# L или LOCALE
# При сопоставлении со специальными символами \w, \W, \b и \B используются региональные настройки.
#
# M или MULTILINE
# Обеспечивает совпадение символов ^ и $ с началом и концом каждой строки в тексте, помимо начала и конца самого текста. (Обычно символы ^ и $ совпадают только с началом и концом всего текста.)
#
# S или DOTALL
# Обеспечивает совпадение символа точки (.) со всеми символами, включая символ перевода строки.
#
# X или VERBOSE
# Игнорирует неэкранированные пробельные символы и комментарии в строке шаблона.




# Методы модуля re
# re.findall(pattern, string, flags=0)
# Возвращает список всех неперекрывающихся совпадений с шаблоном pattern в строке string, включая пустые совпадения.
# Если шаблон имеет группы, возвращает список фрагментов текста, совпавших с группами.
# Если в шаблоне присутствует более одной группы, каждый элемент в списке будет представлен кортежем, содержащим текст из каждой группы.


# re.match(pattern, string, flags=0)
# Проверяет наличие совпадения с шаблоном pattern в строке string.
# В случае успеха возвращает объект типа MatchObject, в противном случае возвращается None.


# re.search(pattern, string, flags=0)
# Отыскивает в строке string первое совпадение с шаблоном pattern.
# В случае успеха возвращает объект типа MatchObject; если совпадений не найдено, возвращается None.

# re.split(pattern, string, maxsplit=0, flags=0)
#Разбивает строку string по совпадениям с шаблоном pattern.
# Возвращает список строк, включая текст, совпавший с группами, присутствующими в шаблоне.
# В аргументе maxsplit передается максимальное количество выполняемых разбиений.
# По умолчанию выполняются все возможные разбиения.

# re.subn(pattern, repl, string, count=0, flag=0)
# Замещает текстом repl самые первые неперекрывающиеся совпадения с шаблоном pattern в строке string.
# В аргументе repl допускается использовать обратные ссылки на группы в шаблоне, такие как \6.
# Аргумент count определяет максимальное количество подстановок. По умолчанию замещаются все найденные совпадения.
# Возвращает кортеж, содержащий новую строку и количество выполненных подстановок.

# re.sub(pattern, repl, string, count=0, flag=0)
# Тоже, что и re.subn, но возвращает изменённую строку.


# re.compile(pattern, flags=0)
# Компилирует регулярное выражение для дальнейшего использования с методами данного регулярного выражения.


# Объекты MatchObject
# Экземпляры класса MatchObject возвращаются методами re.search() и re.match() и содержат информацию о группах,
# а также о позициях найденных совпадений. Экземпляр mo класса MatchObject обладает следующими методами и атрибутами:

# mo.expand(template)
# Возвращает строку, полученную заменой совпавших фрагментов экранированными последовательностями в строке template.
# Обратные ссылки, такие как \1 и \2, замещаются содержимым соответствующих групп.
# Обратите внимание, что эти последовательности должны быть оформлены как «сырые» строки
# или с дополнительным символом обратного слэша, например: r'\1' или '\\1'

# mo.group([group1, group2, ...])
# Возвращает одну или более подгрупп в совпадении. Аргументы определяют номера групп или их имена.
# Если имя группы не задано, возвращается совпадение целиком.
# Если указана только одна группа, возвращается строка, содержащая текст, совпавший с группой.
# В противном случае возвращается кортеж, содержащий совпадения со всеми указанными группами.
# Если было запрошено содержимое группы с недопустимым именем или номером, возбуждает исключение IndexError

# mo.groups([default])
# Возвращает кортеж, содержащий совпадения со всеми группами в шаблоне.
# В аргументе default указывается значение, возвращаемое для групп,
# не участвовавших в совпадении (по умолчанию имеет значение None)

# mo.groupdict([default])
# Возвращает словарь, содержащий совпадения с именованными группами.
# В аргументе default указывается значение, возвращаемое для групп,
# не участвовавших в сопоставлении (по умолчанию имеет значение None).

# mo.start([group])
# mo.end([group])
#Эти два метода возвращают индексы начала и конца совпадения с группой в строке.
# Если аргумент group опущен, возвращаются позиции всего совпадения.
# Если группа существует, но не участвовала в сопоставлении, возвращается None

# mo.span([group])
# Возвращает кортеж из двух элементов (m.start(group), m.end(group)) .
# Если совпадений с группой group не было обнаружено, возвращается кортеж (None, None).
# Если аргумент group опущен, возвращаются позиции начала и конца всего совпадения.

# mo.pos
# Значение аргумента pos, переданное методу re.search или re.match

# mo.endpos
# Значение аргумента endpos, переданное методу re.search или re.match

# mo.lastindex
# Числовой индекс последней совпавшей группы. Если ни одна группа не совпала или в шаблоне нет ни одной группы,
# возвращается None или в шаблоне нет ни одной группы.

# mo.re
# Объект регулярного выражения, чьим методом re.match или re.search был создан данный экземпляр класса MatchObject

# mo.string
# Строка, переданная методу re.match или re.search



# Пример
import re
text = "John will be out of the office from 12/15/2012 - 1/3/2013."

# Шаблон регулярного выражения для поиска дат
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')

# Найти и вывести все даты
for m in datepat.finditer(text):
    print(m.group())

# Отыскать все даты и вывести их в другом формате
monthnames = [None,'Jan','Feb','Mar','Apr','May','Jun',
                'Jul','Aug','Sep','Oct','Nov','Dec']
for m in datepat.finditer(text):
    s = f'{monthnames[int(m.group(1))]}, {m.group(2)}, {m.group(3)}'
    print(s)

# Заменить все даты их значениями в европейском формате (день/месяц/год)
def fix_date(m):
    return f"{m.group(2)}/{m.group(1)}/{m.group(3)}"
newtext = datepat.subn(fix_date, text)
print(newtext)
# Альтернативный способ замены
newtext = datepat.subn(r'\2/\1/\3', text)


# Задачи на регулярные выражения

# 1. Найти все email-адреса в тексте.
# Написать регулярное выражение для поиска всех email-адресов в тексте.
# Пример: "Контакты: example@mail.com, test.user@example.co.uk"
# Ожидаемый результат: ['example@mail.com', 'test.user@example.co.uk']

# 2. Проверить, является ли строка допустимым номером телефона.
# Создать регулярное выражение для проверки номера телефона в формате "(XXX) XXX-XXXX".
# Пример: "(123) 456-7890" или "(987) 654-3210" - допустимые номера.
# Ожидаемый результат: True

# 3. Найти все слова, начинающиеся с заглавной буквы.
# Написать регулярное выражение для поиска всех слов, начинающихся с заглавной буквы.
# Пример: "Today is a Beautiful day in the City."
# Ожидаемый результат: ['Today', 'Beautiful', 'City']

# 4. Проверить, что строка является допустимым IP-адресом.
# Создать регулярное выражение для проверки, что строка является IP-адресом в формате "XXX.XXX.XXX.XXX".
# Пример: "192.168.1.1" или "255.255.255.0" - допустимые IP-адреса.
# Ожидаемый результат: True

# 5. Найти все слова длиной от 5 до 8 символов.
# Написать регулярное выражение для поиска всех слов в тексте, длина которых от 5 до 8 символов.
# Пример: "The quick brown fox jumps over the lazy dog."
# Ожидаемый результат: ['quick', 'brown', 'jumps']

# 6. Заменить все цифры в строке на символ '#'.
# Создать регулярное выражение для замены всех цифр в строке на символ '#'.
# Пример: "User123 has password 4567."
# Ожидаемый результат: "User### has password ####."

# 7. Найти все HTML-теги в строке.
# Написать регулярное выражение для поиска всех HTML-тегов в строке.
# Пример: "<div><p>Hello World!</p></div>"
# Ожидаемый результат: ['<div>', '<p>', '</p>', '</div>']

# 8. Проверить, что строка является допустимым URL.
# Создать регулярное выражение для проверки, что строка является допустимым URL.
# Пример: "https://www.example.com" или "http://example.org" - допустимые URL.
# Ожидаемый результат: True

# 9. Найти все слова, содержащие хотя бы одну цифру.
# Написать регулярное выражение для поиска всех слов в строке, содержащих хотя бы одну цифру.
# Пример: "My password is secure123 and my code is abc4567."
# Ожидаемый результат: ['secure123', 'abc4567']

# 10. Найти все строки, представляющие даты в формате "YYYY-MM-DD".
# Создать регулярное выражение для поиска всех дат в формате "YYYY-MM-DD".
# Пример: "Important dates: 2021-08-15, 2022-01-01, 2023-12-31."
# Ожидаемый результат: ['2021-08-15', '2022-01-01', '2023-12-31']
