Console Based
import random

# Generate a random even number
random_number = random.randint(1, 100)
if random_number % 2 != 0:
    random_number += 1  # Ensure the number is even

answer = random_number % 2  # This will always be 0, since random_number is now even

# Ask the user to think of a number
user_input = input("Think of a number. Type 'yes' once you're done: ")

# Check if the user has thought of a number
if user_input.lower() == "yes":

    user_input2 = input("Now double the number. Type 'yes' once done: ")
    if user_input2.lower() == "yes":

        user_input3 = input(f"Now add {random_number} to the result. Type 'yes' once done: ")
        if user_input3.lower() == "yes":

            user_input4 = input("Now half the number. Type 'yes' once done: ")
            if user_input4.lower() == "yes":

                user_input5 = input("Now subtract the very first number you thought of. Type 'yes' once done: ")
                if user_input5.lower() == "yes":
                    print(f"Your answer is {answer}")
