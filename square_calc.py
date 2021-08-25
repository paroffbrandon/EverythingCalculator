# This is the Square Calculator for the "Everything Calculator" Project

# Import required modules
import math
from os import system, name

def clear_screen(): # This function will be used to clear the screen to keep things from getting messy and confusing in the console window.
    if name == 'nt': # If the computer is running Windows, use the 'cls' command.
        system('cls')
    else: # If the computer is running any other operating system, use the 'clear' command.
        system('clear')



def start_square(): # Creates a definiton that the main program can call upon to start this calculator


    while True: # Run forever until stopped
        clear_screen() # Clear the screen to keep the console output clean.

        print("Welcome to the Square Caclulator!")
        print("Please leave the values you want to solve for blank.")

        input("\nPress enter to continue")

        clear_screen()

        l = input("What is the length of one the sides of the square? ") # Ask the user for the length of one of the sides of the square.
        p = input("What is the perimeter of the of the square? ") # Ask the user for the total perimeter of the square.
        a = input("What is the area of the of the square? ") # Ask the user for the total area of the square.

        clear_screen() # Clear the screen to keep the console output clean.


        # Make sure none of the input variables were left blank. If they were, just set them to zero.
        if (l == ""):
            l = 0.0
        if (p == ""):
            p = 0.0
        if (a == ""):
            a = 0.0



        # Convert all of the input variables to floats, instead of leaving them as strings.
        l = float(l)
        p = float(p)
        a = float(a)



        # These are placeholder variables to be used later. These will be used to keep the solved variables and originally entered variables separate. This separation will make it easier to detect issues with entered values.
        l_solved = 0.0
        p_solved = 0.0
        a_solved = 0.0


        # Check to make sure at least one of the variables was supplied. If not, we don't have enough information to solve for the other two variables.
        if (l == 0 and p == 0 and a == 0):
            print("Error: Not enough information was supplied! You need to enter the value of at least one variable.")


        # Solve for missing values.
        elif (l != 0): # The user as provided the length of the one of the sides of the square.
            l_solved = l # Pass through the value the user entered to the 'solved' variable.
            p_solved = l*4 # Determine the square perimeter.
            a_solved = l*l # Determine the square area.
        elif (p != 0): # The user has provided the total perimeter of the square.
            l_solved = p/4 # Determine the square side length.
            p_solved = p # Pass through the value the user entered as the 'solved' variable.
            a_solved = (p/4)*(p/4) # Determine the square area.
        elif (a != 0): # The user has provided the total area of the square.
            l_solved = math.sqrt(a) # Determine the square side length.
            p_solved = math.sqrt(a)*4 # Determine the square perimeter.
            a_solved = a # Pass through the value the user entered as the 'solved' variable.

        else: # This should never happen. If the script runs this, then something has been programmed wrong.
            print("Error: The script should never end up here. This means that there's a bug somewhere!")
            break




        # Make sure none of the information entered by the user conflicts with the values the program solved for.
        if ((l != 0 and l != l_solved) or (p != 0 and p != p_solved) or (a != 0 and a != a_solved)):
            print("Error: The input values you entered conflict with each other! The square you've defined is not possible.")
            break
        else: # All of the values entered by the user work out with the values the program solved for, so print the solved variables.
            if (l != 0): # If the user originally supplied a value for single side length, then display a star after the output.
                print("Length: " + str(l_solved) + "*") # Print the single side length.
            else:
                print("Length: " + str(l_solved)) # Print the solved single side length.

            if (p != 0): # If the user originally supplied a value for the total perimeter of the square, then display a star after the output.
                print("Perimeter: " + str(p_solved) + "*") # Print the perimeter.
            else:
                print("Perimeter: " + str(p_solved)) # Print the solved perimeter.

            if (a != 0): # If the user originally supplied a value for the total area of the square, then display a star after the output.
                print("Area: " + str(a_solved) + "*") # Print the area.
            else:
                print("Area: " + str(a_solved)) # Print the solved area.

            input("\nPress enter to continue, exit to go back to main. \n") # Wait for the user to press enter before continuing. This prevents the loop from restarting and clearing the screen immediately after displaying the results of the calculations.

