from prettytable import PrettyTable

result = [
    ["Иванов", 5, 4, 3],
    ["Петров", 4, 3, 5],
    ["Сидоров", 3, 2, 4]
]

name = ['Фамилии', "История", "Алгебра", "Информатика"]
table = PrettyTable()
table.field_names = name
for i in result:
    table.add_row(i)

print(table)



for i in result:
    if 2 in i:
        print(i[0],'задолженность',  name[i.index(2)])
    elif 0 in i:
        print(i[0],'задолженность', name[i.index(0)])

SR_is = 0
SR_a = 0
SR_if = 0
k = 0
for i in result:
    k += 1
    SR_is += i[1]
    SR_a += i[2]
    SR_if += i[3]
print('Средний балл:', '\n',
      'История:', SR_is/k, '\n',
      'Алгебра:', SR_a/k, '\n',
      'Информатика:', SR_if/k)


ot = 0
neut = 0
ut = 0
od = 0
nt = 0
for i in result:
    inf = i[3]
    if inf == 0:
        ot += 1
    elif inf == 2:
        neut += 1
    elif inf == 3:
        ut += 1
    elif inf == 4:
        od += 1
    elif inf == 5:
        nt += 1
print("Баллы по Информатике:", "\n",
      ot, '- неявка;',
      neut, '- неудовл.;',
      ut, '- удовл.;',
      od, '- хорошо;',
      nt, '- отлично.'
      )