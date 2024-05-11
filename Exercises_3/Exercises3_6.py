string_to_mess = input("please give string of 5 characters or less. \n")

string_length = len(string_to_mess)

match string_length:
    case 1:
        print(string_to_mess * 6)
    case 2 | 4:
        print(string_to_mess[::-1])
    case 3:
        print(string_to_mess[2:3], string_to_mess[0:2], sep="")
    case 5:
        new_string = ""
        for x in string_to_mess:
            new_string += x + "t"
        print(new_string)