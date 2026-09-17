# File Name: Py_Basics_ACT_Task5_mart3533.py
# Date: 9/16/26
# By: Amanda Martinez
# mart3533
# Section: 1
# Team: 10
#
# ELECTRONIC SIGNATURE
# Amanda Martinez
#
# The electronic signature above indicates that the program
# submitted for evaluation is my individual work. I have
# a general understanding of all aspects of its development
# and execution.
#
# Defines a MyFactorial function and applies it to a list of numbers
# entered by the user, printing the factorial for each valid entry or an
# error message for invalid ones.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# numbers - a string of numbers entered by the user, separated by spaces

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# MyFactorial(n) - returns -999 if n is negative or not a whole number;
# otherwise converts n to an integer and multiplies 1 through n to get
# the factorial.
# numList - the entered numbers split apart and converted to floats.
# factorialList - the factorial of each entry in numList, found by
# calling MyFactorial.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# For each entry, prints an error message if its factorial is -999,
# otherwise prints the number and its factorial.

def MyFactorial(n):
    if n < 0 or n % 1 != 0:
        result = -999
    else:
        n = int(n)
        result = 1
        for i in range(1, n + 1):
            result = result * i
            i += 1
    return(result)
numList = []
factorialList = []
numbers = input("What are some numbers to find the factorials for? ")
numList = numbers.split()
numList = [float(x) for x in numList]
for i in range(len(numList)):
    factorialList.append(MyFactorial(numList[i]))
    if factorialList[i] == -999:
        print("Error: Please enter a non-negative integer.")
    else:
        numList[i] = int(numList[i])
        print(f"{numList[i]} factorial is {factorialList[i]}")