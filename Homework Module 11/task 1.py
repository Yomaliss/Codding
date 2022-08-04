euro = float(input('Введите стоимость покупки в евро: '))
euro_dollar = 1.25
dollar_ruble = 60.87


print(f'Стоимость покупки в рублях: {round(euro * euro_dollar * dollar_ruble, 2)}')
