number_rows = int(input('Введите количество рядов: '))
number_seats = int(input('Введите количество сидений в ряду: '))
number_distance = int(input('Введите расстояние между рядами: '))


print('Сцена')

for _number in range(1, number_rows + 1):
    print('=' * number_seats, '*' * number_distance, '=' * number_seats)
