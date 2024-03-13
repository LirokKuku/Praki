import xml.etree.ElementTree as parse

tree = parse.parse('results.xml')
root = tree.getroot()

for applicant in root.findall("results/applicant"):
    name = applicant.find('name').text
    math = int(applicant.find('math').text)
    russian = int(applicant.find('russian').text)
    informatics = int(applicant.find('informatics').text)
    if (math > 50) and (russian > 50) and (informatics > 50):
        print(name)