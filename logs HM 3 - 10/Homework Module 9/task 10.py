counter = 0
count = 0
unencrypted = input('Введите нерасшифрованное слово: ')


for _code in unencrypted:
    count += 1

for letters in unencrypted:
    counter += 1
    if counter in range(1, count + 1, 2):
        print(letters, end='')

for letters in reversed(unencrypted):
    if counter in range(0, count + 1, 2):
        print(letters, end='')
    counter -= 1
