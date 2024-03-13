import xml.etree.ElementTree as parse

tree = parse.parse('2.0.xml')
root = tree.getroot()

grupa = int(input())
for FIO in root.findall('students/student'):
    group = int(FIO.find('group').text)
    if group == grupa:
        lastname = FIO.find('lastname').text
        firstname = FIO.find('firstname').text
        middlename = FIO.find('middlename').text
        print(lastname, firstname[0] + '.', middlename[0] + '.')