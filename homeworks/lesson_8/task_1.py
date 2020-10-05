# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках
# класса реализовать два метода.
# Первый, с декоратором @classmethod,
# должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца
# и года (например, месяц — от 1 до 12). Проверить работу полученной структуры
# на реальных данных.

class Data:
    def __init__(self, data: str):
        self.data = data

    @classmethod
    def first(cls, data: str):
        day, month, year = map(int, data.split('-'))
        return f'Day {day}, month {month}, year {year} '

    @staticmethod
    def second(day, month, year):
        if day not in range(1, 33) or month not in range(1, 13) or year not in range(1, 2021):
            return f'Ошибка валидации'
        else:
            return f'Валидация прошла успешно'


print(Data.first('1-12-2020'))
print(Data.second(2, 12, 2020))
