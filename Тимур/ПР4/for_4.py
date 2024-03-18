import sys

n = int(input())

minn = sys.maxsize
for i in range(n - 1):
    a = int(input())
    if a % 2 != 0:
        minn = min(minn, a)
print(minn)