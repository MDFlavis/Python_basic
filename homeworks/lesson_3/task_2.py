# Реализовать функцию, принимающую несколько параметров,
# описывающих данные пользователя: имя, фамилия, год
# рождения, город проживания, email, телефон. Функция должна
# принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(name, surname, year, city, email, phone):
    return " ".join([name, surname, year, city, email, phone])

name = input('Введите ваше имя: ')
surname = input('Введите вашу фамилию: ')
year = input('Введите ваш год рождения: ')
city = input('Введите ваш город проживания: ')
email = input('Введите ваш email: ')
phone = input('Введите ваш телефонный номер: ')

user = my_func(name, surname, year, city, email, phone)

print(user)