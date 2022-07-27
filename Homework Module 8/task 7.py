educational_grant = int(input('Введите стипендию: '))
expenses = int(input('Введите расходы на проживание: '))
total_educational_grant = educational_grant
total_expenses = expenses


if educational_grant > expenses:
    print('Расходы на проживание должны быть выше стипендии')
else:
    for month in range(2, 10 + 1):
        total_educational_grant += educational_grant
        expenses += expenses * 3 / 100
        total_expenses += expenses

print(f'У родителей необходимо попросить: '
      f'{total_expenses - total_educational_grant}')
