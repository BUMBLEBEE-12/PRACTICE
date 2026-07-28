print("Welcome to the Pizza delivery shop ")
size = input("What size pizza do you want? S, M, or L ").upper()
Bill = 0
if size == "S":
    Bill += 15
elif size == "M":
    Bill += 20
elif size == "L":
    Bill += 25
else:
    print("Invalid size selected. Please choose S, M, or L.")
pepparoni = input("Do you want pepparoni? Y or N ").lower() 
if pepparoni == "y":
    if size == "S":
        Bill += 2
    else:
        Bill += 3
Extra_cheese = input("Do you want extra cheese? Y or N ").lower()
if Extra_cheese == "y":
    Bill += 1   

print(f"Your final bill is: ${Bill}")