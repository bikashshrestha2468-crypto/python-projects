import tkinter as tk
import random

# Generate random number
number = random.randint(1, 100)

# Function to check guess
def check_guess():
    try:
        guess = int(entry.get())
        
        if guess < number:
            result_label.config(text="Too Low ⬇")
        elif guess > number:
            result_label.config(text="Too High ⬆")
        else:
            result_label.config(text="Correct 🎉")
        
        entry.delete(0, tk.END)
    except:
        result_label.config(text="Enter a valid number!")

# Reset game
def reset_game():
    global number
    number = random.randint(1, 100)
    result_label.config(text="Game Reset! Guess again.")
    entry.delete(0, tk.END)

# Window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("300x250")

# Title
title = tk.Label(root, text="Guess Number (1-100)", font=("Arial", 14))
title.pack(pady=10)

# Input
entry = tk.Entry(root)
entry.pack(pady=5)

# Buttons
guess_btn = tk.Button(root, text="Check", command=check_guess)
guess_btn.pack(pady=5)

reset_btn = tk.Button(root, text="Reset", command=reset_game)
reset_btn.pack(pady=5)

# Result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()