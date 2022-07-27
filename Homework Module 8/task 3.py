reverse_timer = int(input('Сколько секунд разогреваем? '))
check = True


for time in range(reverse_timer, 0, -1):
    print(f'До конца подогрева осталось: {time} секунд')
    command = int(input('Введите: \n \
1 - чтобы прервать режим разогрева \n \
0 - чтобы не прерывать режим разогрева \n \
Поле ввода: '))
    if command == 1:
        print(f'Таймер был прерван на {time} секунде \n \
Ваша еда готова, можете забрать.')
        check = False
        break

if check:
    print('Ваша еда готова, осторожно горячo.')
