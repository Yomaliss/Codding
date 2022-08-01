number = int(input('Введите число: '))
past_num = 1
past_fact = 1
num = 1
amount_factorial = 0


for factorial in range(1, number + 1):
    for num in range(1, factorial + 1):
        num *= past_num
        past_num = num
    past_num = 1
    amount_factorial += num

print(amount_factorial)
