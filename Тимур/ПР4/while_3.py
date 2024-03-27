import sys

a = ''
p = 0

minn = sys.maxsize

while '.' not in a:
    a = input()
    if '.' in a and a.index('.') == 0:
        break
    elif '.' in a:
        p = int(a[:a.index('.'):])
        if p > 0:
            minn = min(p, minn)
    else:
        p = int(a)
        if p > 0:
            minn = min(minn, p)
print(minn)