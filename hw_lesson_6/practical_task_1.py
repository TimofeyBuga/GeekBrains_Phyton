# 1. Создать класс TrafficLight (светофор)
# и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый)
# — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
#


from time import sleep


class TrafficLight:
    __color_tr = ["Red light", "Yellow light", "Green light"]

    def running(self):
        i = 0
        print("ATTENTION!\nWorking traffic light")
        sleep(2)
        while i < 3:
            print (f"Switches traffic light \n {TrafficLight.__color_tr[i]}")
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            elif i == 3:
                sleep(8)
            i += 1


TrafficLight = TrafficLight()
TrafficLight.running()



