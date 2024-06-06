import random

number = random.randint(1,1000)
print(number)

result = 0

for counter in range(1, number+1):
    result += counter

print(result)

result = int(0.5 * number ** 2 + number * 0.5)

print(result)

result = int((number + 1) * number / 2)

print(result)