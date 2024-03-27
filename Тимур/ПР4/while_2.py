import sys

k = 0
a = 1
summ = 0
maxx = -sys.maxsize - 1
minn = sys.maxsize

while a != 0:
        a = float(input())
        if a == 0:
            break
        else:
            maxx = max(maxx, a)
            minn = min(minn, a)
            summ = summ + a
            k += 1
print("Количество чисел:", k)
print("Максимальное число:", maxx)
print("Минимальное число:", minn)
print("Сумма:", summ)
print("Среднее значение:", summ/k)