# 1.3[6]. Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# Примеры/Тесты:
# 385916 >>> yes
# 123456 >>> no

# Решение:

number_ticket = input('Введите номер билета: ')

first_free_number = int(number_ticket[0]) + int(number_ticket[1]) + int(number_ticket[2])
second_free_number = int(number_ticket[3]) + int(number_ticket[4]) + int(number_ticket[5])

if first_free_number == second_free_number:
    print('yes')
else:
    print('no')

# Решение с *:   (подсмотрел)

# print("yes" if sum(map(ord, number_ticket[:3])) == sum(map(ord, number_ticket[3:])) else "no")
