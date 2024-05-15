#create the password
while True:
    pwd = input("please input a password between 4 and 6 characters using only letters.\n")
    if 4 <= len(pwd) <= 6:
        if pwd.isalpha():
            break
        else:
            print("Invalid characters.")
    else:
        print("Invalid length.")

#test the password

while True:
    test = input("Please enter your password to terminate the program.\n")
    if test == pwd:
        print("Correct password.")
        break
    print("Wrong password.")
