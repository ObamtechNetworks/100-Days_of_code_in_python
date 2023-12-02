# Review: 
# Create a function called greet(). 
# Write 3 print statements inside the function.
# Call the greet() function and run your code.


# def greet():
#     print("Hello Good day to you")
#     print("How is the day going?")
#     print("Are you enjoying the weather")

# greet()

# Function that allows inputs
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How is the day going {name}?")
#     print(f"I hope you're enjoying the weather {name}?")

# greet_with_name("John")
    
    
# function with more than one inputs (positional arguments)
# def greet_with(name, location):
#     print(f"Hello {name}!")
#     print(f"How is the weather like at {location}")

# greet_with("John", "Fransisco")

# keyword arguments
def greet_with(name, location):
    print(f"Hello {name}!")
    print(f"How is the weather like at {location}")

# calling the function with keyword arguments
greet_with(location="Dallas", name="Andrew")