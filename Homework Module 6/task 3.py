number_0 = 0
amount = 1

number = int(input('Введите число: '))
while number // 10 != 0:
    number //= 10
    amount += 1

print(f'В заданном числе 5 цифр')
