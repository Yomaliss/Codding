depth = int(input('Введите глубину ямы: '))
width = depth * 2
amount = width - 2
count = depth


for number in range(depth):
    print(depth, end='')
    count = depth
    for num in range(number):
        count -= 1
        print(count, end='')
    print('.' * amount, end='')
    count = depth - number
    while count < depth:
        print(count, end='')
        count += 1
    print(depth, end='')
    amount -= 2
    print()
