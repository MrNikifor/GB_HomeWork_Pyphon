# Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X.
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно содержится в списке.
#
# Примеры/Тесты:
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
# Output: 2
# Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
# Output: 10
# Решение задачи
my_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
x = int(input('Введите число: '))
closest_num = my_list[0]
for num in my_list:
    if abs(num - x) < abs(closest_num - x):
        closest_num = num
print(f' Ваше число: {closest_num}')

# Решение 2
# N = int(input("Введите число N"))
# X = int(input("Введите число X"))
# A = [randint(1, N) for x in range(1, N+1)]
# number = 0
# for i in range(N):
#     if (X-A[i]) < X-number and X-A[i] > 0:
#         number = i
# print(A[number])