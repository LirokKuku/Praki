a = str(input()).split(",")
b = {}
for i in range(len(a)):
    b[a[i]] = "номер " + str(i+1) + " в строке"
print(b)