a = [[1, 2], [3, 4, 4, 3, 1], [4, 1, 4, 5]]

long = []

for i in a:
    long.append(len(i))

for k in range(len(a)):
    if long[k] > 3:
        for j in range(3, len(a[k])):
            a[k][2] += a[k][j]
        a[k] = a[k][0:3]
print(a)