"""
Tip Calculator Project

Instructions
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

Example Input
Welcome to the tip calculator!
What was the total bill? $124.56
How much tip would you like to give? 10, 12, or 15? 12
How many people to split the bill? 7

Example Output
Each person should pay: $19.93

Hint
How to round a number to 2 decimal places in Python
How to limit a float to two decimal places in Python
"""

# LATER IMPROVEMENTS --> INPUT VALIDATIONS

# If the bill was $150.00, split between 5 people, with 12% tip. 


# Each person should pay (150.00 / 5) * 1.12 = 33.6
# Format the result to 2 decimal places = 33.60

# Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

# Write your code below this line 👇

# the welcome message
print("Welcome to the tip calculator")

bill = float(input("What was the total bill? $"))
percent_val = int(input("What percentage tip would you like to give? 10, 12, or 15? "))

percent_list = [10, 12, 15]

# ENSURE PERCENT VALUE IS IN AVAILABLE LIST OF PERCENTS
while True:
    if percent_val not in percent_list:
        print("Enter correct percentage tip among these values: 10, 12 or 15: ")
        percent_val = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
    else:
    	break

split_no = int(input("How many people to split the bill? "))

# convert to percent_val to actual percentage
percent_tip = percent_val / 100

calc_tip = bill + (bill * percent_tip)
final_tip = calc_tip / split_no

print(f"Each person should pay: ${final_tip:.2f}")