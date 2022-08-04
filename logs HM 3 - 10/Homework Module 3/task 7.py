v = int(input('Введите скорость (в км/ч): '))
t = int(input('Введите время (в ч): '))
road_length = 115
distance_travelled = v * t
stopped = distance_travelled % road_length
print('На этом километре остановился водитель:', stopped)
