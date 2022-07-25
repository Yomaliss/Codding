number = int(input('Введите число: '))
number_0 = 0
amount = 0


while number != 0:
    number_current = number
    number %= 10
    if number == 0:
        number = 1
    number_x = number
    number = number_current // 10
    amount += number_x


print(amount)
