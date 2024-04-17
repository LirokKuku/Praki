str_1 = "яблоки, груши, яблоки, киви, сливы, киви"

f = str_1.split(', ')

list_1 = set(f)

a = {}
for i in list_1:
    a[i] = f.count(i)

maxx = max(a.values())

print(*[i for i in a if a[i] == maxx])