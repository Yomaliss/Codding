width = int(input('Введите ширину: '))
heigth = int(input('Введите высоту: '))


for row in range(heigth):
    for col in range(width):
        if col == 0 or col == width - 1:
            print('|', end='')
        elif row == 0 or row == heigth - 1:
            print('-', end='')
        else:
            print(' ', end='')
    print('')