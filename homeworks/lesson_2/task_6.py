# Реализовать структуру данных «Товары». Она должна
# представлять собой список кортежей. Каждый кортеж хранит
# информацию об отдельном товаре. В кортеже должно быть два
# элемента — номер товара и словарь с параметрами
# (характеристиками товара: название, цена, количество, единица
# измерения). Структуру нужно сформировать программно, т.е.
# запрашивать все данные у пользователя.
# Пример готовой структуры:
# [
# (1, {“название”: “компьютер”, “цена”: 20000, “количество”: 5, “eд”: “шт.”}),
# (2, {“название”: “принтер”, “цена”: 6000, “количество”: 2, “eд”: “шт.”}),
# (3, {“название”: “сканер”, “цена”: 2000, “количество”: 7, “eд”: “шт.”})
# ]
# Необходимо собрать аналитику о товарах. Реализовать
# словарь, в котором каждый ключ — характеристика товара,
# например название, а значение — список значений-
# характеристик, например список названий товаров.
# Пример:
# {
# “название”: [“компьютер”, “принтер”, “сканер”],
# “цена”: [20000, 6000, 2000],
# “количество”: [5, 2, 7],
# “ед”: [“шт.”]
# }

products = []

def new_product(product_list):
    product_number = 0
    while product_number != 666:
        product_number = int(input("Введите порядковый номер создаваемого продукта(666 если хотите выйти): "))
        if product_number == 666:
            break
        else:
            product_info = dict(Название=input('Введите название товара: '), Цена=input('Введите стоимость товара: '),
                    Колличество=input('Введите коллическтво товара: '), ед='шт')
            product_tuple = (product_number, product_info,)
            product_list.append(product_tuple)
    return product_list

def anal_names(need_key, product_list):
    key_values = []
    for el in range(len(product_list)):
        value_name = product_list[el][1].get(need_key)
        key_values.append(value_name)
    return key_values

products = new_product(products)

print(f'Ответ: спиок - {products}')

my_keys = list(products[0][1].keys())

name_values = anal_names('Название', products)
cost_values = anal_names('Цена', products)
number_values = anal_names('Колличество', products)
unit_values = anal_names('ед', products)

values_list = [name_values, cost_values, number_values, unit_values]

anal_dict = {}

for el in range(len(values_list)):
    anal_dict.update({my_keys[el]: values_list[el]})

print(f'Ответ: второе задание, аналитика - {anal_dict}')