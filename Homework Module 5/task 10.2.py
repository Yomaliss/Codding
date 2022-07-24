hour = int(input('Введите время в часах: '))
if 14 <= hour < 15 \
        or 10 <= hour < 12 \
        or 18 <= hour < 20 \
        or 0 <= hour < 8 \
        or 22 <= hour <= 23:
    print('Посылку нельзя забрать')
else:
    print('Посылку можно забрать')
