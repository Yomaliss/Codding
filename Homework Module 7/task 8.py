first_number = 10
last_number = 99


for number in range(first_number, last_number + 1):
    number_1 = number % 10
    number_2 = number // 10
    if 3 * number_1 * number_2 == number:
        print(f'Число {number} подходит по условиям')
