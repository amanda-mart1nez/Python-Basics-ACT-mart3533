# File Name: Py_Basics_ACT_Task3D_mart3533.py
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
# Uses helper functions to determine the clock hour from the hour hand's
# unit vector and to ask whether the minute hand points up or down, then
# prints the full time and the number of gongs to sound.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# x - the x component of the hour hand's unit vector, entered as a float
# y - the y component of the hour hand's unit vector, entered as a float
# response - whether the minute hand points "up" or "down", entered as a
# string inside getMinutePosition() (re-prompted until a valid answer is
# given)

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# getHour(x, y) - computes theta with atan2(y, x), converts it to an
# estimated hour, and adjusts to 12 if the result is 0.
# getMinutePosition() - repeatedly prompts until the user enters "up" or
# "down".
# minutes and gongs are set based on the minute hand's position: "00"
# and hour if up, "30" and 1 if down.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# Prints the current time as "hour:minutes".
# Prints the number of gongs the clock will sound.

from math import degrees, atan2
def getHour(x, y):
    theta = degrees(atan2(y, x))
    hour_estimate = (90 - theta) / 30
    hour = round(hour_estimate) % 12
    if hour == 0:
        hour = 12
    return hour
def getMinutePosition():
    while True:
        response = input("Is the minute hand pointing up or down? ").lower()
        if response == "up":
            return "up"
        elif response == "down":
            return "down"
        else:
            print("Please enter either 'up' or 'down'")

x = float(input("What is the x component of the hour hand's unit vector? "))
y = float(input("What is the y component of the hour hand's unit vector? "))
minute_position = getMinutePosition()
hour = getHour(x, y)
if minute_position == "up":
    minutes = "00"
    gongs = hour
else:
    minutes = "30"
    gongs = 1
print("The time is " + str(hour) + ":" + minutes)
print("The gong will sound " + str(gongs) + " time(s).")