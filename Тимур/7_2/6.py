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

names_set = set(names)
products_set = set(products)
kkk_1 = {}
kkk_2 = {}

for i in names_set:
    dla_nas = {}
    k = 0
    for j in names:
        if j == i:
            if j not in kkk_1:
                dla_nas[products[k]] = quantity[k]
                kkk_1[names[k]] = dla_nas
            else:
                if products[k] in kkk_1[j]:
                    o = kkk_1[j]
                    o[products[k]] += quantity[k]
                else:
                    o = kkk_1[j]
                    o.update({products[k]:quantity[k]})
        k += 1

for i in products_set:
    dla_nas = {}
    k = 0
    for j in products:
        if j == i:
            if j not in kkk_2:
                dla_nas[names[k]] = quantity[k]
                kkk_2[products[k]] = dla_nas
            else:
                if names[k] in kkk_2[j]:
                    o = kkk_2[j]
                    o[names[k]] += quantity[k]
                else:
                    o = kkk_2[j]
                    o.update({names[k]:quantity[k]})
        k += 1

print('Товары:', *products_set)
print("Покупатели:", *names_set)
print("Товары покупателей",
    kkk_1, sep='\n')
print('Покупатели товара',
      kkk_2, sep='\n')