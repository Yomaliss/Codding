profit = int(input('Введите вашу прибыль: '))
bar_1 = 10000  # Первая планка повышения налога
bar_2 = 50000  # Вторая планка повышения налога
perc_1 = 13  # Прогрессивный налог до 10000
perc_2 = 20  # Прогрессивный налог от 10000 до 50000
perc_3 = 30  # Прогрессивный налог от 50000

if profit < 0:
    print('Введенное число не соответствует условию')
else:
    if profit < bar_1:
        tax = profit * perc_1 / 100
        profit -= tax
    elif bar_1 <= profit < bar_2:
        tax_1 = (profit - bar_1) * perc_2 / 100
        tax_2 = bar_1 * perc_1 / 100
        tax = tax_1 + tax_2
        profit -= tax
    else:
        tax_1 = (profit - bar_2) * perc_3 / 100
        tax_2 = (bar_2 - bar_1) * perc_2 / 100
        tax_3 = bar_1 * perc_1 / 100
        tax = tax_1 + tax_2 + tax_3
        profit -= tax

print(f'Налог составляет {tax} \n'
      f'Прибыль с учетом налога составляет {profit}')
