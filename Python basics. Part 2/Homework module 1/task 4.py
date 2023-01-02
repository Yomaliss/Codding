import math


def reverse_number(number):
    frac, whole = math.modf(number)
    return str(int(whole))[::-1] + '.' + str(int(float(str(round(frac, 2))[::-1])))


number_1 = float(input('Введите первое число: '))
number_2 = float(input('Введите второе число: '))
print(float(reverse_number(number_1)) + float(reverse_number(number_2)))
