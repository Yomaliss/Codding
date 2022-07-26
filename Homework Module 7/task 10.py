amount = 0
number = int(input('Введите число карточек: '))


for x in range(1, number + 1):
    amount += x

for x in range(1, number):
    amount -= int(input('Введите номер оставшейся карточки: '))
print(f'Номер потерянной карточки - {amount}')
