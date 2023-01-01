def check_point(x_point, y_point):
    x_square = 1
    y_square = 1
    if -x_square <= x_point <= x_square and -y_square <= y_point <= y_square:
        print('Монетка где-то рядом.')
    else:
        print('Монетки в области нет.')


x = float(input('Введите x: '))
y = float(input('Введите y: '))
check_point(x, y)
