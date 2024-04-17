finish = 1

bank = {}

while finish != 0:
    command = str(input()).split()
    if command[0] == '1':
        name = command[1]
        if name in bank:
            namesum = int(command[2])
            bank[name] += namesum
        else:
            namesum = int(command[2])
            bank[name] = namesum
    elif command[0] == '2':
        name = command[1]
        if name in bank:
            namesum = int(command[2])
            bank[name] -= namesum
        else:
            namesum = int(command[2])
            bank[name] = -namesum
    elif command[0] == '3':
        name = command[1]
        print(name + ':', bank[name])
    elif command[0] == '4':
        name_1 = command[1]
        name_2 = command[2]
        summ = int(command[3])
        bank[name_1] -= summ
        bank[name_2] += summ
    elif command[0] == '5':
        p = int(command[1])
        for i in bank:
            if bank[i] > 0:
                bank[i] = int(bank[i] * (1 + p/100))
    elif command[0] == '6':
        for i in bank:
            print(i + ':', bank[i])
            finish = 0