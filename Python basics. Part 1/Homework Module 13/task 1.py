def fpf(numb):
    counter = 0
    if numb >= 1:
        while not 1 <= numb < 10:
            numb /= 10
            counter += 1

    else:
        while not 1 <= numb < 10:
            numb *= 10
            counter -= 1

    print(f'Число в формате плавающей точки: {numb} * 10 ** {counter}')


enterNumb = float(input('Введите число: '))

if enterNumb > 0:
    fpf(enterNumb)

else:
    print('Число не может быть меньше или равно 0. ')
