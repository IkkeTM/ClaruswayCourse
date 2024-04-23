letter = input("please input a letter: ")

vowel_lst = ["a", "e", "o", "u", "i"]

if letter[0].lower() in vowel_lst:
    print(f"{letter[0]} is a vowel.")
else:
    print(f"{letter[0]} is not a vowel.")