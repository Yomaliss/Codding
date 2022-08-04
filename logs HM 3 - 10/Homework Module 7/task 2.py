number = 0
first_number = int(input('Введите первое число диапазона: '))
second_number = int(input('Введите второе число диапазона: '))
n = 0


for number in range(first_number, second_number + 1):
    if number % 2 == 0:
        if number > 0:
            n += 1
            print(f'Число {number} подходит под условия')


print(f'{n} чисел подходят под условия')
