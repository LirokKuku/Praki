# 9.1
phones_list= [
 {'name':'Ivan', 'city':'Moscow', 'phones':['232-19-55', '+7 (916) 230-00-75']},
 {'name':'Anna', 'city':'Samara', 'phones':['200-11-15']},
 {'name':'Anna', 'city':'Vologda', 'phones':['+7 (931) 711-00-75']},
 {'name':'Nikolay', 'city':'Moscow', 'phones':['+7 (916) 778-71-05', '331-66-11', '783-33-85']},
 {'name':'Ivan', 'city':'Moscow', 'phones':['+7 (916) 205-41-05', '232-19-55']},
 {'name':'Anna', 'city':'Samara', 'phones':['+7 (916) 105-13-56']}
]

a = []
b = []
k = 0
for i in phones_list:
    a.append(i['name'])
    b.append(i['city'])
for i in range(len(a)):
    for j in range(i + 1, len(b)):
        if a[i] == a[j] and b[i] == b[j] and 'id' not in phones_list[i]:
            phones_list[j]['id'] = 'забань меня'
            k += 1
            phones_list[i]['phones'] = list(set(phones_list[i]['phones'] + phones_list[j]['phones']))
while k != 0:
    for i in range(len(phones_list)):
        if 'id' in phones_list[i]:
            del phones_list[i]
            k -= 1
            break
for i in phones_list:
    print(i)
# 9.2

BIG = {}
for i in phones_list:
    delay = {}
    for j in i['phones']:
        delay[j] = i['name']
        if i['city'] in BIG:
            BIG[i['city']].update(delay)
        else:
            BIG[i['city']] = delay
for i in BIG:
    print(i + ":", BIG[i])