# Создайте собственный класс-исключение, обрабатывающий
# ситуацию деления на нуль. Проверьте его работу на данных,
# вводимых пользователем. При вводе пользователем нуля в качестве
# делителя программа должна корректно обработать эту ситуацию и не
# завершиться с ошибкой.

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt


user_data = input('Введите число: ')


try:
    user_data = int(user_data)
    if user_data < 0:
        raise MyError('Вы ввели отрицательное число')
except ValueError:
    print("Вы ввели не число")
except MyError as err:
    print(err)
else:
    print('Все ок')