# Раньше можно было писать непонятные переменные, состоящие из одной буквы и тп, но, с этого момента так больше нельзя!
# Твой код становится большим, и, в нём легко запутатся как тебе, так и другому человеку, а чаще всего в реальной работе ты работаешь не один.
# Так что работа над тем, что твой код был красывый и понятный - это необходимость, без этого хорошим программистом не стать.

# С чего же начать? Начнём чуть ли не с самого важного - переменные, а именно их названия. Тут без английского никак.
# Теперь, название переменной должно чётко описывать то, зачем она существует.
# Сюда же добавим и названия функций и классов (о них мы поговорим чуть позже, но краткая информация будет сейчас).

# Названия переменных и функций принято писать со сточной буквы, разделяя слова нижним подчёркиванием (все буквы строчные).
# Названия же классов нужно писать с большой буквы.

# Теперь поговорим про функции. Ты их уже отлично знаешь, так вот, по хорошему весь код помещать в функции, и запускат его через вызов в главной функии.
# Вот БАЗА написания кода:
def foo():
    print("some code")

def main():
    # Тут мы вызываем другие функции и тп
    foo()
    print("Hello, World!")


if __name__ == "__main__":
    main()

# Благодаря этой конструкции можно легко определить, где программа стартует. А так же это просто удобно.
# Подробнее про это можно почитать тут - https://stackoverflow.com/questions/419163/what-does-if-name-main-do

# Соответсвенно, главный файл принято называть "main.py". Так же очень важно распределять файлы по папкам в логическом порядке.


# Подведя итоги, можно сказать что обязанность каждого программиста писат чистый и понтянтый код, используя для этого понятные переменные, функции и классы,
# а так же не забывать всё сортировать по папкам и файлам, чтобы код было легче воспринимать.

# Отныне - ты пишешь чистый код, другой не приму.


# Чистый код
# Задачи - переписать игру в крестики-нолики используя функции

# Финальное задание
# Написать игру - виселица. Данные о словах и описаниях, а так же рисунки виселицы должны быть внесены в отдельный файл, как и компоненты кода.

