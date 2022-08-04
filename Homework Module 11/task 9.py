import math


a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

# a * x ** 2 + b * x + c = 0
if a != 0:
    D = b ** 2 + 4 * a * c
    D = math.sqrt(D)
    if D > 0:
        x_1 = (-b + D) / (2 * a)
        x_2 = (-b - D) / (2 * a)
        print(f'В уравнении 2 корня - {x_1} и {x_2}')
    elif D == 0:
        x_1 = -(b / (2 * a))
        print(f'В уравнении 1 корень - {x_1}')
    else:
        print('Корней нет')
