number = 0
n = 0


for number in (114, 12, 14, 10605, 4907, 450):
    if number % 2 == 0:
        if number % 3 != 0:
            print(f'Число {number} подходит')
        else:
            print(f'Число {number} не подходит.')
    else:
        print(f'Число {number} не подходит.')
