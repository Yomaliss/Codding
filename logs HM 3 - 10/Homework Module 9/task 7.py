text = input('Введите текст: ') + ' '
count_current = 0
count_maximum = 0


for letters in text:
    if letters != ' ':
        for _letter in letters:
            count_current += 1
    elif letters == ' ' or letters == '':
        if count_current > count_maximum:
            count_maximum = count_current
        count_current = 0

print(f'Самая длинная последовательность: {count_maximum}')
