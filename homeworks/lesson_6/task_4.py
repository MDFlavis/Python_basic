# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала, остановилась, повернула (куда). Опишите
# несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый
# класс метод show_speed, который должен показывать текущую скорость автомобиля. Для классов
# TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
# и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к
# атрибутам, выведите результат. Выполните вызов методов и также покажите результат.
import random


class Car:
    speed = random.randrange(5, 70)
    color = 'unknown'
    name = 'unknown'
    is_police = True

    def go(self):
        print('Автомобиль пришел в движение, ПОЕХАЛИ')

    def stop(self):
        print('Автомобиль остановился, СТОП')

    def turn(self):
        direction = [
            'Автомобиль повернул направо',
            'Автомобиль повернул налево',
        ]
        print(random.choice(direction))

    def show_speed(self):
        print(self.speed)


class TownCar(Car):

    def show_speed(self):
        if super().speed > 60:
            return print("Вы превысили скорость")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if super().speed > 40:
            return print("Вы превысили скорость")


class PoliceCar(Car):
    pass


car1 = TownCar()
car1.go()
print(car1.speed)
car1.show_speed()
car1.turn()
car1.stop()


car2 = SportCar()
car2.go()

car2.show_speed()
car2.turn()
car2.stop()

car3 = WorkCar()
car3.go()
print(car3.speed)
car3.show_speed()
car3.turn()
car3.stop()

car4 = PoliceCar()
car4.go()
car4.show_speed()
car4.turn()
car4.stop()