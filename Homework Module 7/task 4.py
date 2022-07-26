peoples_limit = 10
first_sector = 30
last_sector = 35
sector = 0
n_violations = 0


for sector in range(first_sector - 1, last_sector):
    sector += 1
    peoples = int(input(f'Людей в {sector} секторе: '))
    if peoples > peoples_limit:
        n_violations += 1
        print('Нарушение! Слишком много людей в секторе!')
    else:
        print('Все спокойно')


print(f'Количество нарушений = {n_violations}')
