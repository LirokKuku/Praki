a = str(input()).split(", ")
b = {}
for i in range(len(a)):
    b[a[i]] = "номер", i+1, "в строке"
print(b)