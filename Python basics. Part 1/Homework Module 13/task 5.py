def numberCounter(_Number):
    numberCount = 0
    while _Number > 0:
        numberCount += 1
        _Number //= 10
    return numberCount


def replacingDigits(_Number):
    numberCount = numberCounter(_Number) - 1
    last_digit = _Number % 10
    first_digit = _Number // 10 ** numberCount
    between_digits = _Number % 10 ** numberCount // 10
    _Number = last_digit * 10 ** numberCount + between_digits * 10 + first_digit
    return _Number


firstNumber = int(input("Введите первое число: "))

if numberCounter(firstNumber) < 3:
    print('ОШИБКА!\n'
          'В первом числе меньше трёх цифр.')
    exit()

else:
    print(f'Изменённое первое число: {replacingDigits(firstNumber)}')
    secondNumber = int(input("Введите второе число: "))

    if numberCounter(secondNumber) < 4:
        print('ОШИБКА!\n'
              'Во втором числе меньше четырёх цифр.')
        exit()

    else:
        print(f'Изменённое второе число: {replacingDigits(secondNumber)}')

    print(f'\nСумма чисел: {replacingDigits(firstNumber) + replacingDigits(secondNumber)}')
