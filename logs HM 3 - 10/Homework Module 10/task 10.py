depth = int(input('Введите глубину ямы: '))
width = depth * 2
amount = width - 2
count = depth


for number in range(depth):
    count = depth
    for num in range(number + 1):
        print(count, end='')
        count -= 1
    print('.' * amount, end='')
    count = depth - number
    while count < depth + 1:
        print(count, end='')
        count += 1
    amount -= 2
    print()
