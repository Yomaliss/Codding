import math


horse_x = float(input('Введите местоположение коня по горизонтали: '))
horse_y = float(input('Введите местоположение коня по вертикали: '))
point_x = float(input('Введите местоположение точки по горизонтали: '))
point_y = float(input('Введите местоположение точки по вертикали: '))


if 0 <= horse_x <= 0.8 and 0 <= horse_y <= 0.8 and 0 <= point_x <= 0.8 and 0 <= point_y <= 0.8:
    horse_x *= 10
    horse_y *= 10
    point_x *= 10
    point_y *= 10
    horse_x = math.floor(horse_x)
    horse_y = math.floor(horse_y)
    point_x = math.floor(point_x)
    point_y = math.floor(point_y)

    print(f'Конь в клетке ({horse_x},{horse_y}). Точка в клетке ({point_x},{point_y})')

    if (abs(point_x - horse_x) == 2 and abs(point_y - horse_y) == 1) or \
            (abs(point_x - horse_x) == 1 and abs(point_y - horse_y) == 2):
        print('Конь может ходить в эту точку.')
    elif horse_x == point_x and horse_y == point_y:
        print('Конь уже в этой точке.')
    else:
        print('Конь не может ходить в эту точку.')
else:
    print('Неверно заданные условия.')
