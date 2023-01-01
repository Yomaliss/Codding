import math


size = float(input('Введите размер файла для скачивания: '))
speed = float(input('Какова скорость вашего соединения? '))
time = 0
downloaded = 0


while downloaded < size:
    downloaded += speed
    if downloaded > size:
        downloaded = size
    time += 1
    print(f'Прошло {time} секунд. Скачано {downloaded} из {size} МБ ({math.ceil(downloaded / size * 100)}%)')

print('Загрузка завершена!')
