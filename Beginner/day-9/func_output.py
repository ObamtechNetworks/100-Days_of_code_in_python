# FUNCTIONS WITH OUTPUTS
def format_name(f_name, l_name):
    f_name = f_name.title()
    l_name = l_name.title()
    
    return f"{f_name} {l_name}"
    

# store return value of function in a variable or print directly
formatted_name = format_name("michael", "jordan")
print(formatted_name)
# print(format_name("michael", "jordan"))