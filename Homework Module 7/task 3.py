months = 12
month = 0
month_count = 0
salary_total = 0


for month in range(1, 12 + 1):
    month_count += 1
    salary = int(input(f'Введите зарплату за {month_count} месяц: \n \
'))
    salary_total += salary


average_salary = salary_total // month_count

print(f'Средняя зарплата за год - {average_salary}')
