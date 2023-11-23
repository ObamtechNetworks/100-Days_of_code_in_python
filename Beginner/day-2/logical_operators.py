"""
THERE ARE 3 LOGICAL OPERATORS IN PYTHON
and
or
not 
"""

# EXPLORING CONDITIONALS ALONGSIDE OPERATORS
# LOGICAL OPERATORS =-> TO GIVE FREE TICKETS TO PEOPLE BETWEEN
# AGE 45 AND 55 (THOSE HAVING MIDLIFE CRISIS)

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    while True:
        if age <= 0:
            print("invalid age value!")
            age = int(input("What is your age? "))
        else:
            break
    if age < 12:
        bill = 5
        print("Child tickets are $5.")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    # SECTION FOR THOSE WITH MIDLIFE CRISIS
    elif age >= 45 and age <= 55:
        bill = 0
        print("You gained a free ticket, everything's gonna be okay")
    else:
        bill = 12
        print("Adult tickets are $12")
    wants_photo = input("Do you want a photo taken? Y or N. ")
    if wants_photo == "Y":
        # Add $3 to their bill
        bill += 3
    print(f"Your final bill is {bill}")
    
else:
    print("Sorry you have to grow taller before you can ride")