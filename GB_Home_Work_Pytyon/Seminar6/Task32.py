# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)
from random import randint
lenght = int(input("Введите длинну массива: "))
start = int(input("введите число начала диапозона: "))
end = int(input("введите число конца диапазона: "))
array = [randint(0,10) for i in range(lenght)]
print(array)
for i in range(lenght):
    if array[i] >= start and array[i] <= end:
        print(i, end=" ")