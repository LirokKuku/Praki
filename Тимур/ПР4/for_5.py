import sys

n = int(input())

maxx = -sys.maxsize - 1
minn = sys.maxsize
for i in range(n):
    a = int(input())
    if a > 0:
        minn = min(minn, a)
    elif a < 0:
        maxx = max(maxx, a)
if maxx == -sys.maxsize - 1:
    print("Макс. отр. отсутсвует")
elif minn == sys.maxsize:
    print("Мин. пол. отсутсвует")
else:
    print("Макс. отр.", maxx)
    print("Мин. пол.", minn)