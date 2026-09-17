# File Name: Factorial.py
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
# negative integer, or -999 if the input is negative or not a whole
# number.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# n - the number to find the factorial of, passed in as a parameter

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# Returns -999 if n is negative or not a whole number.
# Otherwise, converts n to an integer and multiplies 1 through n to
# compute the factorial.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# Returns the factorial of n, or -999 if n was invalid.

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