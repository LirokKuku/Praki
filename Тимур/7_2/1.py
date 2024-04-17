str_0 = 'мама папа мама сын дочь сын пиво и водка и водка'
q = str_0.split()
p = set(q)

list_1 = []
list_2 = []

for i in p:
    list_1.append(i)
    list_2.append(q.count(i))

for i in range(len(p)-1):
    for j in range(len(p)-1-i):
        if list_2[j] > list_2[j + 1]:
            list_2[j], list_2[j + 1] = list_2[j + 1], list_2[j]
            list_1[j], list_1[j + 1] = list_1[j + 1], list_1[j]

list_1.reverse()
list_2.reverse()

a = {}

for i in range(len(list_1)):
    a[list_1[i]] = list_2[i]
print(a)