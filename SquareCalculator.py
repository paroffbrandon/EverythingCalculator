# This is the Square Calculator for the "Everything Calculator" Project
# Math package
import math

def findArea(l):
    return l * l

def findPerimeter(l):
    return l + l + l + l

def findLength(A):
    return math.sqrt(l)

def findLength(P):
    return p / 4

print("  Welcome to the Square Caclulator!")
print("If you do not know the answer to the value, please answer 0")

while True:
    l = input("What is the Length of the sides of the square? ")
    p = input("What is the Perimeter of the of the square? ")
    a = input("What is the Area of the of the square? ")

    if ((a == 0 and p == 0) or (a == 0) or (p == 0)):
        print("Your Length is " + str(l))
        print("Your Area is " + str(findArea(l)))
        print("Your Perimeter is " + str(findPerimeter(l)))

    elif (l == 0 and a == 0):
        print("Your Length is ", findlegnth(P))
        print("Your Area is ")

    elif (l == 0 and p == 0):
        print("Y")

    else:
        break
