# This Is The Circle Calculator
import math
from os import system, name

def clear_screen():
    if name == 'nt':
        system('cls')
    else:
        system('clear')

print("Welcome to the Circle Calculator")
print("Please leave what you want to solve for blank.")

input("\nPress enter to continue")

while True:
    clear_screen()

    r = input("What is the radius of your Cirlce? ")
    c = input("What is the circumference of your Circle? ")
    a = input("What is the area of your Circle? ")
    PI = 3.14159265

    clear_screen()

    if (r == ""):
        r = 0.0
    if (c == ""):
        c = 0.0
    if (a ==""):
        a = 0.0

    r = float(r)
    c = float(c)
    a = float(a)

    r_solved = 0.0
    c_solved = 0.0
    a_solved = 0.0

    if (r == 0 and c == 0 and a == 0):
        print("Error: Not enough information was supplied! You need to enter the value of at lease one variable.")

    elif (r != 0):
        r_solved = r
        c_solved = 2*PI*r
        a_solved = PI*(r**2)
    elif (c != 0):
        r_solved = c/(2*PI)
        c_solved = c
        a_solved = PI*((c/(2*PI))**2)
    elif (a != 0):
        r_solved = math.sqrt((a/PI))
        c_solved = 2*PI*(math.sqrt((a/PI)))
        a_solved = a

    else:
        print("Error: The script should never end up here. This means that there's a bug somewhere!")
        break

    if ((r != 0 and r != r_solved) or (c != 0 and c != c_solved) or (a != 0 and a != a_solved)):
        print("Error: The input values you gave conflict with eachother! The circle you defined is not possible.")
        break
    else:
        if (r != 0):
            print("Radius: " + str(r_solved) + "*")
        else:
            print("Radius: " + str(r_solved))

        if (c != 0):
            print("Circumference: " + str(c_solved) + "*")
        else:
            print("Circumference: " + str(c_solved))

        if (a != 0):
            print("Area: " + str(a_solved) + "*")
        else:
            print("Area: " + str(a_solved))

        input("\nPress enter to continue")
