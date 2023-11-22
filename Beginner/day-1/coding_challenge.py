"""
CODING CHALLENGE

BMI Calculator
Instructions
Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

The BMI is a measure of some's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

The BMI is calculated by dividing a person's weight (in kg) by the square of their height (in m):

Cannot infer image mime type

Warning you should convert the result to a whole number.

Example Input
weight = 80

height = 1.75

Example Output
80 ÷ (1.75 x 1.75) = 26.122448979591837

26

e.g. When you hit run, this is what should happen:

Cannot infer image mime type

Hint
Check the data type of the inputs.
Try to use the exponent operator in your code.
Remember PEMDAS.
Remember to convert your result to a whole number (int).
"""

print("========Welcome to the BMI Calculator========")
print("👇Enter the details below to calulate your bmi👇")
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

# Write your code below this line 👇
height = float(height)
weight = int(weight)
# calculate bmi
bmi = weight / (height ** 2)
# print(bmi)
whole_num_bmi = int(bmi)
print("Your BMI is: " + str(whole_num_bmi) + "kg/m2" )









