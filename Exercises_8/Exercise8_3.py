def alphabet(letter):
    ascy = ord(letter)
    if 97 <= ascy <= 122:
        return ascy - 96
    elif 65 <= ascy <= 90:
        return ascy - 64


def pangram(in_str):
    pan_check = set()
    for x in in_str:
        pan_check.add(alphabet(x))
    if len(pan_check) == 26:
        return True
    return False



user_str = input("Please input a sentence or word.\n")
print(pangram(user_str))
