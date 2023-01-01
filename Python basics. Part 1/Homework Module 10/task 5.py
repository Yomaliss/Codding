number = int(input('Введите количество чисел: '))
count = 0


for num in range(1, number + 1):
    set_number = int(input(f'Введите {num} число: '))
    for check in range(2, set_number):
        if set_number % check == 0:
            print('Число составное.')
            break
        else:
            print('Число простое.')
            count += 1
            break
    if set_number == 2:
        print('Число простое.')
        count += 1

print(f'Количество простых чисел в последовательности: {count}')
