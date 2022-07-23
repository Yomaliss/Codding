guest_cube = int(input('Введите результат броска кубика Кости: '))
owner_cube = int(input('Введите результат броска кубика владельца: '))
amount = guest_cube + owner_cube
difference = guest_cube - owner_cube
if guest_cube >= owner_cube:
    print(f'Костя платит владельцу {difference * 1000}$')
else:
    print(f'Владелец платит Косте {-difference * 1000}$')
print('Игра окончена.')
