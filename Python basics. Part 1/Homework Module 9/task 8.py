length = int(input('Введите желаемую длину колонтитула: '))
importance = int(input('Сколько ! будет в колонтитуле? '))


check = True
if length % 2 == 0:
    check = False

side = (length - importance) // 2


for footer in range(1, side * 2 + 1):
    print('~', end='')
    if footer == side:
        for _footer_imp in range(1, importance + 1):
            print('!', end='')

if check:
    print('~')
