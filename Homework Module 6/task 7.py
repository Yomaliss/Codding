work = 8
work_current = 0
tasks_total = 0
wife_true = False


print('Начался 8-и часовой рабочий день')
while work_current < work:
    work_current += 1
    print(f'{work_current} час')
    tasks_total += int(input('Сколько задач решит Максим? '))
    wife = int(input('Звонит жена. Взять трубку? (1 — да, 0 — нет): '))
    if wife == 1:
        wife_true = True


print(f'Рабочий день закончился. Всего выполнено задач: {tasks_total} ')

if wife_true:
    print('Нужно зайти в магазин.')
