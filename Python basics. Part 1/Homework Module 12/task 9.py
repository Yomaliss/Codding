def mainMenu():
    choose = input('Введите rps, если хотите сыграть в "Камень, ножницы, бумага"\n'
                   'Введите gtn, если хотите сыграть в "Угадай число"\n'
                   'Введите quit, если хотите выключить игру.\n')
    if choose.lower() == 'rps':
        rock_paper_scissors()
    elif choose.lower() == 'gtn':
        guess_the_number()
    elif choose.lower() == 'quit':
        print('Завершение работы...')
    else:
        print('Повторите попытку ввода\n')
        mainMenu()


def rock_paper_scissors():
    print('Камень, ножницы, бумага...\n'
          'Введите результаты, где:\n'
          'rock - камень\n'
          'scissors - ножницы\n'
          'paper - бумага\n')
    first_player = input('Первый игрок: Камень, ножницы или бумага? ')
    second_player = input('Второй игрок: Камень, ножницы или бумага? ')
    if first_player.lower() == 'rock' and second_player.lower() == 'scissors' or \
            first_player.lower() == 'paper' and second_player.lower() == 'rock' or \
            first_player.lower() == 'scissors' and second_player.lower() == 'paper':
        print('Первый игрок побеждает!\n')
    elif second_player.lower() == 'rock' and first_player.lower() == 'scissors' or \
            second_player.lower() == 'paper' and first_player.lower() == 'rock' or \
            second_player.lower() == 'scissors' and first_player.lower() == 'paper':
        print('Второй игрок побеждает!\n')
    elif second_player.lower() == 'rock' and first_player.lower() == 'rock' or \
            second_player.lower() == 'paper' and first_player.lower() == 'paper' or \
            second_player.lower() == 'scissors' and first_player.lower() == 'scissors':
        print('Ничья!\n')
    else:
        print('Неверные данные, повторите попытку ввода\n')
        rock_paper_scissors()
    mainMenu()


def guess_the_number():
    hidden_number = int(input('Введите загаданное число. '))
    number = ''
    while hidden_number != number:
        number = int(input('Введите число: '))
        if number < hidden_number:
            print('Загаданное число больше!\n')
        elif number > hidden_number:
            print('Загаданное число меньше!\n')
    print('Вы угадали число!\n')


mainMenu()
pass
