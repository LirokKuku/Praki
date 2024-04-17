lane = [1]
names = []
products = []
quantity = []
while len(lane) != 0:
    lane = str(input()).split()
    if len(lane) == 0:
        break
    else:
        names.append(lane[0])
        products.append(lane[1])
        quantity.append(int(lane[2]))
print(names)
print(products)
print(quantity)
names_set = set(names)
products_set = set(products)
pacifier = {}
for i in names_set:
    k = 0
    for j in names:
        if j in i:
            if