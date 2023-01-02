def min_divisor(_number):
    minimum = _number
    for x in range(_number - 1, 1, -1):
        if _number % x == 0:
            if minimum > x:
                minimum = x
    return minimum


number = int(input('Введите число: '))
if number <= 1:
    print('Число должно быть положительным и больше 1!')
else:
    print(f'Наименьший делитель, отличный от единицы: {min_divisor(number)}')
