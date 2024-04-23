number_test = float(input("please input a number: "))

if number_test <= 1000:
    print(f"{number_test} is lower than a 1000")
elif number_test < 2000:
    print(f"{number_test} is in between 1000 and 2000")
else:
    print(f"{number_test} is higher than a 2000")