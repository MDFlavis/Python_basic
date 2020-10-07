# Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом: for el in fact(n)
#     Функция отвечает за получение факториала числа, а в цикле необходимо выводить
#     только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n.

def fact(digit):
    i = 1
    result = 1
    while i <= digit:
        yield result
        i += 1
        result *= i

for el in fact(3):
    print(el)

