# Пример применения побитового оператора &.
# Уровни доступа пользователя

read = 1        # чтение
write = 2       # запись
execute = 4     # изменение

quest = read                        # уровни доступа
user = read | write
admin = read | write | execute

Kolya = read
print(Kolya & execute)          # Вывод значения 0 - нет доступа