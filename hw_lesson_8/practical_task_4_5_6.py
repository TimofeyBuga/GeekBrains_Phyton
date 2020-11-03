# 4. Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
#
# 5. Продолжить работу над первым заданием.
# Разработать методы, отвечающие за приём оргтехники на склад и передачу в определенное подразделение компании.
# Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.
#
# 6. Продолжить работу над вторым заданием.
# Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад,
# нельзя использовать строковый тип данных.


class EquipmentWarehouse:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.items = {"Model": self.name, "Unit price": self.price, "Quantity": self.quantity}

    def income(self):
        try:
            name = input(f"Enter name model: ")
            price = int(input(f"Enter unit price: "))
            quantity = int(input(f"Enter quantity: "))
            item = {"Model": name, "Unit price": price, "Quantity": quantity}
            self.items.update(item)
            print(self.items)
        except ValueError:
            print("Value error!")


class Printer(EquipmentWarehouse):
    pass


class Scanner(EquipmentWarehouse):
    pass


class Xerox(EquipmentWarehouse):
    pass


p = Printer('Hp', 2, 300)
s = Scanner('Canon', 54000, 10)
x = Xerox('Xerox', 7000, 15)
p.income()
s.income()
x.income()
