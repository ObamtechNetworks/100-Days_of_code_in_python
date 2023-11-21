'''
LEARNING ABOUT VARIABLES
Variables are labels or container used to hold values
variables can change or be reassigned
they can hold different type of data
In python they are best known as labels
'''
# sample variable
name = input("Enter your name: ")  # input is stored in the name variable
print(name)  # value from input is printed

length = len(name)
# printing the length of the name
print("Your name is {} chars long".format(length))


'''
Variables
Instructions
Write a program that switches the values stored in the variables a and b.

Warning. Do not change the code on lines 1-4 and 12-18.
Your program should work for different inputs. e.g. any value of a and b.

Example Input
a: 3

b: 5

Example Output
a: 5

b: 3

e.g. When you hit run, this is what should happen:

Hint
You should not have to type any numbers in your code.
You might need to make some more variables.
'''

# SOLUTION

# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆

####################################
# Write your code below this line 👇

# SOLUTION USING SIMPLE TUPLE UNPACKING
a, b = b, a

# OTHER SOLUTION USING A TEMP VARIABLE
# c = a
# a = b
# b = c

# Write your code above this line 👆
####################################

# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)
