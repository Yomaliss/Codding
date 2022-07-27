begin_segment = int(input('Введите начало отрезка: '))
last_segment = int(input('Введите конец отрезка: '))
step = int(input('Введите шаг: '))
x = 0


if begin_segment > last_segment:
    begin_segment, last_segment = last_segment,  begin_segment
if step < 0:
    step = -step

for x in range(begin_segment, last_segment + 1, step):
    y = (x ** 3) + (2 * x ** 2) - 4 * x + 1
    print(f'В точке {x} функция равна {y}')
