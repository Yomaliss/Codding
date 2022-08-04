debtors = int(input('Введите число должников: '))
debt_total = 0


for number in range(0, debtors, 5):
    print(f'Должник с номером {number}')
    debt_total += int(input('Сколько должны? '))
print(f'Общая сумма долга: {debt_total}')
