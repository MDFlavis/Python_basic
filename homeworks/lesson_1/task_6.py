# Спортсмен занимается ежедневными пробежками. В первый
# день его результат составил a километров. Каждый день
# спортсмен увеличивал результат на 10 % относительно
# предыдущего. Требуется определить номер дня, на который
# общий результат спортсмена составить не менее b
# километров. Программа должна принимать значения
# параметров a и b и выводить одно натуральное число — номер
# дня.

a = int(input('Сколько спортсмен пробежал в первый день: '))
b = int(input('К какому ежедневному результату стремится спортсмен: '))
days = 1


while a < b:
    a = a + a/10
    days += 1
    print (days,'-й день: ',"{:.2f}".format(a))

print('Ответ: на',days,'-й день спортсмен достиг результата — не менее', b,' км.')

# a = int(input('Сколько спортсмен пробежал в первый день: '))
# b = int(input('Общий результат спортсмена должен составить: '))
# days = 1
# km = a

# while km < b:
#     a = a + a/10
#     km = km + a
#     days = days + 1
#
# print('Спортсмен пробежит ', b , 'километров на ',days , 'день')
