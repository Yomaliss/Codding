x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
if x > y:
    if x > z:
        print(f'{x} - большее число')
    else:
        print(f'{z} - большее число')
else:
    if y > z:
        print(f'{y} - большее число')
    else:
        print(f'{z} - большее число')
