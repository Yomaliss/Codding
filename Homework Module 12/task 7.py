def min_number(f_numb, s_numb):
    print(((s_numb + f_numb) - abs(s_numb - f_numb)) / 2)


first_number = int(input('Введите первое число: '))
second_number = int(input('Введите второе число: '))
min_number(first_number, second_number)
