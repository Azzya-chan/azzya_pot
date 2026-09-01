'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello Belle')

import math

def get_float(prompt):
    """Safely get a float value from the user."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

# Get coordinates from user
x1 = get_float("Enter x1: ")
y1 = get_float("Enter y1: ")
x2 = get_float("Enter x2: ")
y2 = get_float("Enter y2: ")

# Calculate distance using sqrt() and pow()
distance = math.sqrt(
    math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
)

# Display results
print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.4f}")
