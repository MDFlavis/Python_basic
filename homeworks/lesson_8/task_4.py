# Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать параметры,
# уникальные для каждого типа оргтехники.

class Stock:
    pass


class OfficeEquip:
    def __init__(self, name , cost, weight, width, height):
        self.name = name
        self.weight = weight
        self.width = width
        self.height = height
        self.cost = cost

    def __str__(self):
        return f'Name: {self.name}| Cost: {self.cost} ' \
               f'\n Weight: {self.weight}| Width: {self.width}| Height: {self.height}  '


class Printer(OfficeEquip):
    def __init__(self, name, cost, weight, width, height, color):
        super().__init__(name, cost, weight, width, height)
        self.color = color


class Scanner(OfficeEquip):
    def __init__(self, name , cost, weight, width, height, matrix):
        super().__init__(name , cost, weight, width, height)
        self.matrix = matrix


class Xerox(OfficeEquip):
    def __init__(self, name , cost, weight, width, height, copy_speed):
        super().__init__(name , cost, weight, width, height)
        self.copy_speed = copy_speed

printer = Printer('Samsung', 2500, '5 kg', '50 * 20 sm', '30 sm', 'white')
print(printer)