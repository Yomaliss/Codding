def calculatorDepth(_upperBound, _lowerBound):
    return _lowerBound + (_upperBound - _lowerBound) / 2


def calculatorDanger(_depth):
    return _depth ** 3 - 3 * _depth ** 2 - 12 * _depth + 10


maxDanger = float(input('Введите максимально допустимый уровень опасности: '))
upperBound = 0.0
lowerBound = 4.0

if maxDanger <= 0:
    print('Максимально допустимый уровень опасности не может быть меньше 0. Проверьте правильность ввода.')
else:
    depth = calculatorDepth(upperBound, lowerBound)
    danger = calculatorDanger(depth)
    while abs(danger) > maxDanger:
        if danger > 0:
            upperBound = depth
        else:
            lowerBound = depth
        depth = calculatorDepth(upperBound, lowerBound)
        danger = calculatorDanger(depth)
    print(f'Приблизительная глубина безопасной кладки: {depth} м')
