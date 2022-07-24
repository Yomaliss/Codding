hour = int(input('Введите время в часах: '))
if 14 <= hour < 15 \
        or 10 <= hour < 12 \
        or 18 <= hour < 20:
    print('Посылку нельзя забрать')
else:
    print('Посылку можно забрать')
