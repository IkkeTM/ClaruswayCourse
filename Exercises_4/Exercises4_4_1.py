def valid_test(list):
    for x in list:
        if not (x > 0):
            print("invalid input")
            return False
    return True

sick_list = [10,5,6,7]

if valid_test(sick_list):
    total_sick_day = 0
    for x in sick_list:
        total_sick_day += x

    print(f"Frank was sick for {total_sick_day} days, and healthy for {365 - total_sick_day} days.")