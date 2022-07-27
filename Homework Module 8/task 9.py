total_number_1 = 1
total_number_2 = 1
number_1 = 0
number_2 = 0
x = int(input('Введите x: '))


for number_1 in range(1, 63, 2):
    total_number_1 *= (x - number_1)

for number_2 in range(2, 64, 2):
    total_number_2 *= (x - number_2)

print(f'Сумма ряда - {number_1 / number_2}')
