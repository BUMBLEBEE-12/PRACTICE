import random 
count = 0
player_score = 0
print("welcome to Rock, Paper, Scissors!")
while True:
    choice = input("Enter your choice (r, p, s): ").lower()
    computer_choice = random.randint(0, 99)
    if computer_choice < 33:
        computer_choice = 'r'
    elif computer_choice < 66:
        computer_choice = 'p'
    else:
        computer_choice = 's'
    print(f"Computer chose: {computer_choice}")
    if choice == computer_choice:
        print("It's a tie!")
        count += 1
    elif (choice == 'r' and computer_choice == 's') or (choice == 'p' and computer_choice == 'r') or (choice == 's' and computer_choice == 'p'):
        print("You win!")
        player_score += 1
        count += 1
    else:
        print("You lose!")
        count += 1
    if count >= 5:
        print(f"Game over! You've played {count} rounds.")
        print(f"Your score: {player_score}")
        break