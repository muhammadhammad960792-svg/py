import tkinter as tk
from tkinter import messagebox
import random

# Choices
choices = ["Rock", "Paper", "Scissors"]

# Function to play the game
def play(user_choice):
    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
    else:
        result = "Computer Wins!"

    user_label.config(text=f"You: {user_choice}")
    computer_label.config(text=f"Computer: {computer_choice}")
    result_label.config(text=result)

# Create window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("400x350")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"))
title.pack(pady=10)

instruction = tk.Label(root, text="Choose one:", font=("Arial", 12))
instruction.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=15)

rock_btn = tk.Button(button_frame, text="Rock", width=10, command=lambda: play("Rock"))
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(button_frame, text="Paper", width=10, command=lambda: play("Paper"))
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(button_frame, text="Scissors", width=10, command=lambda: play("Scissors"))
scissors_btn.grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="You: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="blue")
result_label.pack(pady=20)

exit_btn = tk.Button(root, text="Exit", width=10, command=root.destroy)
exit_btn.pack()

root.mainloop()