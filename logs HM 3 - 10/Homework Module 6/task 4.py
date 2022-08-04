month_current = 0
month_even = 0
month_odd = 0
yes = 2
no = 1
end = 0

print('2 - да, 1 - нет, 0 - закончить подсчёт')

while True:
    month = int(input('Месяц чётный? '))
    month_current += 1
    print(f'Текущий месяц по счёту: {month_current}')

    if month == yes:
        print(f'Информация записана как: {month_current} месяц чётный')
        month_even += 1
    elif month == no:
        print(f'Информация записана как: {month_current} месяц нечётный')
        month_odd += 1
    elif month == end:
        print('Подсчёт закончен.')
        break
    else:
        print('Значение неверное.')
        month_current -= 1


print(f'Из {month_current} месяцев {month_even} - чётные.')
