import xml.etree.ElementTree as parse

#Для считывания структуры и содержимого файла:(я хз, почему ET не работает, нашёл только способ через parse)
tree = parse.parse('Books.xml')
root=tree.getroot()

#Фрагмент кода для вывода данных всех книг:
for book in root.findall("Books/Book"):
    title = book.find('Title').text
    author = book.find('Author').text
    id=book.get('id')
    #ol=book.find('Title').get('ol')
    print(id, title, author)

print()

#Фрагмент кода для вывода данных о книге «Война и мир»:
for book in root.findall("Books/Book[Title='Война и мир']"):
    title = book.find('Title').text
    author = book.find('Author').text
    id=book.get('id')
    print(id, title, author)

print()

#Фрагмент кода для вывода данных о книге с id=1. Id – атрибут секции Book:
for book in root.findall("Books/Book[@id='1']"):
    title = book.find('Title').text
    author = book.find('Author').text
    id = book.get('id')
    print(id, title, author)