def calculator():
    number = int(input('Введите число: '))
    action = input('Введите действие, где:\n'
                   'min - минимальная цифра в числе\n'
                   'max - максимальная цифра в числе\n'
                   'amount - сумма цифр в числе\n')
    if action.lower() == 'min':
        minimum(number)
    elif action.lower() == 'max':
        maximum(number)
    elif action.lower() == 'amount':
        amount(number)
    else:
        print('Неверно введено действие.')


def minimum(number):
    min_number = 9
    while number != 0:
        if min_number > number % 10:
            min_number = number % 10
        number //= 10
    print(f'Минимальная цифра в числе - {min_number}')


def maximum(number):
    max_number = 0
    while number != 0:
        if max_number < number % 10:
            max_number = number % 10
        number //= 10
    print(f'Максимальная цифра в числе - {max_number}')


def amount(number):
    summa = 0
    while number != 0:
        summa += number % 10
        number //= 10
    print(f'Максимальная цифра в числе - {summa}')


while True:
    calculator()
