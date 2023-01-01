import math


count_numbers = int(input('Введите количество чисел: '))


for num in range(count_numbers):
    number = float(input('Введите число: '))
    if number < 0:
        print(f'exp(x) = {math.exp(math.floor(number))}')
    elif number > 0:
        print(f'log(x) = {math.log(math.ceil(number))}')
    else:
        print('Ответ: 0')
