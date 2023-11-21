# day-0 Directory

## Introduction
Welcome to Day 0 of my Beginner journey in the 100 Days of Code in Python Challenge! This marks the beginning of my commitment to code for at least an hour every day and document my progress. Today, I'll be focusing on [Working with Variables in Python to Manage Data].

Today's Goals
# [Working with Variables in Python to Manage Data]

- [Printing]
- [Commenting]
- [Debugging]
- [String_Manipulations]
- [Variables]

# [Tasks/Exercises]
1. Write a program that prints the same as this output:
```
Day 1 - Python Print Function
The function is declared like this:
print('what to print')
```

2. String Manipulation Exercise
When you run your program, it should print the following:
```
Day 1 - String Manipulation
String Concatenation is done with the "+" sign.
e.g. print("Hello " + "world")
New lines can be created with a backslash and n.
```
#### Code to fix
```
#Fix the code below 👇

print(Day 1 - String Manipulation")
print("String Concatenation is done with the "+" sign.")
  print('e.g. print("Hello " + "world")')
print(("New lines can be created with a backslash and n.")



```

3. Write a program that prints the number of characters in a user's name. You might need to Google for a function that calculates the length of a string.

#### Example Input
`Angela`

#### Example Output
`6`

#### e.g. When you hit run, this is what should happen:

#### Hint
- You can put functions inside other functions.
- Don't try to print anything other than the length.

4. #### Variables
Instructions
Write a program that switches the values stored in the variables a and b.

*Warning. Do not change the code on lines 1-4 and 12-18. Your program should work for different inputs. e.g. any value of a and b.*

*Example Input*
`a: 3`
`b: 5`

*Example Output*
`a: 5`
`b: 3`

```
Hint
You should not have to type any numbers in your code.
You might need to make some more variables.
```

## What I Learned Today
#### About the Print function
- How to Use it
- Printed some strings with it

#### String Manipulation
- Printing multiple newlines with just a single print function
```
print("Hello World!\n
       Hello World!\n
	   Hello World!"
      )
```

- String Concatenation:
```print("Hello" + " " + "Michael")```

#### Debugging
Learnt about errors in python and how to debug them
Some errors like:
- Indentation errors
- Syntax Errors
- EOL / EOF errors
and more

#### Python Input Function
Learnt about the python input function
- How to use the python input function to receive input from user
- How to use function inside functions

#### Variables
Also learnt about variables as being labels or containers for holding values
- With variables we can use them to hold data
- Variables can vary, means can be changed

#### Also learnt about the Thonny
This IDE is very handy and effective for debugging
[Learn more here:  Thonny IDE](https://thonny.org/)

## Code Snippets
```
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
```

```
print("Hello " + input("What is your name? "))
```

```
'''variables'''
name = input("Enter your name")
print(name)

# Getting the lenght of a string
name = input("What is your name")
print(len(name))
```
# Resources
- Angela Yu #100Daysofcode Course