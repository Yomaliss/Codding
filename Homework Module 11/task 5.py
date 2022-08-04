import math


size_earth = 10.831 * 10 ** 11
radius_planet = float(input('Введите радиус случайной планеты: '))
size_planet = (4 / 3) * math.pi * radius_planet ** 3


if size_earth > size_planet:
    print(f'Размер земли в {round(size_earth / size_planet, 3)} раз больше случайной планеты.')
elif size_planet > size_earth:
    print(f'Размер случайной планеты в {round(size_planet / size_earth, 3)} раз больше земли.')
else:
    print(f'Размер планет одинаковый.')
