summ = 0
pr = 1
for i in range(5):
    a = int(input())
    print(a)
    summ += a
    pr *= a
print("Сумма:", summ)
print("Произведение:", pr)
print("Среднее значение:", summ/5)