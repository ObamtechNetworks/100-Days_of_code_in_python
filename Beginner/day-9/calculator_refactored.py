# import module
from art import logo
from os import system
print(logo)

# CALCULATOR

# starts creating operation function
# add
def add(a, b):
    return a + b

# subtract
def subtract(a, b):
    return a - b

# multiply
def multiply(a, b):
    return a * b

# divide
def divide(a, b):
    if b == 0:
        return "Zero Division Error!"
    return a / b


# CREAT A DICTIONARY with keys as the opeartors and values as functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply, 
    "/": divide
    }
# print(operations)

def my_calculator():
    for key, value in operations.items():
        print(key)
    game_play = True
    
    while game_play:
    # creat a variable that ask user for input
    num1 = int(input("What's the first number?: "))
    # ask user to pick an operation symbol
    operator_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the next number?: "))
    
    calc_function = operations[operator_symbol]
    answer = calc_function(num1, num2)
    print(f"{num1} {operator_symbol} {num2} = {answer}")
    
    calc_again = input(f"Type 'y' to continue with calculating with {answer}, or type 'new' to start afresh else 'x'  to exit.: ")
    if calc_again == 'y':
        num1 = answer
        system('clear')
    elif calc_again == 'new':
        my_calculator()
    elif calc_again = 'x':
        game_play = False
    else:
        game_play = False