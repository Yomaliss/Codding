text = input('Введите текст: ')
count = 0


for number in text:
    count += 1
    if number == '*':
        print(f'Символ `*` стоит на позиции {count}')
