import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("🎮 Rock Paper Scissors Game")

while True:
    user = input("\nEnter rock, paper, or scissors (or 'q' to quit): ").lower()

    if user == 'q':
        break

    if user not in choices:
        print("Invalid choice!")
        continue

    computer = random.choice(choices)

    print(f"You chose: {user}")
    print(f"Computer chose: {computer}")

    if user == computer:
        print("It's a tie!")
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("You win!")
        user_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Score → You: {user_score} | Computer: {computer_score}")

print("\nFinal Score:")
print(f"You: {user_score} | Computer: {computer_score}")
print("Thanks for playing!"

