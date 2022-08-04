lower_bound_c = int(input('Введите нижнюю границу: '))
upper_bound_c = int(input('Введите верхнюю границу: '))
step_c = int(input('Введите шаг: '))


print(f'C \t F')

for current_c in range(lower_bound_c, upper_bound_c + step_c, step_c):
    if current_c == lower_bound_c:
        print(f'{lower_bound_c}\t{32}')
        continue
    elif current_c > upper_bound_c:
        current_c = upper_bound_c
    print(f'{current_c}\t{round(current_c * 1.8 + 32)}')
