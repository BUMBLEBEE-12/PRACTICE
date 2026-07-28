print("Welcome to the Treasure Hunt Game!")
print("Your mission is to find the hidden treasure.")
print("You are at a crossroad. Where do you want to go? Type 'left' or 'right'")
choice = input().lower()
if choice == "left":
    print("you are hit by a trap and lost the game. Game Over.")
elif choice == "right":
    print("You have come to a lake. There is an island in the middle of the lake. Type 'wait' to wait for a boat. Type 'swim' to swim across.")
    choice = input().lower()
    if choice == "swim":
        print("You are attacked by a trout and lost the game. Game Over.")
    elif choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. Which color do you choose?")
        choice = input().lower()
        if choice == "red":
            print("It's a room full of fire. Game Over.")
        elif choice == "yellow":
            print("You found the treasure! You Win!")
        elif choice == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("You chose a door that doesn't exist. Game Over.")