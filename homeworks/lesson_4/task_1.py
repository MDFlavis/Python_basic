# Реализовать скрипт, в котором должна быть предусмотрена
# функция расчета заработной платы сотрудника. В расчете
# необходимо использовать формулу: (выработка в часах *
# ставка в час) + премия. Для выполнения расчета для
# конкретных значений необходимо запускать скрипт с параметрами.
from sys import argv

def salary(hours, s_per_h, prize):
    '''
    Функция вычисления зарплаты
    :param hours: выработка в часах
    :param s_per_h: ставка в час
    :param prize: премия
    :return: зарплата сотредника
    '''
    res = hours * s_per_h + prize
    return res

script_name, hours, s_per_h, prize = argv

print('Имя скрипта: ', script_name)
print('Выработка в часах: ', hours)
print('Ставка в час: ', s_per_h)
print('Премия: ', prize)
print('Зарплата сотрудника: ', salary(int(hours), int(s_per_h), int(prize)))
