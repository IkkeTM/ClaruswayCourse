import random as random

def question(scale):
    number_1 = int(1 + 10 ** scale * random.random())
    number_2 = int(1 + 10 ** scale * random.random())
    question_type = int(4 * random.random())

    match question_type:
        case 0:
            if int(input(f"What is {number_1} + {number_2}? ")) == number_1 + number_2:
                return 1
        case 1:
            if int(input(f"What is {int(0.5 * (number_1 + number_2))} - {int(0.5 * number_2)}? ")) == int(0.5 * number_1):
                return 1
        case 2:
            if int(input(f"What is {number_1} * {number_2}? ")) == number_1 * number_2:
                return 1
        case 3:
            if int(input(f"What is {number_1} / {1 + number_2 // 10} rounded down? ")) == number_1 // (1+ number_2 // 10):
                return 1
    return 0

def test(score, question_number, scale):
    if question(scale):
        score += 1
        print("That is correct!")
        if (score < question_number):
            test(score, question_number, scale)
        else:
            print("Well done, you completed the test!")
    else:
        print("That is incorrect, better luck next time!")

question_amount = int(input("How many questions do you dare to answer? "))
scale = int(input("How many digits large should the numbers be? "))

test(0, question_amount, scale)
