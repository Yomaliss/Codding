month_count = 0
last_salary = 0
print('Последовательно введите зарплату за последние 10 месяцев')


while month_count < 10:
    month_count += 1
    salary = int(input(f'{month_count} месяц: '))

    if salary > last_salary:
        print('Зарплата увеличилась (по сравнению с предыдущим месяцем)!')
        last_salary = salary
    else:
        print('Вывод: зарплата с каждым месяцем не увеличивается')
        break
else:
    print('Вывод: зарплата с каждым месяцем увеличивается')
