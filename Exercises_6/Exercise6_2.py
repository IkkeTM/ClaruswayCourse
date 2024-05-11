my_dict = {"dad": "Eise", "sister_1": "Iris",
"sister_2": "Nicky"}

key_to_test = "daddy"

if key_to_test in my_dict.keys():
    print(key_to_test, " is in the dictionary")
else:
    my_dict[key_to_test] = "Empty"
    print(my_dict)