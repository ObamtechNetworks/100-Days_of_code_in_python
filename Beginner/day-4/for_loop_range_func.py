"""
Using the for loop alongside the range function
"""

# For loop with range
# for number in range(1, 11, 3):  # start, end, step
#     print(number)  # 1 4 7

sums = 0
# ADD UP EVERY NUMBER BETWEEN 1 AND 100
for number in range(1, 101):
    sums += number

print(sums)