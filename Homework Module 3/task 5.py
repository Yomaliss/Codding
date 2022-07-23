minutes = int(input('Введите число минут: '))
full_hours = minutes // 60
print('Всего полных часов:', full_hours)
left_minutes = minutes % 60
print('От полного часа прошло:', left_minutes, 'минут')
