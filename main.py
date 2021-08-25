# The Everything Calculator


# Import required libraries
import math
from os import system, name

# Import other Calculators
import circle_calc
import square_calc


# This is where the fun begins
def clear_screen():
    if name == 'nt': # If the computer is running Windows, use the 'cls' command.
        system('cls')
    else: # If the computer is running any other operating system, use the 'clear' command.
        system('clear')

print("Welcome to the everything calculator!")
print("Through here you can select what type of calculations you want to do!")
print("\nWhat do you need to calculate?")
print("\n1. Squares\n2. Circles")

choice = input()
clear_screen()

while True:

    if (choice == "1"):
        square_calc.start_square()
    elif (choice == "2"):
        circle_calc.start_circle()
