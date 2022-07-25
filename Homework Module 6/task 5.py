number = int(input('Введите номер билета: '))
number_y = number
n = 0
number_amount_1 = 0
number_amount_2 = 0
number_1 = number % 1000
number_2 = number // 1000


while number_y > 0:
    n += 1
    number_y //= 10


if n % 2 == 0:
    while number_1 != 0:
        number_x = number_1 % 10
        number_1 //= 10
        number_amount_1 += number_x
    while number_2 != 0:
        number_x = number_2 % 10
        number_2 //= 10
        number_amount_2 += number_x
    print(f'Сумма последних 3 чисел билета = {number_amount_1} \n \
            Сумма первых 3 чисел билета = {number_amount_2}')

    if number_amount_1 == number_amount_2:
        print('Ваш билет счастливый!')
    else:
        print('Ваш билет не счастливый.')
else:
    print('Номер билета не соответствует условию')
