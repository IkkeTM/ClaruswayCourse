number_1 = eval(input("Please input a number \n"))
number_2 = eval(input("Please input another number \n"))

multiplication = number_1 * number_2

if multiplication <= 1000:
    print(multiplication)
else:
    print(number_1 + number_2)