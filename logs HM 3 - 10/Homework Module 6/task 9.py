number = 0
n = 0
hide_number = int(input('Введите загаданное число: '))


while number != hide_number:
    n += 1
    number = int(input('Введите число: '))
    if number < hide_number:
        print('Число меньше, чем нужно. Попробуйте ещё раз!')
    elif number > hide_number:
        print('Число больше, чем нужно. Попробуйте ещё раз!')
    else:
        print(f'Вы угадали!Число попыток: {n}')
