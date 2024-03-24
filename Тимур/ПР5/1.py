import matplotlib.pyplot as plt

# a) y = x ** 2 - 1;
# б) y = x ** 2 - 8 * x + 15;
# в) y = -2 * x ** 2 + 4 * x;

list_x1 = []
list_y1 = []

# A
for i in range(0, 10 + 1, 1):
    list_x1.append(i)
    list_y1.append(i ** 2 - 1)
plt.plot(list_x1, list_y1, 'b.-')
del list_x1[:], list_y1[:]

# Б
for i in range(0, 10 + 1, 1):
    list_x1.append(i)
    list_y1.append(i ** 2 - i * 8 + 15)
plt.plot(list_x1, list_y1, 'r.-')
del list_x1[:], list_y1[:]

# В
for i in range(0, 10 + 1, 1):
    list_x1.append(i)
    list_y1.append(- 2 * i ** 2 + i * 4)
plt.plot(list_x1, list_y1, 'g.-')
plt.show()