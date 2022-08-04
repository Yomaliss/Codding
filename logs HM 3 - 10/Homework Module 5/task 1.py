exp = int(input('Введите число опыта: '))
if 0 <= exp < 1000:
    level = 1
    print(f'Ваш уровень: {level}')
elif 1000 <= exp < 2500:
    level = 2
    print(f'Ваш уровень: {level}')
elif 2500 <= exp < 5000:
    level = 3
    print(f'Ваш уровень: {level}')
elif exp >= 5000:
    level = 4
    print(f'Ваш уровень: {level}')
else:
    print('Значение не может быть отрицательным')
