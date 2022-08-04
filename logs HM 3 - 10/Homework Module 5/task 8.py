square = int(input('Введите площадь: '))
price = int(input('Введите стоимость: '))
if square >= 100 and price <= 10000000:
    print('Эта квартира вам подходит.')
elif square >= 80 and price <= 7000000:
    print('Эта квартира вам подходит.')
else:
    print('Эта квартира вам не подходит.')
