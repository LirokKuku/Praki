import matplotlib.pyplot as plt

# a) y = x ** 2 - 1;
# б) y = x ** 2 - 8 * x + 15;
# в) -2 * x ** 2 + 4 * x;

list_x = []
list_y = []

# A
# for i in range(0, 100 + 1, 5):
#     list_x.append(i)
#     list_y.append(i ** 2 - 1)
#
# Б
# for i in range(0, 100 + 1, 5):
#     list_x.append(i)
#     list_y.append(i ** 2 - i * 8 + 15)
# В
# for i in range(0, 100 + 1, 5):
#     list_x.append(i)
#     list_y.append(- 2 * i ** 2 + i * 4)
plt.plot(list_x, list_y, 'g.-')
plt.show()