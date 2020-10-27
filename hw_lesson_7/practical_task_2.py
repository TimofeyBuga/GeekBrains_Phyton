# 2) Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь определенное название.
# К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост (для костюма).
# Это могут быть обычные числа: V и H, соответственно.
#
# Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5),
# для костюма (2*H + 0.3). Проверить работу этих методов на реальных данных.
#
# Реализовать общий подсчет расхода ткани.
# Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта,
# проверить на практике работу декоратора @property.

from abc import ABC, abstractmethod


class Fabric(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_yardage_c(self):
        return self.width / 6.5 + 0.5

    def get_yardage_j(self):
        return self.height * 2 + 0.3

    @property
    def get_yardage_full(self):
        return str(f"Amount of fabric: \n{(self.width / 6.5 + 0.5) + (self.height * 2 + 0.3)}")

    @abstractmethod
    def abstract(self):
        return "Smth vary abstract"


class Coat(Fabric):

    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.width / 6.5 + 0.5)

    def __str__(self):
        return f"Dimension coat:\n{self.square_c}"

    def abstract(self):
        return "Abstract"


class Costume(Fabric):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.height * 2 + 0.3)

    def __str__(self):
        return f"Dimension jacket:\n{self.square_j}"

    def abstract(self):
        pass


coat = Coat(18, 8)
costume = Costume(4, 10)

print(f"{coat}\n"
      f"{coat.get_yardage_full}\n"
      f"{coat.get_yardage_c()}\n"
      f"{coat.abstract()}")

print(f"{costume}\n"
      f"{costume.get_yardage_full}\n"
      f"{costume.get_yardage_j()}")

