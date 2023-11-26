"""
Password Generator
Instructions
The program will ask:

How many letters would you like in your password?

How many symbols would you like?

How many numbers would you like?

The objective is to take the inputs from the user to these questions and then generate a random password. Use your knowledge about Python lists and loops to complete the challenge.

Easy Version (Step 1)
Generate the password in sequence. If the user wants

4 letters
2 symbols and
3 numbers
then the password might look like this:

fgdx$*924

You can see that all the letters are together. All the symbols are together and all the numbers follow each other as well. Try to solve this problem first.

Hard Version (Step 2)
When you've completed the easy version, you're ready to tackle the hard version. In the advanced version of this project the final password does not follow a pattern. So the example above might look like this:

x$d24g*f9

And every time you generate a password, the positions of the symbols, numbers, and letters are different.
"""

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Eazy Level - Order not randomised:
# e.g. 4 letter, 2 symbol, 2 number = JduE&!91

'''
# RANDOMLY GENERATE THE LETTERS AND SAVE IN A VARIABLE
letter_comb = ""
for i in range(1, nr_letters + 1):
    # randomly generate numbers for each iteration
    random_letters = random.randint(1, nr_letters + 1)
    letter_comb = letter_comb + letters[random_letters]

# RANDOMLY GENERATE THE SYMBOLS
symbol_comb = ""
for i in range(1, nr_symbols + 1):
    # randomly generate numbers for each iteration
    random_symbols = random.randint(1, nr_symbols + 1)
    symbol_comb = symbol_comb + symbols[random_symbols]


# RANDOMLY GENERATE THE SYMBOLS
number_comb = ""
for i in range(1, nr_numbers + 1):
    # randomly generate numbers for each iteration
    random_numbers = random.randint(1, nr_numbers + 1)
    number_comb = number_comb + numbers[random_numbers]

# PRINT THE GENERATED PASSWORD TO THE USER
print(f"Here's your password {letter_comb + symbol_comb + number_comb}")
'''
# RANDOMLY GENERATE THE NUMBERS
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# CHANGING ORDER OF CHARACTER USIGN THE SCHUFFLE METHOD OF THE RANDOM
# RANDOMLY GENERATE THE LETTERS AND SAVE IN A VARIABLE
letter_comb2 = []
for i in range(1, nr_letters + 1):
    # randomly generate numbers for each iteration
    letter_comb2.append(random.choice(letters))

# RANDOMLY GENERATE THE SYMBOLS
symbol_comb2 = []
for i in range(1, nr_symbols + 1):
    # randomly generate numbers for each iteration
    symbol_comb2.append(random.choice(symbols))

# RANDOMLY GENERATE THE SYMBOLS
number_comb2 = []
for i in range(1, nr_numbers + 1):
    # randomly generate numbers for each iteration
    number_comb2.append(random.choice(numbers))

# put all list together using extend
password = letter_comb2 + symbol_comb2 + number_comb2
# Schuffle the list
random.shuffle(password)
# convert password to a string
password_str = "".join(password)
print(f"Here's your password: {password_str}")