my_lst = ["a", 1, "b", 2, "c", 3, True]

half = len(my_lst)//2

tuple_1 = my_lst[:half]
tuple_2 = my_lst[half:]

print(tuple_1)
print(tuple_2)

# for exercise 2:

tuple_3 = my_lst[::2]
tuple_4 = my_lst[1::2]

print(tuple_3)
print(tuple_4)