def ident_three_digits(_first, _second):
    for year in range(_first, _second + 1):
        a = year // 1000
        b = year // 100 % 10
        c = year // 10 % 10
        d = year % 10
        if (a == b == c) or (a == c == d) or (a == b == d) or (b == c == d):
            print(year)


first = int(input('Введите первый год: '))
second = int(input('Введите второй год: '))

print(f'Года от {first} до {second} с тремя одинаковыми цифрами:')
ident_three_digits(first, second)

