students = int(input('Введите число учеников: '))
five = 0
four = 0
three = 0


for number in range(1, students + 1):
    x = int(input('Введите оценку: '))
    if x == 5:
        five += 1
    elif x == 4:
        four += 1
    elif x == 3:
        three += 1
    else:
        print('Такой оценки не существует или такая оценка не была получена')

if five > four and five > three:
    print('Больше всего в классе отличников')
elif four > five and four > three:
    print('Больше всего в классе хорошистов')
elif three > five and three > four:
    print('Больше всего в классе троечников')
else:
    print('Количество отличников, хорошистов и троечников должно быть различно. '
          'Проверьте введённую информацию ')
