'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print ('Hello Belle')

import math

# Get coordinates from user
x1 = float(input("enter x1: "))
y1 = float(input("enter y1: "))
x2 = float(input("enter x2: "))
y2 = float(input("enter y2: "))

# Calculate distance using sqrt() and pow()
distance = math.sqrt(
    math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2)
)

# Display results
print(f"\nThe distance between ({x1}, {y1}) and ({x2}, {y2}) is: {distance:.4f}")
