a = int(input('Введите 1 число: '))
b = int(input('Введите 2 число: '))
c = int(input('Введите 3 число: '))
total_number = 0
counter = 0

for number in range(a - 1, b + 1, c):
    counter += 1
    total_number += number
print(f'Среднее арифметическое чисел от {a} до {b}, кратных {c}: \n \
{total_number // counter}')
