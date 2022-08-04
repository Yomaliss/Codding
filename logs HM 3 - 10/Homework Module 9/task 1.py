day = input('Введите день недели: ')
count = 0
check = True


for days in ('понедельник', 'вторник', 'среда', 'четверг', 'пятница',
             'суббота', 'воскресенье'):
    count += 1
    if days == day.lower():
        print(f'Номер дня недели: {count}')
        check = False

if check:
    print('Такого дня недели не существует, либо он написан неправильно')
