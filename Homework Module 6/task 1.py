number = int(input('Введите число: '))
start_number = 0


while start_number <= number:
    start_number += 1
    current_number = start_number
    start_number **= 3
    print(start_number)
    start_number = current_number
