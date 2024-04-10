import matplotlib.pyplot as plt
from tkinter import *
from tkinter import ttk


# Функции для построения графиков
def A(x):
    return x ** 2 - 1


def B(x):
    return x ** 2 - 8 * x + 15


def C(x):
    return -2 * x ** 2 + 4 * x


# Обработчик нажатия кнопки "Построить график"
def graph():
    function = combobox.get() #выносной список
    start = int(entry_start.get()) #считываение 1 значение
    end = int(entry_end.get())
    x_values = [i for i in range(start, end + 1)] #чё хотим прописываем, это для оси, для маштобирования соответсвенно

    if function == "y = x**2 - 1":
        plt.plot(x_values, [A(x) for x in x_values])
    elif function == "y = x**2 - 8*x + 15":
        plt.plot(x_values, [B(x) for x in x_values])
    elif function == "y = -2*x**2 + 4*x":
        plt.plot(x_values, [C(x) for x in x_values])

    plt.grid() # чтоб пизже было
    plt.show()


# Создание графического интерфейса
okno = Tk()
okno.title("Построение графиков функций")
okno.geometry("500x500")

functions = ["y = x**2 - 1", "y = x**2 - 8*x + 15", "y = -2*x**2 + 4*x"]
combobox = ttk.Combobox(okno, values=functions)
combobox.pack() #вывод кнопок(выгодно)

label_start = ttk.Label(okno, text="Начало интервала X:")
label_start.pack()
entry_start = ttk.Entry(okno)
entry_start.pack()

label_end = ttk.Label(okno, text="Конец интервала X:")
label_end.pack()
entry_end = ttk.Entry(okno)
entry_end.pack()

plot_button = ttk.Button(okno, text="Построить график", command=graph)
plot_button.pack()
okno.mainloop()