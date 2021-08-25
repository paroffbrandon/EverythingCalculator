# This Is The Circle Calculator

# Import required modules
import math
from os import system, name

def clear_screen(): # This function will be used to clear the screen to keep things from getting messy
    if name == 'nt': # If computer is running windows, use the 'cls' command.
        system('cls') 
    else: # If the computer is running any other operating system, use the 'clear' command.
        system('clear')


def start_circle():
    print("Welcome to the Circle Calculator")
    print("Please leave what you want to solve for blank.")

    input("\nPress enter to continue")

    # Run forever until stopped
    while True:
        clear_screen() # Clear the screen to keep the console output clean>

        r = input("What is the radius of your Cirlce? ") # Ask the user for the radius of the circle.
        c = input("What is the circumference of your Circle? ") # Ask the user for the Circumference of your circle.
        a = input("What is the area of your Circle? ") # Ask the user for the total area of the circle.
        PI = 3.14159265 # Value that will be used for Pi, not exacly Pi but big enough that answers will round easily

        clear_screen() # Clear the screen to keep the console output clean.

        # Make sure none of the input variables were left blank. If they were, set then to zero.
        if (r == ""):
            r = 0.0
        if (c == ""):
            c = 0.0
        if (a ==""):
            a = 0.0

        # Convert all of the input variables into floats, instead of leaving them all as strings.
        r = float(r)
        c = float(c)
        a = float(a)

        # These aer placeholder variables to be used later. These will be used to keep the solved variables and originally entered values seperate. This seperation will make it easier to detect issues with entered values.
        r_solved = 0.0
        c_solved = 0.0
        a_solved = 0.0

        # Check to make sure at least one of the variables aws supplied. If not, we do not have enough information to solve the other two variables
        if (r == 0 and c == 0 and a == 0):
            print("Error: Not enough information was supplied! You need to enter the value of at lease one variable.")

        # Solve for the missing values
        elif (r != 0): # The user has provided the radius of the circle
            r_solved = r # Pass through the value the user entered to the 'solved' variable.
            c_solved = 2*PI*r # Determine the circle's circumference.
            a_solved = PI*(r**2) # Determine the circle's area.
        elif (c != 0): # The user has provided the circumference of the circle
            r_solved = c/(2*PI) # Determine the circle's radius.
            c_solved = c # Pass through the value the user entered as the 'solved variable.
            a_solved = PI*((c/(2*PI))**2) # Determine the circle's area.
        elif (a != 0): # The user has provided the radius of the circle
            r_solved = math.sqrt((a/PI)) # Determine the circle's radius.
            c_solved = 2*PI*(math.sqrt((a/PI))) # Determine the circle's circumference
            a_solved = a # Pass through the value the user has entered to the 'sovled' variable.

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

