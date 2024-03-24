import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


# Функции для построения графиков
def func_a(x):
    return x ** 2 - 1


def func_b(x):
    return x ** 2 - 8 * x + 15


def func_c(x):
    return -2 * x ** 2 + 4 * x


# Обработчик нажатия кнопки "Построить график"
def plot_graph():
    function = combobox.get()
    start = int(entry_start.get())
    end = int(entry_end.get())
    step = 0.1
    x_values = [i * step for i in range(int(start * 10), int(end * 10))]

    plt.figure()
    plt.title("График функции " + function)

    if function == "y = x**2 - 1":
        plt.plot(x_values, [func_a(x) for x in x_values])
    elif function == "y = x**2 - 8*x + 15":
        plt.plot(x_values, [func_b(x) for x in x_values])
    elif function == "y = -2*x**2 + 4*x":
        plt.plot(x_values, [func_c(x) for x in x_values])

    plt.grid()
    plt.show()


# Создание графического интерфейса
root = Tk()
root.title("Построение графиков функций")
root.geometry("300x200")

functions = ["y = x**2 - 1", "y = x**2 - 8*x + 15", "y = -2*x**2 + 4*x"]
combobox = ttk.Combobox(root, values=functions)
combobox.pack(pady=5)

label_start = Label(root, text="Начало интервала X:")
label_start.pack()
entry_start = Entry(root)
entry_start.pack()

label_end = Label(root, text="Конец интервала X:")
label_end.pack()
entry_end = Entry(root)
entry_end.pack()

plot_button = Button(root, text="Построить график", command=plot_graph)
plot_button.pack(pady=10)

root.mainloop()