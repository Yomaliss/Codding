boys = int(input('Введите число мальчиков: '))
girls = int(input('Введите число девочек: '))
boy = 'B'
girl = 'G'
comb = ''
total = boys + girls
check = True


if boys > girls * 2 or girls > boys * 2:
    print('Ответ: Нет решения')
elif boys > girls:
    for x in range(1, total + 1, 2):
        if girls > 0 and boys > 0:
            comb += boy + girl + boy
            girls -= 1
            boys -= 2
elif girls > boys:
    for x in range(1, total + 1, 2):
        if girls > 0 and boys > 0:
            comb += girl + boy + girl
            girls -= 2
            boys -= 1
elif girls == boys:
    for x in range(1, total + 1, 2):
        comb += girl + boy
else:
    check = False
    print('Данные условия невозможны')

if check:
    print(f'Ответ: {comb}')
