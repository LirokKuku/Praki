#для того чтобы показать, какой ты крутой
# import itertools
# my_list = list(input())
# permutations = list(itertools.permutations(my_list))
#
# for p in permutations:
#     print(int(''.join(p)))

#доказать, что ИМЕННО ТЫ не ищешь лёгкий путей и прёшь на пролом
my_list = list(input())
print(*my_list, sep='')
print(my_list[0], my_list[2], my_list[1], sep='')
print(my_list[1], my_list[0], my_list[2], sep='')
print(my_list[1], my_list[2], my_list[0], sep='')
print(my_list[2], my_list[1], my_list[0], sep='')
print(my_list[2], my_list[0], my_list[1], sep='')