def annuityPayment(_percent, _years):
    t = (1 + _percent) ** _years
    _annuity = _percent * t / (t - 1)
    return _annuity


def periodPayment(_creditSum, _percent, _annuity, _periodNum):
    loanBody = annuity - _creditSum * _percent
    print(f'\nПериод: {_periodNum}\n'
          f'Остаток долга на начало периода: {_creditSum:.2f}\n'
          f'Выплачено процентов: {_creditSum * _percent:.2f}\n'
          f'Выплачено тело кредита: {loanBody:.2f}')
    return _creditSum - loanBody


creditSum = float(input('Введите сумму кредита: '))
percent = int(input("Сколько процентов годовых? ")) / 100
years = int(input('На сколько лет выдан? '))
annuity = annuityPayment(percent, years) * creditSum

for periodNum in range(1, 4):
    creditSum = periodPayment(creditSum, percent, annuity, periodNum)

print(f'\nОстаток долга: {creditSum:.2f}\n'
      f'\n====================\n')

years = int(input('На сколько лет продлевается договор? ')) + years - 3
percent = int(input('Увеличение ставки до: ')) / 100
annuity = annuityPayment(percent, years) * creditSum

for periodNum in range(1, years + 1):
    creditSum = periodPayment(creditSum, percent, annuity, periodNum)

print(f'\nОстаток долга: {creditSum:.2f}')
