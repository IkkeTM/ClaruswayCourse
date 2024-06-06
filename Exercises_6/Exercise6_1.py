lst_1 = [1,2,3,4]
lst_2 = [5,6,7,8]

dict_1 = {
    lst_1[0] : lst_2[0],
    lst_1[1] : lst_2[1],
    lst_1[2] : lst_2[2],
    lst_1[3] : lst_2[3]
}

dict_2 = dict(zip(lst_1, lst_2))

print(dict_1)
print(dict_2)