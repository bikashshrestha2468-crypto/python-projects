import tkinter as tk
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

# Function to play game
def play(user_choice):
    global user_score, computer_score

    computer = random.choice(choices)

    result_text.set(f"You: {user_choice} | Computer: {computer}")

    if user_choice == computer:
        result.set("It's a tie!")
    elif (user_choice == "rock" and computer == "scissors") or \
         (user_choice == "paper" and computer == "rock") or \
         (user_choice == "scissors" and computer == "paper"):
        result.set("You win!")
        user_score += 1
    else:
        result.set("You lose!")
        computer_score += 1

    score.set(f"Score → You: {user_score} | Computer: {computer_score}")

# Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

# Text variables
result_text = tk.StringVar()
result = tk.StringVar()
score = tk.StringVar()

# Labels
tk.Label(root, text="Choose one:", font=("Arial", 12)).pack(pady=10)
tk.Label(root, textvariable=result_text).pack()
tk.Label(root, textvariable=result).pack()
tk.Label(root, textvariable=score).pack(pady=10)

# Buttons
tk.Button(root, text="Rock", command=lambda: play("rock")).pack(fill="x")
tk.Button(root, text="Paper", command=lambda: play("paper")).pack(fill="x")
tk.Button(root, text="Scissors", command=lambda: play("scissors")).pack(fill="x")

root.mainloop()