def list_is_empty(list):
    if len(list) == 0:
        return True
    else:
        return False

list_1 = []
list_2 = [1,2,3]

print(list_is_empty(list_1))
print(list_is_empty(list_2))