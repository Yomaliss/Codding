def factorialNumber(_x):
    factorial = 1
    for counter in range(2, _x + 1):
        factorial *= counter
    return factorial


def degreeNumber(_x, _n):
    count = 1
    for number in range(1, _n + 1):
        count *= _n
    return count


precision = float(input('Введите точность: '))
x = float(input('Введите X: '))               # Переменная X в уравнении
n = 0                                         # Переменная N в уравнении
ceil = 1
result = 0

while abs(ceil) > precision:
    ceil = degreeNumber(-1, n) * (degreeNumber(x, (2 * n)) / factorialNumber(2 * n))
    result += ceil
    n += 1

print(f'Сумма ряда = {result}')