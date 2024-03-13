from prettytable import PrettyTable as ET

tree = ET.parse('.xml')
root = tree.getroot()

# Создание таблицы и добавление заголовков
x = PrettyTable()

x.field_names = ["ID", "Title", "Author"]

# Добавление данных в таблицу
data = [
    [1, "Python Programming", "John Doe"],
    [2, "Data Science Essentials", "Jane Smith"],
    [3, "Web Development Basics", "Alex Johnson"]
]

for row in data:
    x.add_row(row)

# Вывод таблицы
print(x)
