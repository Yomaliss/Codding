number = int(input('Введите n: '))
s = 1
x = 1


for n in range(1, number + 1):
    x = ((-1) ** n) / (2 ** n)
    s += x

print(f'Сумма ряда - {s}, член ряда - {x}')
