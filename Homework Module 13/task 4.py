startNumber = float(input('Введите число в экспоненциальной форме: '))
mantissa = startNumber
order = 0
while not 1 <= mantissa < 10:
    order += 1
    mantissa /= 10
print(f'Мантисса числа {startNumber} - {mantissa}, а порядок - {order}')

