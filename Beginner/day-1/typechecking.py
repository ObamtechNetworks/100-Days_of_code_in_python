# CHECKIG TYPE OF DATA
numchar = len(input("What is your name? "))

print("Before typecasting")
print(type(numchar))
print(numchar)

# TYPE CASTING / CONVERSION
print("We are about to typecast: ")
numchar = str(numchar)
print(type(numchar))
print(numchar)

# CONVERTING OTHER TYPES 
# str to integers
str_num = "123"
# convert to actual number
print(int(str_num) + 100)  # operation was performed using the int() function

# floats to  str and str to floats
PI = 3.1459
str_PI = str(PI)
print(str_PI, type(str_PI))

num_PI = float(str_PI)
print(num_PI, type(num_PI))