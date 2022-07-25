plus = 0
minus = 0


while True:
    number = int(input('Введите оценку: '))
    if 0 < number <= 100:
        print('Положительный отзыв записан.')
        plus += 1
    elif 0 > number >= -100:
        print('Отрицательный отзыв записан.')
        minus += 1
    elif number == 0:
        print('Подсчет отзывов закончен.')
        break
    else:
        print('Данной оценки не существует')


print(f'Количество отрицательных отзывов: {minus} \n \
        Количество положительных отзывов: {plus}')
