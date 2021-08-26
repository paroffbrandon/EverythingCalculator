# This Is The Right Triangle Calculator

# Import required modules
import math
from os import system, name

def clear_screen(): # This function will be used to clear the screen to keep things from getting messy
    if name == 'nt': # If computer is running windows, use the 'cls' command.
        system('cls')
    else: # If the computer is running any other operating system, use the 'clear' command.
        system('clear')


def start_rightTri():
    print("Welcome to the Right Triangle Calculator")
    print("Please leave what you want to solve for blank.")
    print("(for now, the calculator needs the base and height)")

    input("\nPress enter to continue")

    # Run forever until stopped
    while True:
        clear_screen() # Clear the screen to keep the console output clean>


        # Printng a demonstration of the what values are on the triangle
        print("  |\  ")
        print("s | \ h")
        print("  |  \  ")
        print("   ‾b‾  ")
        print("        \n")


        b = input("What is the base of your Right Triangle? ") # Ask the user for the base of the Triangle.
        s = input("What is the side of your Right Triangle? ") # Ask the user for the side of your Triangle.
        h = input("What is the hypotenuse of your Right Triangle? ") # Ask the user for the hypotenuse of the Triangle
        a = input("What is the area of your Right Triangle? ") # Ask the user for the total area of the Triangle.
        p = input("What is the perimeter of your Right Triangle? ") # Ask the user for the perimeter of the triangle


        clear_screen() # Clear the screen to keep the console output clean.


        # Make sure none of the input variables were left blank. If they were, set then to zero.
        if (b == ""):
            b = 0.0
        if (s == ""):
            s = 0.0
        if (h == ""):
            h = 0.0
        if (a == ""):
            a = 0.0
        if (p ==""):
            p = 0.0


        # Convert all of the input variables into floats, instead of leaving them all as strings.
        b = float(b)
        s = float(s)
        h = float(h)
        a = float(a)
        p = float(p)


        # These aer placeholder variables to be used later. These will be used to keep the solved variables and originally entered values seperate. This seperation will make it easier to detect issues with entered values.
        b_solved = 0.0
        s_solved = 0.0
        h_solved = 0.0
        a_solved = 0.0
        p_solved = 0.0


        # Check to make sure at least one of the variables aws supplied. If not, we do not have enough information to solve the other two variables
        if (b == 0 and s == 0 and h == 0 and a == 0 and p == 0):
            print("Error: Not enough information was supplied! You need to enter the value of at lease one variable.")


        # Solve for the missing values. This was the "Fun" part of the programming. ☺
        elif (b != 0 and s != 0): # The user has provided the base and side length of the Right Triangle
            b_solved = b # Pass through the value the user entered to the 'solved' variable.
            s_solved = s # Pass through the value the user entered to the 'solved' variable.
            h_solved = math.sqrt(((b**2)+(s**2)))# Determine the hypotenuse of the Triangle
            a_solved = (s*b)/2# Determine the area of the Triangle
            p_solved = (s+b)(math.sqrt(((b**2)+(s**2))))# Determine the Perimeter of the Triangle.
        elif (b != 0 and h != 0):
            b_solved = b # Pass through the value the user entered to the 'solved' variable.
            s_solved = math.sqrt(((h**2)-(s**2))) # Determine the value the user entered to the 'solved' variable.
            h_solved = h # Pass through the hypotenuse of the Triangle
            a_solved = (s*(math.sqrt(((h**2)-(s**2)))))/2 # Determine the area of the Triangle
            p_solved = (math.sqrt(((h**2)-(s**2))))+b+h # Determine the Perimeter of the Triangle.
        elif (b != 0 and a != 0):
            b_solved = b # Pass through the value the user entered to the 'solved' variable.
            s_solved = (2*a)/b # Pass through the value the user entered to the 'solved' variable.
            h_solved = math.sqrt(((((2*a)/b)**2)+(b**2))) # Determine the hypotenuse of the Triangle
            a_solved = a # Determine the area of the Triangle
            p_solved = ((2*a)/b)+b+(math.sqrt(((((2*a)/b)**2)+(b**2)))) # Determine the Perimeter of the Triangle.
        elif (b != 0 and p != 0):
            b_solved = b # Pass through the value the user entered to the 'solved' variable.
            s_solved =  # Pass through the value the user entered to the 'solved' variable.
            h_solved =  # Determine the hypotenuse of the Triangle
            a_solved =  # Determine the area of the Triangle
            p_solved = p # Determine the Perimeter of the Triangle.
        elif (s != 0 and h != 0):
            b_solved =  # Pass through the value the user entered to the 'solved' variable.
            s_solved = s # Pass through the value the user entered to the 'solved' variable.
            h_solved =  # Determine the hypotenuse of the Triangle
            a_solved =  # Determine the area of the Triangle
            p_solved =  # Determine the Perimeter of the Triangle.
        elif (s != 0 and a != 0):
            b_solved =  # Pass through the value the user entered to the 'solved' variable.
            s_solved = s # Pass through the value the user entered to the 'solved' variable.
            h_solved =  # Determine the hypotenuse of the Triangle
            a_solved =  # Determine the area of the Triangle
            p_solved =  # Determine the Perimeter of the Triangle.
        elif (s != 0 and p != 0):
            b_solved =  # Pass through the value the user entered to the 'solved' variable.
            s_solved = s # Pass through the value the user entered to the 'solved' variable.
            h_solved =  # Determine the hypotenuse of the Triangle
            a_solved =  # Determine the area of the Triangle
            p_solved =  # Determine the Perimeter of the Triangle.


        # This should never happen. If the script runs this, then something has been programmed wrong.
        else:
            print("Error: The script should never end up here. This means that there's a bug somewhere!")
            break


        # Make sure all of the information entered by the user conflicts with the values the program solved for.
        if ((r != 0 and r != r_solved) or (c != 0 and c != c_solved) or (a != 0 and a != a_solved)):
            print("Error: The input values you gave conflict with eachother! The circle you defined is not possible.")
            break
        else: # All of the values entered by the user work with the values the program solved for, so print solves for variables
            if (r != 0): # If user origianlly supplied the radius, put a * next to it. if not leave output alone
                print("Radius: " + str(r_solved) + "*") # Print radius
            else:
                print("Radius: " + str(r_solved)) # Print solved radius

            if (c != 0): # If user origianlly supplied the circumference, put a * next to it. if not leave output alone
                print("Circumference: " + str(c_solved) + "*") # Print circumference
            else:
                print("Circumference: " + str(c_solved)) # Print solved circumference

            if (a != 0): # If user origianlly supplied the area, put a * next to it. if not leave output alone
                print("Area: " + str(a_solved) + "*") # Print area
            else:
                print("Area: " + str(a_solved)) # Print solved area

            input("\nPress enter to continue") # this prevents the loop from immediatly erasing the results of the calculation
