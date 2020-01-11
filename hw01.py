"""
CY300 Homework 1, AY20-2
Name: Bolen, Zachary
x-Number: x25588
File Name: hw01.py
"""

##NOTES: 1) You MUST name your procedures and functions EXACTLY as they appear
##          in the problem description.
##       2) Although not assessed for this first assignment, you are strongly 
##          encouraged to use the design methodology from Lesson 3 (see slides)
##          to complete this homework.  You WILL be required to use the design
##          method for all remaining assignments.

# Problem 1 (5 pts):  ##define your display_sum procedure below this line.
def display_sum(a,b):
    print(f'Sum is: {a+b}')

# Problem 2 (5 pts):  ##define your get_next_hour function below this line.
def get_next_hour(h):
    return (h + 1)%24
