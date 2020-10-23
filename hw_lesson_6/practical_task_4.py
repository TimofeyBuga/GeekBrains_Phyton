# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
# остановилась, повернула (куда). Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f"{self.name} went."

    def stop(self):
        return f'{self.name} has stopped.'

    def turn(self, direction):
        return f'{self.name} turned {direction},'

    def show_speed(self):
        return f'Your speed is {self.speed},'


class TownCar(Car):

    def show_speed(self):
        if self.speed > 60:
            return f"Your speed is higher than allow! Your speed is {self.speed},"
        else:
            return f"Speed of {self.name} is normal. Your speed is {self.speed},"


class SportCar(Car):

    def police_doc(self):
        if self.is_police:
            return f"{self.name} is from Brooklyn police department."
        else:
            return f"{self.name} is not from Brooklyn police department."


class WorkCar(Car):

    def show_speed(self):
        if self.speed > 40:
            return f"Your speed is higher than allow! Your speed is {self.speed},"
        else:
            return f"Speed of {self.name} is normal. Your speed is {self.speed},"


class PoliceCar(Car):

    def police_doc(self):
        if self.is_police:
            return f"{self.name} is from Brooklyn police department."
        else:
            return f"{self.name} is not from Brooklyn police department."


town = TownCar("Dodge", 80, "Black", False)
print("\nTownCar: " + town.go(), town.show_speed(), town.turn("right"), town.stop())

sport = SportCar("Zonda", 240, "Gray", False)
print("\nSportCar: " + sport.go(), sport.show_speed(), sport.turn("right"), sport.stop(), sport.police_doc())

work = WorkCar("Mercedes-Benz", 40, "Green", False)
print("\nWorkCar: " + work.go(), work.show_speed(), work.turn("left"), work.stop())

police = PoliceCar("Porsche", 130, "Black-White", True)
print("\nPoliceCar: " + police.go(), police.show_speed(), police.turn("left"), police.stop(), police.police_doc())