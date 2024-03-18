k = 0
a = 1

while a != 0:
    a = float(input())
    maxx = max(maxx, a)
    minn = min(minn, a)
    summ = summ + a
    k += 1
print("Количество чисел:", k)
print("Максимальное число:", maxx)
print("Минимальное число:", minn)
print("Сумма:", summ)
print("Среднее значение:", summ/k)