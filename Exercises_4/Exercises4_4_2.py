def valid_test(list):
    if not len(list) == 4:
        return False

    for x in list:
        if not (x > 0):
            print("invalid input")
            return False

    return True

sick_list = [10,5,6,7]
sick_list_2 = [4,5,2,19]

if valid_test(sick_list) and valid_test(sick_list_2):
    total_list = sick_list + sick_list_2
