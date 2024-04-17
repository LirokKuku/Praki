numbers = [2, 3, 4, 5, 40]
words = ['два', 'три', 'четыре', 'пять', 'сорок']

a = {}

for i in range(len(numbers)):
    a[words[i]] = numbers[i]

p = str(input()).split()

number = 0
for i in range(len(p)):
    for j in a:
        if j in p[i] and 'надцать' in p[i]:
            number += a[j] + 10
        elif j in p[i] and 'дцать' in p[i]:
            number += a[j] * 10
        elif j in p[i]:
            number += a[j]
print(number**0.5)