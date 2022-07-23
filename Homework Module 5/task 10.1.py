hour = int(input('Введите время в часах: '))  # Число от 0 до 23
bad_hours = 14 <= hour <= 15 \
         or 10 <= hour <= 12 \
         or 18 <= hour <= 20
if 8 <= hour <= 22 and not bad_hours:
    print('Посылку можно забрать')
else:
    print('Посылку нельзя забрать')
