import xml.etree.ElementTree as parse

tree = parse.parse('results.xml')
root = tree.getroot()

math_max = 0
math_min = 1000
russian_max = 0
russian_min = 1000
informatic_max = 0
informatic_min = 1000

for applicant in root.findall("results/applicant"):
    math_max = max(int(applicant.find("math").text), math_max)
    math_min = min(int(applicant.find("math").text), math_min)
    russian_max = max(int(applicant.find("russian").text), russian_max)
    russian_min = min(int(applicant.find("russian").text), russian_min)
    informatic_max = max(int(applicant.find("informatics").text), informatic_max)
    informatic_min = min(int(applicant.find("informatics").text), informatic_min)
print('Макс. математика: ' + str(math_max),
        'Мин. математика: ' + str(math_min),
        "Макс. русский: " + str(russian_max),
        'Мин. русский: ' + str(russian_min),
        'Макс. информатика: ' + str(informatic_max),
        'Мин. информатика: ' + str(informatic_min),
        sep='\n')