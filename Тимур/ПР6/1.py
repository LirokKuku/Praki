f = open('number.txt', 'r') # я решил создать файл с 30 значениями
fp = f.readlines()
n = 5
m = 6

list_n1 = list()
list_m1 = list()

o = 0 - 6
h = 6 - 6

for i in range(n):
    o += m
    h += m
    for j in range(o, h):
        list_m1.append(int(fp[j]))
    list_n1.append(list_m1)
    list_m1 = list()

nulli = []
for i in range(n):
    if 0 in list_n1[i]:
        nulli.append(i + 1)
print('Количетсво строк с нулями:', len(nulli))

list_n2 = list()

k = 0
for i in range(len(list_n1)):
    if list_n1.count(list_n1[i]) > 1:
         k += 1
print('Количество одинаковых строк:', int(k/2))

for i in range(m):
    list_m2 = list()
    for j in range(n):
        list_m2.append(list_n1[j][i])
    list_n2.append(list_m2)

n_1 = int(input())
n_2 = int(input())
print('Ввидите комманду:')
command = str(input())

def one(x_1, x_2):
    for i in range(n):
        for j in range(m):
            if j + 1 == x_2:
                list_n1[i].remove(list_n1[i][j])
    list_n1.remove(list_n1[x_1 - 1])
    return list_n1
def two(x_1, x_2):
    l_0 = [0 for x in range(m)]
    for i in range(n + 1):
        if i + 1 == x_1:
            list_n1.insert(0, l_0)
        for j in range(m):
            if j + 1 == x_2:
                list_n1[i].insert(j, 0)
    return list_n1

if command == '1':
    p = one(n_1, n_2)
    for i in list_n1:
        print(i)
elif command == "2":
    p = two(n_1, n_2)
    for i in list_n1:
        print(i)