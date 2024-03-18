a, b = int(input()), int(input())

while min(a, b) != 0:
    maxx = min(a, b)
    minn = max(a, b) % min(a, b)
    a, b = maxx, minn
print(max(a, b))