from prettytable import PrettyTable

x = PrettyTable()
x.field_names = ["Месяц", "1 Банк", "2 Банк"]

data = [
]
sum_1 = 10**5
sum_2 = 10**5
b = sum_1
q = 0

mouth_12 = ""
mouth_24 = ""

for i in range(24):
    a = []
    a.append(i + 1)
    a.append(b + sum_1 * 0.011)
    a.append(sum_2 + sum_2 * 0.01)
    b += b + sum_1 * 0.011
    sum_2 += sum_2 + sum_2 * 0.01
    data.append(a)
    if i+1 == 12:
        if b > sum_2:
            q = 1
        else:
            q = 2
    elif i + 1 == 24:
        if b > sum_2:
            q = 1
        else:
            q = 2

j = 0
for i in range(2):
    j += 1
    if q == 1:
        print("1 Банк выгоднее на", j, 'год')
    else:
        print("2 Банк выгоднее на", j, 'год')
        
for row in data:
    x.add_row(row)

# Вывод таблицы
print(x)