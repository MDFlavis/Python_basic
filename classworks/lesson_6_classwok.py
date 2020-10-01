import random

NAMES = ('Шарик', 'Бобик', 'Пират')

class Animal:
    __age = 0
    __population = []

    def __init__(self, a_type, mass):
        print('START INIT')
        print(id(self))
        self.a_type = a_type
        self.mass = mass
        print('END INIT')
        self.__population.append(self)

    def say(self):
        print(f"{self.name}'asdasdd"")

    def get_age(self):
        return self.__age

    def get_population(self):
        return tuple(self.__population)

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(self.a_type, random.randint(1, 10))

class Dog(Animal):
    def __init__(self, name, mass):
        self.name = name
        super().__init__('Собака', random.randint(1, 3))

    def say(self):
        print('ГАВ ГАВ')

    def breeding(self, other):
        cls = random.choice((type(self), type(other)))
        return cls(random.choice(NAMES))

class Cat(Animal):
    def __init__(self):
        self.name = name
        super().__init__('Кошка', random.randint(1, 3))

    def say(self):
        print('Мяу')

class Zoo:
    def __init__(self, name):
        self.name = name
        self.__animals = {}
    def add_animal(self, animal):
        if self.__animals.get(animal.a_type):
            self.__animals.get(animal.a_type).append(animal)
        else:
            self.__animals.get[animal.a_type] = [animal]
    def atype_population(self, atype):
        return self.__animals.get(atype)

zoo = Zoo('jhjjk')
animal1 = Animal('Пес', 27)
dog1 = Dog('Шарик')
print(id(animal1))
print('#' * 20)
animal2 = Animal('Кот', 8)
dog2 = Dog('Хатико')
zoo.add_animal(dog1)
zoo.add_animal(animal2)
cat1 = Cat('Барсик')
cat2 = Cat('Борис ')
zoo.add_animal(cat2)

print(1)