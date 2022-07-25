name = input('Введите имя: ')
amount = int(input('Введите сумму долга: '))
payment = 0


while payment < amount:
    payment = int(input('Сколько рублей вы внесёте прямо сейчас, '
                        'чтобы её погасить? '))
    print(f'Внесено: {payment}')
    if payment < amount:
        print(f'Маловато {name}. Давайте ещё раз.')


print(f'Отлично, {name}! Вы погасили долг. Спасибо!')
