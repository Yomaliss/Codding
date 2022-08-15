def max_common_div(f_numb, s_numb):
    max_com_div = 1
    if s_numb < f_numb:
        s_numb, f_numb = f_numb, s_numb
    for number in range(1, s_numb + 1):
        if s_numb % number == 0 and f_numb % number == 0:
            max_com_div = number
    print(f'Наибольший делитель чисел {f_numb} и {s_numb} это {max_com_div} ')


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
max_common_div(first_number, second_number)
