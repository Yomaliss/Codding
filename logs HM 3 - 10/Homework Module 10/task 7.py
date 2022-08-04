amount = 0
last_amount = 0
needed_number = 0


print('Чтобы закончить ввод чисел, введите 0: ')
while True:
    number = int(input('Введите натуральное число: '))
    if number < 0:
        print('Число не натуральное, повторите ввод')
    elif number == 0:
        print('Ввод чисел закончен.')
        break
    else:
        temp = number
        while number != 0:
            letter = number % 10
            amount += letter
            number //= 10
        if amount > last_amount:
            last_amount = amount
            needed_number = temp
            amount = 0

print(f'Наибольшая сумма цифр в числе {needed_number} - {last_amount}')
