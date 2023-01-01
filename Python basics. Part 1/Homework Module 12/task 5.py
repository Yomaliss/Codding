def count_letters(textual):
    count_letter = 0
    count_number = 0
    letter = input('Какую букву ищем? ')
    number = input('Какую цифру ищем? ')
    for symbol in textual:
        if symbol == letter.lower():
            count_letter += 1
        elif symbol == number:
            count_number += 1
    print(f'Количество букв {letter}: {count_letter}\n'
          f'Количество цифр {number}: {count_number}')


text = input('Введите текст: ')
count_letters(text)
