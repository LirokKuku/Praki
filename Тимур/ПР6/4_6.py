import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import messagebox


# Функция для добавления новых данных в XML-файле
def add_data():
    new_code = code_entry.get()
    new_name = name_entry.get()
    new_math = math_entry.get()
    new_russian = russian_entry.get()
    new_informatics = informatics_entry.get()

    root = tree.getroot()

    new_applicant = ET.SubElement(root.find("results"), "applicant", code=new_code)
    ET.SubElement(new_applicant, "name").text = new_name
    ET.SubElement(new_applicant, "math").text = new_math
    ET.SubElement(new_applicant, "russian").text = new_russian
    ET.SubElement(new_applicant, "informatics").text = new_informatics

    tree.write('results.xml', encoding="UTF-8")
    messagebox.showinfo("Успех", "Новые данные успешно добавлены в XML-файл")


# Создание графического интерфейса
root = Tk()
root.title("Добавление новых данных в XML-файл")
root.geometry("400x300")

# Поля для ввода новых данных
code_label = Label(root, text="Введите шифр абитуриента:")
code_label.pack()
code_entry = Entry(root)
code_entry.pack()

name_label = Label(root, text="Введите имя абитуриента:")
name_label.pack()
name_entry = Entry(root)
name_entry.pack()

math_label = Label(root, text="Введите балл по математике:")
math_label.pack()
math_entry = Entry(root)
math_entry.pack()

russian_label = Label(root, text="Введите балл по русскому языку:")
russian_label.pack()
russian_entry = Entry(root)
russian_entry.pack()

informatics_label = Label(root, text="Введите балл по информатике:")
informatics_label.pack()
informatics_entry = Entry(root)
informatics_entry.pack()

# Кнопка для добавления новых данных
add_button = Button(root, text="Добавить данные", command=add_data)
add_button.pack()

# Загрузка и парсинг XML-файла
tree = ET.parse("test.xml")

root.mainloop()