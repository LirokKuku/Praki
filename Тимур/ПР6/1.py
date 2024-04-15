f = open('number.txt', 'r') # я решил создать файл с 30 значениями
fp = f.readlines()
n = 5
m = 6


list_n = list() # список Big (который снаружи)
list_m = list() # список Small (который внутри)

# тупо ходим по массиву
o = 0 - 6
h = 6 - 6

# создаём матрицу
for i in range(n):
    o += m
    h += m
    print(o, h)
    for j in range(o, h):
        list_m.append(int(fp[j]))
    list_n.append(list_m)
    list_m = list()

nulli = []
for i in range(n):
    if 0 in list_n[i]:
        nulli.append(i + 1)
        if list_n.count(list_n[i]) != 1:
            print("Тута есть дубликаты")
        else:
            p