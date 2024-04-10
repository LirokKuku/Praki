import matplotlib.pyplot as plt
import json

with open('3.json', 'r', encoding="UTF-8") as file:
    data = json.load(file)

data = data['Договара']

list_one = list()
list_x = list()
name = list()

for dictt in data:
    data = dictt.get('Выплаты')
    for zp in data:
        list_one.append(int(zp.get('Размер выплаты')))
    list_x.append(sum(list_one) / len(list_one))
    list_one = list()
    name.append(dictt.get("ФИО"))

plt.pie(list_x, labels = name)
plt.show()