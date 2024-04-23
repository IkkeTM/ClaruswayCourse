def reverse_integer(input):
    input = int(input)
    output = 0
    while input > 0:
        output = output * 10 + input % 10
        input //= 10
    return output

def reverse_string(input):
    output = []
    for x in input:
        output.insert(0,x)
    output = "".join(output)
    return output


input_variable = input("please input something to be reversed \n")

if input_variable.isnumeric():
    print("The integer reversed is:", reverse_integer(input_variable))
else:
    print("The string reversed is:", reverse_string(input_variable))


def evert(input):
    num_str = str(input)
    num_str_len = len(num_str)
    reverse_str = ""
    for i in range(num_str_len):
        reverse_str += num_str[num_str_len - i - 1]
    return reverse_str

# print(evert(input_variable))

# print(input_variable[::-1])