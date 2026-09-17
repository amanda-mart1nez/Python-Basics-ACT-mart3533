# File Name: Py_Basics_ACT_Task4_mart3533.py
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
# Defines a MyFactorial function that returns the factorial of a non-
# negative integer (or -999 for invalid input), then prompts the user
# for a number and prints its factorial or an error message.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# number - the value to find the factorial of, entered by the user as a
# float

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# MyFactorial(n) - returns -999 if n is negative or not a whole number;
# otherwise converts n to an integer and multiplies 1 through n to get
# the factorial.
# factorial - the result of calling MyFactorial on the entered number.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# If factorial is -999, prints "-999" and an error message asking for a
# non-negative integer.
# Otherwise, prints the entered number and its factorial.

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
number = float(input("What is the number? "))
factorial = MyFactorial(number)
if factorial == -999:
    print("-999")
    print("Please enter a non-negative integer.")
else:
    number = int(number)
    print(f"{number} factorial is {factorial}.")