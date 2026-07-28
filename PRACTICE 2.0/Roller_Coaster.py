height = int(input("What is your height in cm? "))
age = int(input("What is your age? "))
Bill = 0
if height >= 120:
    if age >=18:
        print(f"the ticket is {Bill}")
    elif age >= 12:
        print(f"the ticket is {Bill + 7}")
    elif age >= 4:
        print(f"the ticket is {Bill + 5}")
    Photo = input("Do you want a photo taken? Y or N ").lower()
    if Photo == "y":
        print(f"the ticket is {Bill + 3}")
else: 
    print("Sorry you have to grow taller before you can ride")