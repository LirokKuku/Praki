import matplotlib.pyplot as plt
import json

months_dict = {
    1: "Январь",
    2: "Февраль",
    3: "Март",
    4: "Апрель",
    5: "Май",
    6: "Июнь",
    7: "Июль",
    8: "Август",
    9: "Сентябрь",
    10: "Октябрь",
    11: "Ноябрь",
    12: "Декабрь"
}

name = input()

with open('3.json', 'r') as file:
    data = json.load(file)

data = data['Договара']


list_x = list()
list_y = list()

for dictt in data:
    if name in dictt.values():
        data = dictt.get('Выплаты')
        for zp in data:
            list_x.append(int(zp.get('Размер выплаты')))
            list_y.append(months_dict.get(int(zp.get('Месяц'))))
        break
if len(list_x) == 0:
    print("Нет тут такого, ищите в другом месте")
else:
    plt.bar(list_y, list_x, width=0.4, color='green', edgecolor='black')
    plt.xlabel('Зарплата')
    plt.ylabel('Месяц')
    plt.title("ЗП" + ' ' + name)
    plt.show()