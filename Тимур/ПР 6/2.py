for book in root.findall("Books/Book[@id='2']"):
    book.find('Title').text = str("Война и мир. Часть 2")
    book.find('Author').text = str("Л.Н. Толстой")

tree.write('d:/Python/test.xml',encoding="UTF-8")