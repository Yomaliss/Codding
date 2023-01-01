def max_twoNumbers(_second_number, _first_number):
    _temp_number = ((abs(_second_number - _first_number) + _second_number + _first_number) / 2)
    return _temp_number


def max_threeNumbers(_first_number, _second_number, _third_number):
    _temp_number = max_twoNumbers(_second_number, _first_number)
    _max_number = ((abs(_temp_number - _third_number) + _temp_number + _third_number) / 2)
    return _max_number


answer = input('Максимум скольки чисел ищем? Двух или трёх? ')
max_number = 0
if answer.lower() == 'двух':
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    max_number = max_twoNumbers(second_number, first_number)
    print(f'Максимальное число из введённых - {max_number}')
elif answer.lower() == 'трёх' or answer.lower() == 'трех':
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    third_number = int(input('Введите третье число: '))
    max_number = max_threeNumbers(first_number, second_number, third_number)
    print(f'Максимальное число из введённых - {max_number}')
else:
    print('Ответ не распознан, попробуйте ещё раз!')