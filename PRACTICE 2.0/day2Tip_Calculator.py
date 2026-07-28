print("Welcome to the tip calculator")
bill = float(input("How much was the total bill?\n"))

Tip =int(input("how much of a tip would you like to give ? 10% , 12% , 15%\n"))

if(Tip == 10):
    Tip = 0.10
elif(Tip == 12):
    Tip = 0.12
elif(Tip == 15):    
    Tip = 0.15
people = int(input("How many people to split the bill?"))

bill_per_person = float (bill * (1 + Tip) / people)
print(f"Each person should pay {round(bill_per_person, 3)}")
print(round(bill_per_person, 2))

