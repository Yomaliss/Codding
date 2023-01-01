hours = int(input('Введите отработанные часы: '))
income = ((200 * hours) / 2 ** 3) + hours
money_credit = int(input('Введите остаток по кредиту: '))
money_food = int(input('Введите затраты на еду: '))
expenses = money_credit + money_food
if income >= expenses:
    print('Часов хватает. Можно отдохнуть')
else:
    print('Часов не хватает. Придётся работать!')
