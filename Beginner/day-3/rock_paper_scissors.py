"""
Rock Paper Scissors
Instructions
Make a rock, paper, scissors game.

Inside the main.py file, you'll find the
ASCII art for the hand signals already saved to a corresponding variable:
rock, paper, and scissors.
This will make it easy to print them out to the console.

Start the game by asking the player:

"What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."

From there you will need to figure out:

How you will store the user's input.
How you will generate a random choice for the computer.
How you will compare the user's and the computer's choice to determine the winner (or a draw).
And also how you will give feedback to the player.
You can find the "official" rules of the game on the World Rock Paper Scissors A
"""

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

# import random module to generate random integers from 0 to 2
import random
import sys

while True:
    # get user's input
    user_input = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: ")
    # generate random integers
    computer = random.randint(0, 2)
    #convert user's input to integer
    try:
        choice = int(user_input)
    except Exception:
        print("invalid input")
        sys.exit(1)
    
    if choice not in [0, 1, 2]:
        print("Invlaid input")
        sys.exit(1)
    
    # store the rock paper scissors in list
    rock_paper_scissors = [rock, paper, scissors]
    choice_name = ["Rock", "Paper", "Scissors"]
    
    # print(rock_paper_scissors[choice])
	# check if user's input match computer's input based on the index value of in list
    if rock_paper_scissors[choice] == rock_paper_scissors[computer]:
        print("It's a Draw!")
    else:
        print(f"\nYour choice: {choice_name[choice]}")
        print(rock_paper_scissors[choice])
    
        print(f"\nComputer: {choice_name[computer]}")
        print(rock_paper_scissors[computer])

	# DECISIONS BASED ON GAME RULES
    if choice == 0 and computer == 2:
        print("You win!")
    elif choice == 2 and computer == 0:
        print("You lost!")
    if choice == 2 and computer == 1:
    	print("You win!")
    elif choice == 1 and computer == 2:
    	print("You lost!")
    if choice == 1 and computer == 0:
    	print("You win!")
    elif choice == 0 and computer == 1:
    	print("You lost!")