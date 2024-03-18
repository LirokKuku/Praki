import math
def sin(x):
    return math.sin(x)

a, b = float(input()), float(input())

while a <= b:
    print(round(a, 2), round(sin(a), 2))
    a += 0.1