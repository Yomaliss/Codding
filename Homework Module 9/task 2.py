total_pass = 0


for _number_pirate in range(1, 10 + 1):
    answer = input('Введите фразу: ')
    if answer.lower() == 'Карамба':
        total_pass += 1

print(f'В ряды старого пирата присоединились {total_pass} пиратов')
