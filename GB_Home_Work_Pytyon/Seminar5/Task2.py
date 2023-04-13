def sum(a: int, b: int):
    if b == 0:
        return a
    elif b > 0:
        return sum(a + 1, b - 1)
    else:
        return sum(a - 1, b + 1)

print(sum(2,2))