string_to_test = input("Please input a sentence. \n")

if len(string_to_test) % 3 == 0:
    print(string_to_test[::-1])
else:
    print(string_to_test)