import xml.etree.ElementTree as parse

tree = parse.parse('2.0.xml')
root = tree.getroot()

list1 = []
list2 = []
for FIO in root.findall("student"):
    lastname = FIO.find('lastname').text
    firstname = FIO.find('firstname').text
    middlename = FIO.find('middlename').text
    list1.append(lastname)
    list2.append(lastname + ' ' + firstname + " " + middlename)
for i in range(len(list1)):
    print(list2[i], list1.count(list1[i]) - 1)