number_lst = []
compare_number = int(input("How many numbers do you want to compare to find the largest? "))

for _ in range(compare_number):
    number_lst.append(float(input("please input a number: ")))

largest = number_lst[0]

for x in number_lst:
    if x > largest:
        largest = x

print(f"the largest number you gave is {largest}.")