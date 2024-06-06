import math

def armstrong(num):
    length = int(math.log10(num)+1)  # or convert to str and get the len
    n = num  # we make n to break down digit by digit
    total = 0
    while not n == 0:
        total += (n % 10)**length
        n //= 10
    return total == num

while True:
    user_num = input("Please input a whole number up until which you want to find narcissistic numbers.\n")
    if user_num.isdigit():
        user_num = int(user_num)
        break

print(f"The narcissistic numbers from 1 to {user_num} are:")
for x in range(1,user_num):
    if armstrong(x):
        print(x, end = " ")
