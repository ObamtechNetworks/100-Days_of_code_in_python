"""
Heads or Tails

Instructions
You are going to write a virtual coin toss program.
It will randomly tell the user "Heads" or "Tails".

Important, the first letter should be capitalised
and spelt exactly like in the example e.g. Heads, not heads.

There are many ways of doing this.
But to practice what we learnt in the last lesson, you should generate a random number,
either 0 or 1.
Then use that number to print out Heads or Tails.

e.g. 1 means Heads 0 means Tails

Example Output
Heads

or

Tails
"""

# Write your code below this line 👇
# Hint: Remember to import the random module first. 🎲

# import the random module
import random

print("Welcome to the simple TOSS COIN GAME!")
while True:
    head_or_tail = random.randint(0, 1)
    user_input = input('Which do you choose? "1 for Heads" | "0 for Tails" | "exit/Enter key" to quit\n')
    
    if user_input == "exit" or user_input == '':
        break
    
    # convert user input to integer
    user_input = int(user_input)
    if user_input == head_or_tail:
            print("")
            print(f"Great! You rock!-> {'Heads' if user_input == 1 else 'Tails'}\n")
    else:
        print("")
        print(f"Oh Nope!: -> {'Heads' if head_or_tail == 1 else 'Tails'}\n")