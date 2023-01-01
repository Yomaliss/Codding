def test():
    number = int(input('Введите число: '))
    if number < 0:
        negative()
    elif number > 0:
        positive()


def negative():
    print('Отрицательное')


def positive():
    print('Положительное')


test()
