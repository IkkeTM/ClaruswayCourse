def is_vowel(char):
    if char.lower() in vowel_lst:
        return "vowel"
    elif char.isalpha():
        return "consonant"

vowel_lst = ["a", "e", "i", "o", "u"]  # declaring outside the function is more efficient

user_str = input("Please input a sentence or word.\n")

vowel_count = 0
consonant_count = 0

for x in user_str:
    x = is_vowel(x)
    if x == "vowel":
        vowel_count += 1
    elif x == "consonant":
        consonant_count += 1

print(f"This string contains {vowel_count} vowels and {consonant_count} consonants")