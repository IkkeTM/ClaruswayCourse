import random

random_list = [(random.randint(1,100), random.randint(1,100)) for _ in range(5)]
print(random_list)
my_lst = random_list

# We create a list of reversed tuples
reversed_lst = [0] * len(my_lst)
for idx, x in enumerate(my_lst):
    reversed_lst[idx] = ((x[1], x[0]))

#we sort it
reversed_lst.sort()

#we put the reversed list into the original list
for idx, x in enumerate(reversed_lst):
    my_lst[idx] = ((x[1],x[0]))

print(my_lst)