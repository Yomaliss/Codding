heigth = int(input('Введите высоту пирамиды: '))
amount = 1


for row in range(heigth):
    print(' ' * (heigth - 1 - row),
          '#' * amount,
          end='')
    amount += 2
    print()
