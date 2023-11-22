"""
f-strings in python
Allows us to mix different data types in a string
"""

score = 0
height = 1.8
isWinning = True
# print("Your score is {}, your height is {}, {}".format(score, height, 'you are winning' if isWinning else 'you are loosing'))
print(f"Your score is {score}, your height is {height}, {'you are winning' if score > 0 and isWinning else 'you are loosing'}")