red_object_Set = {"apple", "crab", "rose", "strawberry", "ferrari"}
fruit_set = {"orange", "apple", "strawberry", "grape", "kiwi", "mandarin", "banana"}

print(red_object_Set & fruit_set)
print(fruit_set - red_object_Set)

# part 2

orange_object_set = { "basketball", "fanta", "orange", "autumn leaves", "mandarin"}

print(fruit_set & red_object_Set, fruit_set & orange_object_set)
print(red_object_Set.union(orange_object_set) - fruit_set)

# part 3

lst_1 = list(red_object_Set.union(orange_object_set).union(fruit_set))
print(lst_1)