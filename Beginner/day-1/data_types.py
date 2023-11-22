'''
Learnt about how to check the data type of data using the 'type' function
>>> type("string")

Learnt that you cannot concatenate string with number
Learnt about typecasting from int to str, from float to str
'''

# CHECKING TYPE OF DATA
# gets the length of the input string
numb_char = len(input("what is your name? "))

# checks the type of variable
type(numb_char)

# TYPE CASTING FROM STRING TO INT
print("Your name has " + str(numb_char) + " characters")

# TYPE CASTING TO INT / FLOATS
a = float("123")
# check it's type
type(a)

# cast a string to float and perform addition operation
print(70 + float("100.5"))

# cast an integer to string
print(str(70) + str(100))