def reverse_number(_number):      # Переворачивание числа
    reversed_number = 0
    while _number > 0:
        temp = _number % 10
        reversed_number = reversed_number * 10 + temp
        _number = _number // 10
    return reversed_number


number_N = int(input('Введите число N: '))
number_K = int(input('Введите число K: '))
amount = reverse_number(reverse_number(number_N) + reverse_number(number_K))   # Переворот суммы перевернутых N и K
print(amount)
