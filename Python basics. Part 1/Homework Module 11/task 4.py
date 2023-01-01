import math


number = float(input('Введите число: '))


print(round((math.floor(math.floor(number * 10) / 10) - (math.floor(number * 10) / 10)) * -10))
