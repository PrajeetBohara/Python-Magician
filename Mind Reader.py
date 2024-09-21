# Console Based
# import random

# # Generate a random even number
# random_number = random.randint(1, 100)
# if random_number % 2 != 0:
#     random_number += 1  # Ensure the number is even

# answer = random_number % 2  # This will always be 0, since random_number is now even

# # Ask the user to think of a number
# user_input = input("Think of a number. Type 'yes' once you're done: ")

# # Check if the user has thought of a number
# if user_input.lower() == "yes":

#     user_input2 = input("Now double the number. Type 'yes' once done: ")
#     if user_input2.lower() == "yes":

#         user_input3 = input(f"Now add {random_number} to the result. Type 'yes' once done: ")
#         if user_input3.lower() == "yes":

#             user_input4 = input("Now half the number. Type 'yes' once done: ")
#             if user_input4.lower() == "yes":

#                 user_input5 = input("Now subtract the very first number you thought of. Type 'yes' once done: ")
#                 if user_input5.lower() == "yes":
#                     print(f"Your answer is {answer}")


# GUI Based
import tkinter as tk
from tkinter import messagebox
import random

# Function to calculate the final result
def start_game():
    global random_number, current_step
    random_number = random.randint(1, 100)
    if random_number % 2 != 0:
        random_number += 1  # Ensure the number is even
    current_step = 1
    magician_label.config(text="Magician: Think of a number. Click 'Next' when done.")
    next_button.config(state="normal")
    
def next_step():
    global current_step, random_number
    if current_step == 1:
        magician_label.config(text="Magician: Now double the number. Click 'Next' when done.")
        current_step += 1
    elif current_step == 2:
        magician_label.config(text=f"Magician: Now add {random_number} to the result. Click 'Next' when done.")
        current_step += 1
    elif current_step == 3:
        magician_label.config(text="Magician: Now half the number. Click 'Next' when done.")
        current_step += 1
    elif current_step == 4:
        magician_label.config(text="Magician: Now subtract the first number you thought of. Click 'Reveal Answer' to see the answer.")
        next_button.config(state="disabled")
        reveal_button.config(state="normal")
        current_step += 1

def reveal_answer():
    answer = random_number / 2  # This will always be 0 (since random_number is even)
    messagebox.showinfo("Magician", f"Your answer is {answer}!")
    magician_label.config(text="Magician: Want to play again? Click 'Start'!")

# Create the main window
root = tk.Tk()
root.title("Magician Mind Reader Game")
root.geometry("400x300")

# Create labels and buttons
magician_label = tk.Label(root, text="Welcome to the Magician Mind Reader Game!", font=("Arial", 14), wraplength=300)
magician_label.pack(pady=20)

start_button = tk.Button(root, text="Start", command=start_game, font=("Arial", 12))
start_button.pack(pady=10)

next_button = tk.Button(root, text="Next", command=next_step, font=("Arial", 12), state="disabled")
next_button.pack(pady=10)

reveal_button = tk.Button(root, text="Reveal Answer", command=reveal_answer, font=("Arial", 12), state="disabled")
reveal_button.pack(pady=10)

# Global variables to track game state
random_number = 0
current_step = 0

# Run the application
root.mainloop()

