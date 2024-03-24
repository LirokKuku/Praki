import xml.etree.ElementTree as ET
from tkinter import *
from tkinter import messagebox


# Функция для изменения данных в XML-файле
def update_data():
    search_value = search_entry.get()
    search_type = search_option.get()
    exam_values = [exam.get() for exam in exam_vars if exam.get() == 1]

    tree = ET.parse("results.xml")
    root = tree.getroot()

    for applicant in root.findall("results/applicant"):
        if (search_type == "Фамилия" and applicant.find('name').text == search_value) or (
                search_type == "Шифр" and applicant.attrib['code'] == search_value):
            for exam in exam_values:
                exam_name = exams[exam_values.index(exam)]
                applicant.find(exam_name).text = str(new_values[exam_name].get())

    tree.write('test.xml', encoding="UTF-8")
    messagebox.showinfo("Успех", "Данные успешно изменены в XML-файле")


# Создание графического интерфейса
root = Tk()
root.title("Изменение данных в XML-файле")
root.geometry("400x300")

# Поле для ввода значения поиска
search_label = Label(root, text="Введите фамилию или шифр абитуриента:")
search_label.pack()
search_entry = Entry(root)
search_entry.pack()

# Radiobutton для выбора поиска по фамилии или шифру
search_option = StringVar()
search_option.set("Фамилия")
search_radio1 = Radiobutton(root, text="Фамилия", variable=search_option, value="Фамилия")
search_radio2 = Radiobutton(root, text="Шифр", variable=search_option, value="Шифр")
search_radio1.pack()
search_radio2.pack()

# Checkbuttons для выбора вступительных испытаний
exams_label = Label(root, text="Выберите вступительные испытания:")
exams_label.pack()
exams = ["math", "russian", "informatics"]
exam_vars = []
new_values = {}
for exam in exams:
    var = IntVar()
    exam_vars.append(var)
    checkbutton = Checkbutton(root, text=exam, variable=var)
    checkbutton.pack()

    new_value = Entry(root)
    new_value.pack()
    new_values[exam] = new_value

# Кнопка для изменения данных
update_button = Button(root, text="Изменить данные", command=update_data)
update_button.pack()

root.mainloop()