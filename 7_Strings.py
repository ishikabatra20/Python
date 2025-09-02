# String is a data type in python.
# String is a sequence of characters enclosed in quotes.
# We can primarily write a string in these three ways.
# a ='John' # Single quoted string
# b = "John" # Double quoted string
# c = '''John''' # Triple quoted string

first_name = "Rach"
second_name = 'Green'
description = '''
String is a data type in python.
String is a sequence of characters enclosed in quotes.
We can primarily write a string in these three ways.

'''

print(first_name)
print(second_name)
print(description)

# STRING SLICING
# A string in python can be sliced for getting a part of the strings.
# Consider the following string:

#length of string
name = "Rachel"
#length=6
# +ve indices   character     -ve indices
#     0           R               -6
#     1           a               -5
#     2           c               -4
#     3           h               -3
#     4           e               -2
#     5           l               -1
print(len(name))

#The index in a sting starts from 0 to (length -1) in Python. In order to slice a string, we use the following syntax:

print(name[0])   #R
print(name[2])     #c
print(name[0:3])  #Rac
print(name[-1])  #l
#You need to reverse the direction by giving a negative step:
print(name[-1:-4:-1])#leh

# Here:

# start at -1 → "l"

# move left (step = -1)

# stop before -4 → so it collects "l", "e", "h"




