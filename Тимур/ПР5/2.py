import matplotlib.pyplot as plt

list_x = []
list_y = []

for i in range(-100, 100 + 1, 10):
    list_x.append(i)
    if i >= 1:
        list_y.append(i ** 2 - 6 * i + 10)
    elif i < 1:
        list_y.append(i + 2)
plt.plot(list_x,list_y,'g.-')
plt.show()