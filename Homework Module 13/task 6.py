startAmplitude = float(input('Введите начальную амплитуду: '))
endAmplitude = float(input('Введите амплитуду остановки: '))
count = 0

while startAmplitude > endAmplitude:
    count += 1
    startAmplitude -= (startAmplitude * 0.084)
print(f'Маятник считается остановившимся через {count} колебаний')