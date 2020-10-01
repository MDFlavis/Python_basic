# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса
# Pen (ручка), Pencil (карандаш), Handle (маркер). В каждом из классов реализовать
# переопределение метода draw. Для каждого из классов методы должен выводить уникальное
# сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для
# каждого экземпляра.

class Stationery:
    title = 'unknown'

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    title = 'Перо'

    def draw(self):
        print(f'Запуск отрисовки с помощью инструмента: {self.title}')


class Pencil(Stationery):
    title = 'Карандаш'

    def draw(self):
        print(f'Запуск отрисовки с помощью инструмента: {self.title}')


class Handle(Stationery):
    title = 'Ручка'

    def draw(self):
        print(f'Запуск отрисовки с помощью инструмента: {self.title}')


a = Stationery()
a.draw()

b = Pen()
b.draw()

c = Pencil()
c.draw()

d = Handle()
d.draw()
