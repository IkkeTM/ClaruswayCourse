string_to_test = input("Please input a sentence. \n")
string_length = len(string_to_test)

if string_to_test[:string_length//2] == string_to_test[:string_length//2:-1]:
    print("This is a palindrome")
else:
    print("This is not a palindrome")