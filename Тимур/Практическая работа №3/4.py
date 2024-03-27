import xml.etree.ElementTree as ET
from prettytable import PrettyTable
def count_same_last_names(list):
    tree = ET.parse(list)
    root = tree.getroot()

    last_name_counts = {}

    for student in root.findall('student'):
        last_name = student.find('lastname').text

        last_name_counts[last_name] = last_name_counts.get(last_name, 0) + 1

    table = PrettyTable(["ФИО студента", "Количество однофамильцев"])

    for student in root.findall('student'):
        last_name = student.find('lastname').text
        first_name = student.find('firstname').text
        middle_name = student.find('middlename').text
        full_name = f"{last_name} {first_name} {middle_name}"
        same_last_name_count = last_name_counts.get(last_name, 0)
        table.add_row([full_name, same_last_name_count])


    print(table)
count_same_last_names("2.0.xml")