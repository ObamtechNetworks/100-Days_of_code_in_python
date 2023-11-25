"""
💪 This is a Difficult Challenge 💪
Instructions
You are going to write a program that tests the compat. between two people.

To work out the love score between two people:

Take both people's names and check for the number of times
the letters in the word TRUE occurs.
Then check for the number of times the letters in the word LOVE occurs.
Then combine these numbers to make a 2 digit number.

For Love Scores less than 10 or greater than 90, the message should be:

"Your score is **x**, you go together like coke and mentos."

For Love Scores between 40 and 50, the message should be:

"Your score is **y**, you are alright together."

Otherwise, the message will just be their score. e.g.:

"Your score is **z**."

e.g.

name1 = "Angela Yu"

name2 = "Jack Bauer"

T occurs 0 times

R occurs 1 time

U occurs 2 times

E occurs 2 times

Total = 5

L occurs 1 time

O occurs 0 times

V occurs 0 times

E occurs 2 times

Total = 3

Love Score = 53

Print: "Your score is 53."

Example Input 1
name1 = "Kanye West"

name2 = "Kim Kardashian"

Example Output 1
Your score is 42, you are alright together.

Example Input 2
name1 = "Brad Pitt"

name2 = "Jennifer Aniston"

Example Output 2
Your score is 73.

e.g. When you hit run, this is what should happen:

The testing code will check for print output that is formatted like one of the lines below:

"Your score is 47, you are alright together."
"Your score is 125, you go together like coke and mentos."
"Your score is 54."

Score Comparison
Not sure you're getting the correct score for the exercise?
Use this table to check your code's score against mine.

Name 1	Name 2	Score
Catherine Zeta-Jones	Michael Douglas	99
Brad Pitt	Jennifer Aniston	73
Prince William	Kate Middleton	67
Angela Yu	Jack Bauer	53
Kanye West	Kim Kardashian	42
Beyonce	Jay-Z	23
John Lennon	Yoko Ono	18
Hint
The lower() function changes all the letters in a string to lower case.
https://stackoverflow.com/questions/6797984/how-do-i-lowercase-a-string-in-python

The count() function will give you the number of times a letter occurs in a string.
https://stackoverflow.com/questions/1155617/count-the-number-occurrences-of-a-character-in-a-string
"""

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# concatenate the names
lovers = name1 + name2

# normalize the names by converting to lowercase
normalize_lovers = lovers.lower()

# Begin counting number of times each char in TRUE and LOVE occurs in name
true = ["t", "r", "u", "e"]
love = ["l", "o", "v", "e"]

total_1 = 0
total_2 = 0
for char in true:
    total_1 += normalize_lovers.count(char)
for char in love:
    total_2 += normalize_lovers.count(char)

print(f"Total_1: {total_1}, Total_2: {total_2}")
# combine the result and turn to integer
love_score = int(str(total_1) + str(total_2))

# check their fate
if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and menthos.')
elif love_score >= 40 and love_score <= 50:
    print(f'Your score is {love_score}, you are alright together')
else:
    print(f'Your score is {love_score}')
    
