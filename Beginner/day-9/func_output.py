# FUNCTIONS WITH OUTPUTS
def format_name(f_name, l_name):
    """
    Take a first and last name and format it
    to return a title case version of the name.
    """
    f_name = f_name.title()
    l_name = l_name.title()
    
    return f"{f_name} {l_name}"
    

# store return value of function in a variable or print directly
formatted_name = format_name("michael", "jordan")
print(formatted_name)
# print(format_name("michael", "jordan"))

# PRINT THE FUNCTION'S DOCUMENTATION
print(format_name.__doc__)