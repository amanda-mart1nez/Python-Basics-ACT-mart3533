# File Name: Py_Basics_ACT_Task3C_mart3533.py
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
# Calculates the current clock hour from the x and y components of the
# hour hand's unit vector and prints the time as hour:30.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# x - the x component of the hour hand's unit vector, entered as a float
# y - the y component of the hour hand's unit vector, entered as a float

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# theta - the angle of the hour hand, found with atan2(y, x) and
# converted to degrees.
# hourEstimate/hour - the estimated clock hour derived from theta,
# rounded and adjusted to 12 if the result is 0.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# Prints the current time as "hour:30".

from math import atan2, degrees
x = float(input("What is the x component of the hour hand's unit vector? "))
y = float(input("What is the y-component of the hour hand's unit vector? "))
theta = degrees(atan2(y, x))
hourEstimate = (90 - theta) / 30
hour = round(hourEstimate) % 12
if hour == 0:
    hour = 12
print("The time is " + str(hour) + ":30")