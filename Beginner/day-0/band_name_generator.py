'''
This is simple program that asks for user input based on some questions
It then combines these responses from the user to coin a band name
'''

# 1. Create a greeting for your program.
print("Hello welcome to our band name generator program")

# 2. Ask the user for the city that they grew up in.
city = input("What city did you grow up?\n")

# 3. Ask the user for the name of a pet.
pet = input("What is the name of your pet?\n")

# 4. Combine the name of their city and pet and show them their band name.
band_name = city + ' ' + pet
print("The name of your band is: " + band_name)

# 5. Make sure the input cursor shows on a new line:
