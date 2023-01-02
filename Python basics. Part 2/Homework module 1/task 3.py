def sum_digits(_number):
    if _number <= 0:
        print('Проверьте ввод')
    else:
        amount = 0
        while _number != 0:
            amount += _number % 10
            _number //= 10
    print(f'Сумма цифр: {amount}')
    return amount


def len_digits(_number):
    _number = str(_number)
    print(f'Количество цифр в числе {len(_number)}')
    return len(_number)


number = int(input('Введите положительное число: '))
print(f'Разность суммы и количества цифр: {sum_digits(number) - len_digits(number)}')