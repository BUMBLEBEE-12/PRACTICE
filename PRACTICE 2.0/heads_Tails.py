import random
count = 0
player_score = 0
print("Welcome to Heads or Tails!")
while True:
    choice = input("Enter your choice (h for heads, t for tails): ").lower()
    computer_choice = random.randint(0, 15)
    if computer_choice < 7:
        computer_choice = 'h'
    else:
        computer_choice = 't'
    if computer_choice == choice:
        print("You win!")
        player_score += 1
        count += 1
    else:
        print("You lose!")
        count += 1
    if count >= 10:
        print(f"Game over! You've played {count} rounds.")
        print(f"Your score: {player_score}")
        break