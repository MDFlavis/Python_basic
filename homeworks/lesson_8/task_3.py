'''
Создайте собственный класс-исключение, который должен
проверять содержимое списка на наличие только чисел.

Проверить работу исключения на реальном примере.
Необходимо запрашивать
у пользователя данные и заполнять список.

Класс-исключение должен
контролировать типы данных элементов списка.

Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно,
 пока пользователь сам не остановит работу скрипта, введя, например, команду “stop”.
  При этом скрипт завершается, сформированный список выводится на экран.

Подсказка: для данного задания примем, что пользователь может вводить только числа и
 строки. При вводе пользователем очередного элемента необходимо реализовать проверку
  типа элемента и вносить его в список, только если введено число. Класс-исключение должен
   не позволить пользователю ввести текст (не число) и отобразить соответствующее сообщение.
    При этом работа скрипта не должна завершаться.
'''


class NumberError(Exception):
    def __init__(self, txt):
        self.txt = txt


my_data = []

while True:
    user_data = input('Введите число или stop для завершения: ')
    if user_data == 'stop':
        break
    my_data.append(user_data)
    for el in range(len(my_data)):
        try:
            my_data[el] = int(my_data[el])
        except ValueError:
            print('Вы ввели не число, попытайтесь еще раз')
            my_data.pop()
    print(my_data)


print(f'Финальный список: {my_data}')


# try:
    #     for el in range(len(my_data)):
    #         try:
    #             if (my_data[el] == int(my_data[el])) is False:
    #                 raise NumberError('Вы ввели не число, попробуйте еще раз')
    #             my_data[el] = int(my_data[el])
    #             print(type(my_data[el]))
    #         except NumberError as err:
    #             print(err)
    #             my_data.pop()
    # except ValueError:
    #     print('НЕ ПО ПЛАНУ')
    # print(my_data)

# while True:
#     user_data = input('Введите число или stop для выхода: ')
#     if user_data == 'stop':
#         break
#     try:
#         user_data = int(user_data)
#         if user_data == str:
#             raise NumberError('Вы ввели не число, попытайтесь снова')
#     except ValueError as NumberError:
#         print(NumberError)
#     my_data.append(user_data)
#     print(my_data)