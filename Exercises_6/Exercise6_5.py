my_dict = {0: 19, 1: 33, 2: 18, 3: 30, 4: 26}

lst_keys = list(my_dict.keys())
lst_keys.sort()

lst_values = list(my_dict.values())
lst_values.sort()

#I used a loop not to type out every seperate index number, ok?
for x in range(0,len(lst_keys)):
    my_dict[lst_keys[x]] = lst_values[x]

print(my_dict)