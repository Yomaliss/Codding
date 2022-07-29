current_x = 8
current_y = 10
begin_limit_x, begin_limit_y = 0, 0
last_limit_x, last_limit_y = 15, 20


print('Введите сторону света, куда переместится марсоход: \n'
      'W - север \n'
      'S - юг \n'
      'A - запад \n'
      'D - восток \n'
      'exit - выйти')

while True:
    print(f'[Программа]: Марсоход находится на позиции {current_x}, '
          f'{current_y}, введите команду: ')
    command = input('[Оператор] ')
    if command.lower() == 'w':
        if current_y == last_limit_y:
            current_y = last_limit_y
            continue
        current_y += 1
    elif command.lower() == 's':
        if current_y == begin_limit_y:
            current_y = begin_limit_y
            continue
        current_y -= 1
    elif command.lower() == 'a':
        if current_x == begin_limit_x:
            current_x = begin_limit_x
            continue
        current_x -= 1
    elif command.lower() == 'd':
        if current_x == last_limit_x:
            current_x = last_limit_x
            continue
        current_x += 1
    elif command.lower() == 'exit':
        print('Программа завершена!')
        break
    else:
        print('Введённая команда не существует')

print(f'[Программа]: Конечная позиция Марсохода: {current_x}, {current_y}.')
