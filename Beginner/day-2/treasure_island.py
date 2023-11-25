"""
Treasure Island

Instructions
Make your own "Choose Your Own Adventure" game.
Use conditionals such as if, else, and elif statements to
lay out the logic and the story's path in your program.

To write your code according to my story,
you can use this flow chart from draw.io to help you.

However, I think the fun part is writing your own story 😊
🧞‍♂️ 🐊 🧙‍♂️ 🧟 🧚‍♂️ 🧝‍♂️ 🥷 🤖 👽 🙀

That said if you'd like to continue with my example,
feel free to use the text snippets below...

Text Snippets from my example
'You're at a crossroad. Where do you want to go? Type "left" or "right"'
'You've come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across.'
"You arrive at the island unharmed.
There is a house with 3 doors.
One red, one yellow and one blue. Which colour do you choose?"
"It's a room full of fire. Game Over."
"You found the treasure! You Win!"
"You enter a room of beasts. Game Over."
"You chose a door that doesn't exist. Game Over."
"You get attacked by an angry trout. Game Over."
"You fell into a hole. Game Over."
Escaping Characters
If you want to use multiple sets of quotes inside a single string,
you might have to "escape" some of them using the backslash \.
You can see this in my first sentence: 'You're at a crossroad...'.
More on escaping characters here.

Extensions
Have a think about how you might write your program to make a-
player's answers less case-sensitive. In other words,
your code should work regardless of whether your user answers
"left" or "Left".

You can also add your own ASCII art. Just remember to add
three single quotes '''
at the start and at the end of your artwork to
turn it into a multi-line string.
"""

# ARTS TO PRINT BASED ON GAME SCENARIOS
bomb = '''
             \|/
            .-*-         
           / /|\         
          _L_            
        ,"   ".          
    (\ /  O O  \ /)      
     \|    _    |/       
       \  (_)  /         
       _/.___,\_         
      (_/ alf \_) 
'''

lion = """
                     __,,,,_
       _ ___.--'''`--''// ,-_ `-.
   \`"' ' |  \  \ '\/ / // / ,-  `,_
  /'`  \   |  Y  | \|/ / // / -.,__ `-.
 /<"\    \ \  |  | ||/ // | \/    |`-._`-._
/  _.-.  .-\,___|  _-| / \ \/|_/  |    `-._-
`-'  f/ |       / __/ \__  / |__/ |
     `-'       |  -| -|\__ \  |-' |
            __/   /__,-'    ),'  |'
           ((__.-'((____..-' \__,'
"""

trap = """
                                    _.-'
                                 _.-'
                 _____________.-'________________
                /         _.-' O                /|
               /  i====_======O      __________/ /
              /  / _.-'      O      /     _   /|/
             /  / | p       o      /     (   / /
            /  /           O      /_________/ /
           /  L===========O                /|/
          /______________O________________/ /
     aos |________________________________|/
"""
santa = '''
        __                                                      _.
 _---_.*~<('===          ,~~,         ,~~,         ,~~,           ,_)
(,    \ (__)=3--__._----_()'4__._----_()'4__._----_()'4__._,____.()'b
  \--------/-\  ~~(        ) ~~(        ) ~~(        )  ~~:       :'
   \_______|       (,_,,,_)     (,_,,,_)     (,_,,,_)     ;,,,,,,:
___I___I___I./     / /  \ \     / /  \ \     / /  \ \     / /  \ \
'''

thumb = '''
              _
       /(|
      (  :
     __\  \  _____
   (____)  `|
  (____)|   |
   (____).__|
    (___)__.|_____
      '''

treasure = '''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
'''

print(treasure)

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇

# ask the user which way to go
user_input = input("Which way do you want to go? Left or Right? ")

# normalize user input
normalize_input = user_input.lower()

# check what the user entered
if normalize_input == "right":
    print("Ouch! that was a ditch")
    print(bomb)
    print("------ Game Over --------")
elif normalize_input == "left":
    print(thumb)
    print("Great move!")
    print("But wait...! There's a river!..")
    decide = input("What would you do? 'swim' or 'wait?' ")
    decide = decide.lower()
    if decide == "swim":
        print("\nOh no! It's a deadly sea and too salty :(")
        print("Good by fella!")
        print("------ Game Over --------")
    elif decide == "wait":
        print("\nVoila! Your patience paid off!")
        print("Here comes Santa for your rescue")
        print(santa)
        print("\nNow you have 3 options to decide your fate")
        print("There are 3 doors which leads to the treasure room"
                "\nYou need to make a selection out of the three")
        door = input("Which door? Blue? Red? Yellow? ")
        door = door.lower()
        if door == "blue":
            print("\nOh No! That's a trap! :( So long fella!")
            print(trap)
            print("------ Game Over --------")
        elif door == "red":
            print("\nSuch hard luck! It's a lion's den")
            print(lion)
            print("----- Game Over -------")
        elif door == "yellow":
            print("\nLuck found you! :)")
            print(treasure)
            print("\nYou win")
        elif door == "green":
            print("\nHuh huh! Not so fast! That's a bomb room!")
            print(bomb)
            print("______ Game Over _______")
        else:
            print("\nYou hit the wrong answer! ------ Game over ------ ")
else:
    print("\n----- Wrong input! ------")
    print("Game Over!!!")
