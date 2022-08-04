bank = int(input('Введите начальное состояние вклада: '))
percents = int(input('Введите проценты вклада: '))
bank_last = int(input('Введите конечное состояние вклада: '))
years = 0


while bank <= bank_last:
    bank += int(bank * percents / 100)
    years += 1


print(f'Сумма в размере {bank} у вас накопиться за {years} лет')
