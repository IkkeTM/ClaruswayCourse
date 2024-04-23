number = int(input("Please input a number. \n"))

print("The number is ", end = "")
if number % 2 == False: # Needlessly confusing boolean value to complicate matters
    print("even.")
else:
    print("odd.")