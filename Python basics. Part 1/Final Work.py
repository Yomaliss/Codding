# MyProfile app

SEPARATOR = '------------------------------------------'

# user profile
name = ''
age = 0
phone_number = ''
email = ''
index = ''
address = ''
add_info = False
# entrepreneur information
psrnsp = ''
itn = ''
bank_account = ''
name_bank = ''
bic = ''
corr_account = ''


def menu(variable):    # main function
    print(f'{SEPARATOR}')
    if variable == 'main menu':
        print('ГЛАВНОЕ МЕНЮ\n'
              '1 - Ввести или обновить информацию\n'
              '2 - Вывести информацию\n'
              '0 - Завершить работу')
    elif variable == 'submenu 1':
        print('ВВЕСТИ ИЛИ ОБНОВИТЬ ИНФОРМАЦИЮ\n'
              '1 - Личная информация\n'
              '2 - Информация о предпринимателе\n'
              '0 - Назад')
    elif variable == 'submenu 2':
        print('ВЫВЕСТИ ИНФОРМАЦИЮ\n'
              '1 - Личная информация\n'
              '2 - Вся информация\n'
              '0 - Назад')


def general_info_user(n_parameter, a_parameter, ph_parameter, e_parameter, index_parameter, address_parameter,
                      i_parameter):   # main function
    print(f'SEPARATOR'
          f'Имя: {n_parameter}')
    if 11 <= a_parameter % 100 <= 19:
        years_parameter = 'лет'
    elif a_parameter % 10 == 1:
        years_parameter = 'год'
    elif 2 <= a_parameter % 10 <= 4:
        years_parameter = 'года'
    else:
        years_parameter = 'лет'

    print(f'Возраст: {a_parameter} {years_parameter}\n'
          f'Телефон: {ph_parameter}\n'
          f'E-mail: {e_parameter}\n'
          f'Индекс: {index_parameter}\n'
          f'Адрес: {address_parameter}')

    if add_info:
        print('\nДополнительная информация:\n'
              f'{i_parameter}')


def entrepreneur_info_user(psrnsp_parameter, itn_parameter, bank_account_parameter, name_bank_parameter, bic_parameter,
                           corr_account_parameter):   # main function
    print('Информация о предпринимателе'
          f'ОГРНИП: {psrnsp_parameter}\n'
          f'ИНН: {itn_parameter}\n'
          'Банковские реквизиты\n'
          f'Расчётный счёт: {bank_account_parameter}\n'
          f'Название банка: {name_bank_parameter}\n'
          f'БИК: {bic_parameter}\n'
          f'Корреспондентский счёт: {corr_account_parameter}\n')


def get_user_info(option_value):   # main function
    if option_value == 1:
        _name = input('Введите имя: ')
        _age = validate_user_age(int(input('Введите возраст: ')))
        _phone_number = correct_uph(input('Введите номер телефона (+7ХХХХХХХХХХ): '))
        _email = input('Введите адрес электронной почты: ')
        _index = only_digits(input('Введите почтовый индекс: '))
        _address = input('Введите почтовый адрес (без индекса): ')
        _add_info = input('Введите дополнительную информацию:\n')
        return _name, _age, _phone_number, _email, _index, _address, _add_info

    elif option_value == 2:
        _psrnsp = checking_digits('psrnsp')
        _itn = input('Введите ИНН: ')
        _bank_account = checking_digits('bank_account')
        _name_bank = input('Введите название банка: ')
        _bic = input('Введите БИК: ')
        _corr_account = input('Введите корреспондентский счет: ')
        return _psrnsp, _itn, _bank_account, _name_bank, _bic, _corr_account


def correct_uph(variable):   # auxiliary function
    _phone_number = ''
    for sign in variable:
        if sign == '+' or ('0' <= sign <= '9'):
            _phone_number += sign
    return _phone_number


def checking_digits(variable):   # auxiliary function
    if variable == 'psrnsp':
        digits = 15
        name_variable = 'ОГРНИП'
    elif variable == 'bank_account':
        digits = 20
        name_variable = 'Расчётный счёт'
    while True:
        variable = input(f'Введите {name_variable}: ')

        if len(variable) == digits and variable.isdigit():
            break
        else:
            print(f' {name_variable} должен содержать {digits} цифр')

    return variable


def only_digits(variable):   # auxiliary function
    variable = int(''.join(x for x in variable if x.isdigit()))
    return variable


def validate_user_age(_age):
    while _age <= 0:
        print('Возраст должен быть положительным')
        _age = int(input('Введите возраст: '))
        if _age > 0:
            break
    return _age


print('Приложение MyProfile'
      'Сохраняй информацию о себе и выводи ее в разных форматах')

while True:
    # main menu
    menu('main menu')

    option = int(input('Введите номер пункта меню: '))
    if option == 0:
        break

    if option == 1:
        # submenu 1: edit info
        while True:
            menu('submenu 1')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                # input general info
                name, age, phone_number, email, index, address, add_info = get_user_info(option2)

            elif option2 == 2:
                # input entrepreneur information
                psrnsp, itn, bank_account, name_bank, bic, corr_account = get_user_info(option2)

            else:
                print('Введён некорректный пункт меню')
    elif option == 2:
        # submenu 2: print info
        while True:
            menu('submenu 2')

            option2 = int(input('Введите номер пункта меню: '))
            if option2 == 0:
                break
            if option2 == 1:
                general_info_user(name, age, phone_number, email, index, address, add_info)

            elif option2 == 2:
                general_info_user(name, age, phone_number, email, index, address, add_info)
                entrepreneur_info_user(psrnsp, itn, bank_account, name_bank, bic, corr_account)
            else:
                print('Введён некорректный пункт меню')
    else:
        print('Введён некорректный пункт меню')
