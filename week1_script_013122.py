# -*- coding: utf-8 -*-
"""
Spyder Editor

This is the Modelscape lesson script for January 31, 2022.
"""

# You can also add comments like this.

# The shortcut to run a line
# Mac - fn + F9
# PC - FN + F9 or Ctrl + F5

print("Hello World")

# Introduction to Python built-in data types

text = "Data Carpentry" # string

number = 42 # integer

pi_value = 3.1415 # float - number with decimal places

pi_value # call back a value

# type() function - to figure out the type of a given variable or data

type(number)

# print() function - to show a value

print(number)

# Note, this may seem redundant, but print() is the only way to display output in a script.

# Operators

2 + 2 # addition

6 * 7 # multiplication

2 ** 16 # power

13 % 5 # "modulo" - integer remainder

13 / 5 # division

# Boolean data types

3 > 4 # greater than

# Sequences: Lists and Tuples

# Note, Python indexes START WITH ZERO.

numbers = [1, 2, 3]

numbers[0] # calls first value in the list

practice = ["blue", "green", "red"]
again = ['blue', 'green', 'red']

blue = 4
green = 3
red = 14

practice_again = [blue, green, red] # without quotes, these need to be recognized as variables

# A for loop can be used to access elements in a list.
# Must be indented as part of a for loop.
# Otherwise, may throw an error if other lines indented unnecessarily.

for num in numbers:
    print(num)

# Can use the append method to add to a list.
# Akin to using functions in sequence in a tidyverse pipe.

numbers.append(4)

# Many kinds of methods available, and you can view them using the help() function.

help(numbers)

numbers.reverse()

# Tuples are ordered lists and use parentheses.
# Note, tuples cannot be changed.

a_tuple = (1, 2, 3)

another_tuple = ('blue', 'green', 'red')

# Dictionaries contain pairs of objects - keys and values.

translation = {'one':'first', 'two':'second'}

translation['one']

# Keys are unique identifiers for the value it corresponds to.

colors = {'first':'red', 'second':'blue'}

# add an item to the dictionary

colors['third'] = 'yellow'

colors

# Can also use for loops on dictionaries
# method #1:

for key, value in colors.items(): # using the .items method
    print(key, '->', value)

# method #2:

for key in colors.keys(): # using the .keys method
    print(key, '->', colors[key])
    
# Creating your own function
# Note, this always requires the def keyword

# function for addition
def add_function(a, b):
    result = a+b
    return result

# Note, user defined functions are not displayed in the Variable Explorer.

z = add_function(20, 22)

print(z)

# If working in the console, elipses (...) appear when typing out for loops
# or functions, and for each subsequent line, you do need to indent using tabs.

# End of script.
