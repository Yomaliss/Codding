size = int(input('Введите число: '))


for row in range(size + 1):
    for col in range(size + 1):
        if row == col:
            print('^', end='')
        if col == -row + size:
            print('^', end='')
        else:
            print(' ', end='')
    print()
