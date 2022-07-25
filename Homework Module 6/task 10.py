first_number = 1
last_number = 100
n = 0
print('Загадайте число от 1 до 100')


while first_number <= last_number:
    n += 1
    mid_number = (first_number + last_number) // 2
    print(f'Вы загадали это число? {mid_number}')
    print('Команды:')
    answer = int(input('Введите число от 1 до 3, которое поможет компьютеру отгадать число: \n \
1 - равно \n \
2 - больше \n \
3 - меньше \n '
                       ''))
    if answer == 3:
        last_number = mid_number - 1
    elif answer == 2:
        first_number = mid_number + 1
    elif answer == 1:
        print('Компьютер отгадал ваше число!')
        break
    else:
        print('Это число не входит в список доступных чисел.')
