import random

# making and printing list
lst_len = 10
int_lst = [0] * lst_len
for x in range(0, lst_len):
    int_lst[x] = random.randint(1, 10)
print(int_lst)

def summation(lst):
    total = 0
    for x in lst:
        total += x
    return total

print(summation(int_lst))

def rm_dup(lst):
    lst = set(lst)
    return list(lst)

print(rm_dup(int_lst))

ex_lst = [1, 2, 3, 4, 4, 3, 2, 1]
print(summation(rm_dup(ex_lst)))