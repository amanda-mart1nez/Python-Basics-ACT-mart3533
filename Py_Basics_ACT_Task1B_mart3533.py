# File Name: Py_Basics_ACT_Task1B_mart3533.py
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
# Builds a Fibonacci-style list up to a user-specified maximum term
# value (entered as an integer), re-prompting if a negative value is
# given, and prints the resulting list.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# max - the maximum term value for the list, entered by the user as an
# integer (re-prompted for a non-negative integer if the first entry is
# negative)

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# numList is built starting from 0 and 1, then extended with 1 and 2.
# While max is greater than the most recently added term, a new term
# (the sum of the two terms before it) is appended and the index is
# advanced.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# numList - the resulting list of terms, printed to the console once the
# maximum condition is reached (or immediately if max is 0 or 1).

max = int(input("What is the maximum term number? "))
numList = []
if max < 0:
    max = int(input("Please enter a non-negative integer. "))
numList.append(0)
numList.append(1)
if max == 0:
    print(str(numList))
numList.extend([1, 2])
if max == 1:
    print(str(numList))
if max > 1:
    index = 3
    while max > numList[index]:
        numList.append(numList[index - 1] + numList[index - 2])
        index += 1
    print(str(numList))