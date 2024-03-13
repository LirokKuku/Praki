import xml.etree.ElementTree as parse

tree = parse.parse('results.xml')
root = tree.getroot()

for applicant in root.findall("results/applicant[name='Иванов']"):
    math = int(applicant.find('math').text)
    russian = int(applicant.find('russian').text)
    informatics = int(applicant.find('informatics').text)
    print((math + russian + informatics)/3)