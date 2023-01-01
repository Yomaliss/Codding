number = int(input('Введите значение n, чтобы найти его факториал: '))
n_x = 1
x = 0

if number > 0:
    for x in range(1, number + 1):
        n_x *= x
    print(f'Факториал вашего числа - {x} - равен {n_x}')
elif number == 0:
    print('Факториал 0 = 1')
else:
    print('Факториал не может быть равен отрицательному числу')
