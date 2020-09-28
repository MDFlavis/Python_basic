# Создать программно файл в текстовом формате, записать в
# него построчно данные, вводимые пользователем. Об
# окончании ввода данных свидетельствует пустая строка.

my_file = open('my_file.txt', 'w')
user_data = input('Введите данные, что бы выйти не вводите ничего: ')

while user_data:
    my_file.write(user_data)
    user_data = input('Введите данные, что бы выйти - не вводите ничего: ')
my_file.close()

my_file = open('my_file.txt', 'r')
content = my_file.read()
print(content)
my_file.close()

