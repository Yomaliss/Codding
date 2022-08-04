size_letter = int(input('Введите одну из сторон письма: '))
size_envelope = 12
n = 0


if size_letter <= size_envelope:
    print('Письмо входит в конверт')
else:
    while True:
        n += 1
        if size_letter >= size_envelope:
            size_letter //= 2
            print(f'Складываем письмо пополам \n \
Текущий размер стороны письма: {size_letter}')
        else:
            print('Письмо входит в конверт')
            break

print(f'Письмо пришлось сложить {n} раз')
