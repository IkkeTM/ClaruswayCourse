import random

number = random.randint(1,1000)
print(number)

counter = 0
result = 0

while counter <= number:
    result += counter
    counter += 1

print(result)

result = 0.5 * number ** 2 + number * 0.5

print(result)