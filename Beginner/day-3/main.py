"""
Learning about Randomization in Python, how to generate
Random numbers in Python, both integers and floating points
This is achieved using the Python Random module
So in this case, we'd be learning about how to import modules
"""


import random

# Generate random integers between 1 and 10: randint func frm random mdoule
random_integer = random.randint(1, 10)
print(random_integer)

# Generate brandom floating points from 0 to 1: random func from random modu
random_float = random.random()
print(random_float)

# Generate random floats from 0 to 5: random func with some tweak
random_zero_to_five = random.random() * 6
print(random_zero_to_five)  # remember, we can round to decimal places too