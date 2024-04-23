string_to_test = input("Please input a sentence.\n")
length_of_str = len(string_to_test)

print("This sentence is ", end="")
if length_of_str < 10:
    print("shorter than ", end="")
elif length_of_str > 10:
    print("longer than ", end="")
else:
    print("exactly ", end="")
print("10 characters")