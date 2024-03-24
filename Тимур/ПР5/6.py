import matplotlib.pyplot as plt
import json

with open('3.json', 'r') as file:
    data = json.load(file)

data = data['Договара']

name = list()
list_max = list()
list_min = list()
list_dummy = list()

for dictt in data:
    data = dictt.get('Выплаты')
    for zp in data:
        list_dummy.append(int(zp.get('Размер выплаты')))
    list_max = max(list_dummy)
    list_min = min(list_dummy)
    list_dummy = list()
    name.append(dictt.get("ФИО"))

# 3
width = 0.4
plt.bar([x-width/2 for x in range(3)], list_max, width, color='green', edgecolor = 'black')
plt.bar([x+width/2 for x in range(3)], list_min, width, color='red', edgecolor = 'black')
plt.xticks([x for x in range(3)], name)
plt.xlabel('Сотрудники')
plt.ylabel('Зароботная плата max/min')
plt.show()