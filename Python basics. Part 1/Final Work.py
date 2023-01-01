# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
n = ''
a = 0
ph = ''
e = ''
i = ''
# social links
v = ''
t = ''
tk = ''


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, index_parameter, address_parameter,
                      i_parameter):
    print(SEPARATOR)
    print('Имя:    ', n_parameter)
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print('Возраст:', a_parameter, years_parameter)
    print('Телефон:', ph_parameter)
    print('E-mail: ', e_parameter)
    print('Индекс: ', index_parameter)
    print('Адрес:', address_parameter)

    if i:
        print('')
        print('Дополнительная информация:')
        print(i_parameter)


print('Приложение MyProfile')
print('Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    print(SEPARATOR)
    print('ГЛАВНОЕ МЕНЮ')
    print('1 - Ввести или обновить информацию')
    print('2 - Вывести информацию')
    print('0 - Завершить работу')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            print(SEPARATOR)
            print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Информация о предпринимателе')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                n = input('Введите имя: ')
                while 1:
                    # validate user age
                    a = int(input('Введите возраст: '))
                    if a > 0:
                        break
                    print('Возраст должен быть положительным')

                uph = input('Введите номер телефона (+7ХХХХХХХХХХ): ')
                ph = ''
                for ch in uph:
                    if ch == '+' or ('0' <= ch <= '9'):
                        ph += ch

                e = input('Введите адрес электронной почты: ')
                index = input('Введите почтовый индекс: ')

                index = int(''.join(i for i in index if i.isdigit()))   # numbers from a string

                address = input('Введите почтовый адрес (без индекса): ')
                i = input('Введите дополнительную информацию:\n')

            elif option2 == 2:
                # input social links
                while True:   # PSRNSP, checking 15 digits
                    PSRNSP = input('Введите ОГРНИП: ')
                    if len(PSRNSP) == 15 and PSRNSP.isdigit():
                        break
                    else:
                        print('ОГРНИП должен содержать 15 цифр')

                ITN = input('Введите ИНН: ')

                while True:   # bank account, checking 20 digits
                    bankAccount = input('Введите расчётный счёт: ')
                    if len(bankAccount) == 20 and bankAccount.isdigit():
                        break
                    else:
                        print('Расчётный счёт должен содержать 20 цифр')

                nameBank = input('Введите название банка: ')
                BIC = input('Введите БИК: ')
                corrAccount = input('Введите корреспондентский счет: ')

            else:
                print('Введён некорректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            print(SEPARATOR)
            print('ВЫВЕСТИ ИНФОРМАЦИЮ')
            print('1 - Личная информация')
            print('2 - Вся информация')
            print('0 - Назад')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(n, a, ph, e, index, address, i)

            elif option2 == 2:
                general_info_user(n, a, ph, e, index, address, i)

                # print social links
                print('Информация о предпринимателе')
                print(f'ОГРНИП: {PSRNSP}')
                print(f'ИНН: {ITN}')
                print('Банковские реквизиты')
                print(f'Расчётный счёт: {bankAccount}')
                print(f'Название банка: {nameBank}')
                print(f'БИК: {BIC}')
                print(f'Корреспондентский счёт: {corrAccount}')
            else:
                print('Введён некорректный пункт меню')
    else:
        print('Введён некорректный пункт меню')
