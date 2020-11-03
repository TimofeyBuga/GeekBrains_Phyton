# 2. Создайте собственный класс-исключение,
# обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class NotZero(Exception):
    def __init__(self, txt):
        self.txt = txt


def division():
    try:
        div_1 = int(input("Enter number dividend: "))
        div_2 = int(input("Enter number divider: "))
        if div_2 == 0:
            raise NotZero("Cannot be divided by zero!")
        else:
            res = div_1 / div_2
            return res
    except ValueError:
        return "Entered not a number!"
    except NotZero as err:
        return err


print(division())