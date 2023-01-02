print('Введите координаты монетки')
coord_x = float(input('Введите X: '))
coord_y = float(input('Введите Y: '))
radius = float(input('Введите радиус: '))

if -radius <= coord_x <= radius and -radius <= coord_y <= radius:
    print('Монетка где-то рядом')
else:
    print('Монетки в области нет')