import xml.etree.ElementTree as parse

tree = parse.parse('2.0.xml')
root = tree.getroot()

totals_works = 0
total_zachot = 0
Student_A = input().split()
for FIO in root.findall("student"):
    lastname = FIO.find('lastname').text
    firstname = FIO.find('firstname').text
    middlename = FIO.find('middlename').text
    if Student_A[0] == lastname and Student_A[1] == firstname and Student_A[-1] == middlename:
        for KIO in FIO.findall('discipline'):
            total_works = int(KIO.find('total_works').text)
            totals_works += total_works
            completed_works = int(KIO.find('completed_works').text)
            total_zachot += completed_works
        print(total_zachot/totals_works*100)