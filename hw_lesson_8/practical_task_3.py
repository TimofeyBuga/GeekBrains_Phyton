# 3. Создайте собственный класс-исключение,
# который должен проверять содержимое списка на наличие только чисел.
# Проверить работу исключения на реальном примере.
# Необходимо запрашивать у пользователя данные и заполнять список.
# Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована.
# Элементы запрашиваются бесконечно, пока пользователь сам не остановит работу скрипта,
# введя, например, команду “stop”. При этом скрипт завершается,
# сформированный список выводится на экран.


class ThisError(Exception):
    def __init__(self):
        pass


class TypeCheck:
    def __init__(self):
        self.my_list = []

    def check_value(self):
        global user_val
        while True:
            try:
                try:
                    user_val = int(input("Enter numbers: "))
                    ex = input(f"{user_val} now on the list.\n Next number: press 'ENTER'"
                               f"\n Stop program: enter 'stop'\n").lower()
                    self.my_list.append(user_val)
                    if ex == "stop":
                        print(self.my_list)
                        break
                except ValueError:
                    raise ThisError
            except ThisError:
                ex = input(f"This is not numbers!\n Next number: press 'ENTER'"
                           f"\n Stop program: enter 'stop'\n").lower()
                if ex == "stop":
                    print(self.my_list)
                    break
                else:
                    self.check_value()


a = TypeCheck()
a.check_value()