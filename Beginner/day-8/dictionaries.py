programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
    }

# accessing dictionary values
# print(programming_dictionary["Bug"])

# add new values to a dictionary
programming_dictionary["loop"] = "The action of doing something over and over again"

# print(programming_dictionary["loop"])

# creating empty dictionary
empty_dictionary = {}

# Wiping out or deleting and existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in a dictionary
programming_dictionary["Bug"] = "An annoying error in a program mostly caused by the programmer his/herself"
# print(programming_dictionary["Bug"])

# LOOPING THROUGH dictionaries
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])