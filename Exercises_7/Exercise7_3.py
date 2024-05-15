number_lst = []

for number in range(2950, 5211):
    if number % 9 == 0 or number % 13 == 0:
        number_lst.append(number)

print(number_lst)