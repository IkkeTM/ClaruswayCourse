my_lst = [1,2,3,4,5]

# answer = (my_lst[0] + my_lst[1] + my_lst[2] + my_lst[3] + my_lst[4])/5
# print(answer)

answer = sum(my_lst) / len(my_lst)
print(answer)

# part 2

desired_average = 5
append_number = desired_average * (len(my_lst)+1) - sum(my_lst)
my_lst.append(append_number)

answer = sum(my_lst) / len(my_lst)

print(append_number)
print(answer)