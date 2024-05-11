my_lst = [1, 2, 3, 4, 5, 6, 7]

pop_lst = [1, 3, 4]

for x in pop_lst:
    if len(my_lst) >= x:
        my_lst.pop(x-1)

print(my_lst)