# Реализовать функцию my_func(), которая принимает три
# позиционных аргумента, и возвращает сумму наибольших двух
# аргументов. 2  1  8     var 1 и var 2, var 1 и var 3 | var2 and var1, var2 and var3 | var3 and var1, var3 and var2

def my_func(var_1, var_2, var_3):
    if var_1 >= var_3 and  var_2 >= var_3:
        return var_1 + var_2
    elif var_1 >= var_2 and var_3 >= var_2:
        return var_3 + var_1
    elif var_2 >= var_1 and var_3 >= var_1:
        return var_2 + var_3


var_1 = int(input("Введите первое число"))
var_2 = int(input('Введите второе число'))
var_3 = int(input('Введите третье число'))

answer = my_func(var_1, var_2, var_3)

print(answer)