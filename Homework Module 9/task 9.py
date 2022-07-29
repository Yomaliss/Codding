busy = input('Введите последовательность из 10 символов a и b, где \n'
             'a - свободное стойло \n'
             'b - занятое стойло \n')
milk_amount = 0
milk = 0
count = 0
check = True


for _counter in busy:
    count += 1
if count == 10:
    for busy_answer in busy:
        milk += 2
        if busy_answer.lower() == 'b':
            print(f'Стойло приносит {milk} литров молока')
            milk_amount += milk
        elif busy_answer.lower() == 'a':
            print('Стойло свободное')
        else:
            print('Данный символ не соответствует условиям')
            break
else:
    print('Неверное количество символов в последовательности.')
    check = False

if check:
    print(f'За день было произведено {milk_amount} литров молока')
