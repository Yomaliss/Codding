heigth = int(input('Введите глубину ямы: '))
width = heigth * 2
amount = width - 2
count = heigth


for number in range(heigth):
    print(heigth, end='')
    count = heigth
    for num in range(number):
        count -= 1
        print(count, end='')
    print('.' * amount, end='')
    count = heigth - number
    while count < heigth:
        print(count, end='')
        count += 1
    print(heigth, end='')
    amount -= 2
    print()
