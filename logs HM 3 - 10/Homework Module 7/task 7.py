a = int(input('Введите число a: '))
b = int(input('Введите число b: '))
needed_number = 0
n = 0


if a > b:
    a, b = b, a

for number in range(a, b + 1):
    if number % 3 == 0:
        n += 1
        print(f'Число {number} кратно трём')
        needed_number += number
    else:
        print(f'Число {number} не кратно трём')

if n > 0:
    print(f'Среднее арифметическое чисел, кратных 3 в диапазоне от '
          f'{a} до {b} = {needed_number // n}')
else:
    print('Числа, кратные 3, отсутствуют')
