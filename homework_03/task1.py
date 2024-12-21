# В базе магазина электроники есть список видеокарт компании NVIDIA разных
# поколений. Вместо полных названий хранятся только числа, которые обозначают
# модель и поколение видеокарты. Недавно компания выпустила новую линейку
# видеокарт. Самые старшие поколения разобрали за пару дней.
# Напишите программу, которая удаляет наибольшие элементы из списка видеокарт.
# Пример:
# Количество видеокарт: 5
# Видеокарта 1: 3070
# Видеокарта 2: 2060
# Видеокарта 3: 3090
# Видеокарта 4: 3070
# Видеокарта 5: 3090
# Старый список видеокарт: [ 3070 2060 3090 3070 3090 ]
# Новый список видеокарт: [ 3070 2060 3070 ]

videoСardsNumber = int(input('Введите количество видеокарт: '))
videoСards = []
newVideoCardsList = []
maxItem = 0

for item in range(videoСardsNumber):
    videoСards.append(int(input(f'Видеокарта {item + 1}: ')))
    if videoСards[item] > maxItem:
        maxItem = videoСards[item]
for item in range(videoСardsNumber):
    if videoСards[item] != maxItem:
        newVideoCardsList.append(videoСards[item])

print()
print('Старый список видеокарт: [', end=' ')
for item in range(videoСardsNumber):
    print(videoСards[item], end=' ')
print(']')

print('Новый список видеокарт: [', end=' ')
for item in range(len(newVideoCardsList)):
    print(newVideoCardsList[item], end=' ')
print(']')
