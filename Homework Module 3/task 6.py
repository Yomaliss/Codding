x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
x_last_two_digits = x % 100
y_last_two_digits = y % 100
amount_last_two_digits = x_last_two_digits + y_last_two_digits
print('Сумма двух последних разрядов этих чисел:', amount_last_two_digits)
