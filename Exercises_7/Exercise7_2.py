number = ""

while not number.isnumeric():
    number = input("please input a number.\n")
number = int(number)

multi_lst = [0]*10

for iterator in range(1,11):
    multi_lst[iterator-1] = iterator * number

print(multi_lst)