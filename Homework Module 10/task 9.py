levels = int(input('Введите количество уровней пирамиды: '))
amount = 1


for row in range(1, levels + 1):
    print('\t' * (levels - row), end='')
    for col in range(row):
        print(amount, end='')
        amount += 2
        print('\t' * 2, end='')
    print()
