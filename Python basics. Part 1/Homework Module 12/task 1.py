def summa_n(n):
    amount = 0
    for number in range(1, n + 1):
        amount += number
    print(f'Я знаю, что сумма чисел от 1 до {n} равна {amount}')


num = int(input('Введите число: '))
summa_n(num)
