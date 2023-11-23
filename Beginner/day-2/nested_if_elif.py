#!/usr/bin/python3

# EXPLORING CONDITIONALS ALONGSIDE OPERATORS

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

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
        print("Please pay $5.")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry you have to grow taller before you can ride")