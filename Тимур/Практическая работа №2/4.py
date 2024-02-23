num_1 = int(input())
num_2 = int(input())
a_1 = num_1 // 100
a_2 = num_1 // 10 % 10
a_3 = num_1 % 10
b_1 = num_2 // 100
b_2 = num_2 // 10 % 10
b_3 = num_2 % 10
print('Сумма:', str(a_1 + a_2 + a_3 + b_1 + b_2 + b_3))
print("Разница:" + str((a_1 + a_2 + a_3) - (b_1 + b_2 + b_3)))
print('Произведение:', str(a_1 * a_2 * a_3 * b_1 * b_2 * b_3))
print("Частное:" + str((a_1 + a_2 + a_3) / (b_1 + b_2 + b_3)))