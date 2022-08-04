mileage = int(input('Введите пробег: '))  # трёхзначное число
today = int(input('Введите сегодняшнее число: '))
mileage_1 = mileage // 100
mileage_2 = mileage // 10 % 10
mileage_3 = mileage % 10
mileage_amount = mileage_1 + mileage_2 + mileage_3
if mileage_amount > today:
    print('Сброс.')
    mileage = 0
    print(f'Пробег: {mileage}')
else:
    print('Сегодня не сломался.')
    print(f'Пробег: {mileage}')
