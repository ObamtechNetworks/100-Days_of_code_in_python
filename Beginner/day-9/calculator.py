# import module
from art import logo
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

def calculator(op, symbol, n1, n2):
    # use the user's input to process their operation
    calc_function = op[symbol]
    # now call the function on the user number
    answer = calc_function(n1, n2)
    print(f"{n1} {symbol} {n2} = {answer}")
    return answer

game_play = True
while game_play:
    # creat a variable that ask user for input
    num1 = int(input("What's the first number?: "))
    # loop through dictionary and print out each symbol (keys)
    for key, value in operations.items():
        print(key)
    
    # ask user to pick an operation symbol
    operator_symbol = input("Pick an operation from the line above: ")
    num2 = int(input("What's the second number?: "))
    
    # call the calculator function    
    answer = calculator(operations, operator_symbol, num1, num2)
    # print(f"{num1} {operator_symbol} {num2} = {answer}")
    while True:
        calc_again = input(f"Type 'y' to continue with calculating with {answer}, or type 'new' to start afresh else 'x'  to exit.: ")
        if calc_again == 'new':
            # game_play = False
            break
        elif calc_again == 'y':
            # ask user to pick operation
            operator_symbol = input("Pick another operation: ")
            # ask for the next number
            num3 = int(input("What's the next number?: "))
            # call function on these new values
            new_answer = calculator(operations, operator_symbol, answer, num3)
            answer = new_answer
        elif calc_again == 'x':
            game_play = False
            break
    
    # # ask user to see if they want to perform another operation with the result

    
    
    # # grab the function that'll perform operation through user's choice
    # calc_function = operations[operator_symbol]
    
    # # use previous answer to perform operatoin on new number
    # second_answer = calc_function(first_answer, num3)
    # print(f"{first_answer} {operator_symbol} {num3} = {second_answer}")