# Программа запрашивает у пользователя строку чисел,
# разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел.
#
# Пользователь может продолжить ввод чисел,
# разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной
# сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается.

# Если специальный
# символ введен после нескольких чисел, то вначале нужно
# добавить сумму этих чисел к полученной ранее сумме и после
# этого завершить программу.

end = True
sum_result = 0
while end == True:
    digits = input('Введите числа через пробел или q для выхода: ')
    digits_data = digits.split()
    res = 0

    for el in range(len(digits_data)):
        if digits_data[el] == 'q' or digits_data[el] == 'Q':
            end = False
            break
        else:
            try:
                digits_data[el] = int(digits_data[el])
            except ValueError:
                digits_data[el] = float(digits_data[el])

        res = res + digits_data[el]

    sum_result += res
    print(f'Результат сложения равен {sum_result}')

print(f'Окончательный результат - {sum_result}')