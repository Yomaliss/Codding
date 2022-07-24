hour = int(input('Введите время в часах: '))
if 8 <= hour < 22 and not \
        (14 <= hour < 15
         or 10 <= hour < 12
         or 18 <= hour < 20):
    print('Посылку можно забрать')
else:
    print('Посылку нельзя забрать')
