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

#create the shift
shift = ""
while not shift.isdigit():
    shift = input("How many characters in the alphabet would you like to shift your password? \n")
shift = int(shift)

#encrypt
crypt = ""
small_z = ord("z")
big_z = ord("Z")

for letter in pwd:
    letter_num = ord(letter)

    #we check if we need to loop around the end of the alphabet
    if letter_num <= big_z and letter_num > big_z - shift or letter_num <= small_z and letter_num > small_z - shift:
        letter_num -= 26

    crypt += chr(letter_num + shift)

print(crypt)

