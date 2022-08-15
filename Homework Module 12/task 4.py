def opposite_number():
    while True:
        number = int(input('Введите число: '))
        opp_number = ''
        if number == 0:
            break
        while number != 0:
            if number % 10 != 0:
                opp_number += str(number % 10)
            number //= 10
        print(f'Число наоборот: {opp_number}')
    print('Программа завершена.')


opposite_number()
