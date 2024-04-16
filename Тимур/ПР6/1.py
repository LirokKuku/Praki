f = open('number.txt', 'r') # я решил создать файл с 30 значениями
fp = f.readlines()
n = 5
m = 6


list_n1 = list() # список Big (который снаружи)
list_m1 = list() # список Small (который внутри)

# тупо ходим по массиву
o = 0 - 6
h = 6 - 6


# создаём матрицу
for i in range(n):
    o += m
    h += m
    for j in range(o, h):
        list_m1.append(int(fp[j]))
    list_n1.append(list_m1)
    list_m1 = list()

# условние 1 и 2
nulli = []
for i in range(n):
    if 0 in list_n1[i]:
        nulli.append(i + 1)
        if list_n1.count(list_n1[i]) != 1:
            print("Тута есть дубликаты")
        else:
            print("Тута нет дубликатов")
print(*nulli)

# это для условния 3
list_n2 = list()

#транспонированная матрица
for i in range(m):
    list_m2 = list()
    for j in range(n):
        list_m2.append(list_n1[j][i])
    list_n2.append(list_m2)

# удаление строк
n_1 = int(input())
n_2 = int(input())
# for i in range(n):
#     for j in range(m):
#         if j + 1 == n_2:
#             list_n1[i].remove(list_n1[i][j])
# list_n1.remove(list_n1[n_1 - 1])

# вставка строки с столбцы
n_1 = int(input())
n_2 = int(input())
l_0 = [0 for x in range(m)]
for i in range(n + 1):
    if i + 1 == n_1:
        list_n1.insert(0, l_0)
    for j in range(m):
        if j + 1 == n_2:
            list_n1[i].insert(j, 0)