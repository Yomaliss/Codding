number = int(input('Введите число: '))


for row in range(number + 1):
    for col in range(number + 1):
        print(row * 2 + col, end='\t')
    print('\t')