# PEP 8


#snake_case = 1 | Переменные и функции
#CamelCase = 2  | Классы
# camelCase = 3 | WRONG!
#kebab-case = 10|   WRONG!

some_str = "Hello my friends" # str()
some_str2 = 'Hello my friends'

some_int = 1 # int()
some_float = 2.33333234321 # float()
some_bool = True # bool()


ask_name = "Введите имя \n"
ask_age = "Введите возраст \n"

#name = input(ask_name)

#print("Привет", name, end= '!!!!!!', sep='---')


#age =int(input(ask_age)) Пока нет

#age =input(ask_age)
#if age.isdigit():
#    age_int = int(age) # age = int(age)
#    if age >= 18:
#        print('Доступ к разделам ХХХ открыт')
#    elif age > 16:
#        print('Доступ к боевикам')
#    else:
#        print('Смотри мультики')
#else:
#    print('Введено не число')
#    print('Повторите ввод')

#print('HELLO')
#print('WORLD')
#print(age)


a = 1234561234567
temp = a
while temp:
    tmp = temp % 10
    temp //= 10
    if tmp ==5:
        continue
    # a =  a // 10 # a //= 10
    print(tmp, temp)
else:
    print('else')