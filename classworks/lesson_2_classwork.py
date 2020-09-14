var_str = "Это строка" # str неизменяемый тип коллекция итерируемый
# Индексы и разрезы, в var_str индекс 1 - Э, 2 - т и т.д., разрез это var_str[::2]
var_int = 22 # int неизменяемы тип
var_float = 2.33 # float неизменяемое число
var_list = [1, 2, 3, 4, 5, [1, 2, 3], True, False, 'HELLO'] # list любые типы данных, изменемы коллекция итерируемая
var_tuple = (1, 2, 3, 4, 5, [1, 2, 3], True, False, 'HELLO') # кортеж tuple неизменяемая коллекция

var_set = {1, 2, 3, 4, 5, 6, 1, 2, 3,  (1, 2, 3)} # set множество изменяемый не индексируемый

var_dict = {'key': 'Hello', 1:22, (1,2): 33} # dict словарь изменяемый итерируемый

# i = 0
# while i < len(var_str):
#     char = var_str[i]
#     print(char)
#     i += 1

# for char in var_str;
#     print(char)

# user_template = {
#     'age': 'Введите возраст',
#     'name': 'Введите имя',
#     'surname': 'Введите фамилию',
#     'phone': 'Номер'
# }
#
# user = {}
# for key, ask in user_template.items():
#     user[key] = input(ask+'\n')
#
# print(user)

# for key, value in var_dict.items():
#     print(key, value)

# for idx, char in enumerate(var_str):
#     print((idx, char))

# for idx, num in enumerate(range(9, -10, -1), 77):
#     print(idx, num)

temp = {}
for idx, num in enumerate(range(9, -10, -1), 77):
    temp[idx] = num

print(temp)
