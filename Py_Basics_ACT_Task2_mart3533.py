# File Name: Py_Basics_ACT_Task2_mart3533.py
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
# Reads a temperature and pressure from the user and prints 'Danger',
# 'Normal', or 'Warning' depending on which threshold range the values
# fall into.
#
#---------------------------------------------------
#  Inputs
#---------------------------------------------------
# temp - the temperature in degrees C, entered by the user as an integer
# pressure - the pressure in MPa, entered by the user as an integer

#---------------------------------------------------
#  Computations
#---------------------------------------------------
# temp and pressure are compared against the given threshold ranges to
# determine whether conditions are dangerous, normal, or a warning.

#---------------------------------------------------
#  Outputs
#---------------------------------------------------
# Prints "Danger" if temp > 1000 or pressure > 20.
# Prints "Normal" if 750 < temp < 1000 and 10 < pressure < 20.
# Prints "Warning" for all other cases.

temp = int(input("Input the temperature in °C: "))
pressure = int(input("Input the pressure in MPa: "))
if temp > 1000 or pressure > 20:
    print("Danger")
elif 750 < temp < 1000 and 10 < pressure < 20:
    print("Normal")
else:
    print("Warning")