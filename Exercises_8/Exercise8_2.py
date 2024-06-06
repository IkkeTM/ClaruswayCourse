def flawed_range(start, stop):
    lst = [start+1] * (stop-start-1)
    for idx,x in enumerate(range(start+2, stop)):
        lst[idx+1] = x
    return lst

print(flawed_range(5,10))