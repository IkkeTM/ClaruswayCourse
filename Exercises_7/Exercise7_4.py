number = ""

while not number.isnumeric():
    number = input("please input a number.\n")
number = int(number)

even = 0
odd = 0

# we're going to eat up the number from the last digit using % 10 to determine it and // 10 to remove it
while not number == 0:
    if (number % 10 ) % 2 == 0:
        even += 1
    else:
        odd += 1
    number //= 10

print(f"Thus number had {even} even digits and {odd} odd digits.")