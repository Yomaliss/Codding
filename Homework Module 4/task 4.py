first_product = int(input('Введите стоимость первого товара: '))
second_product = int(input('Введите стоимость второго товара: '))
third_product = int(input('Введите стоимость третьего товара: '))
discount_after = 10000
total_amount = first_product + second_product + third_product
if first_product + second_product + third_product > discount_after:
    total_amount = total_amount - (total_amount * 10 / 100)
    print(f'Конечная цена: {total_amount}')
else:
    print(f'Конечная цена: {total_amount}')
