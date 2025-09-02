# type() function is used to find the data type of a given variable in python.

a = 31
print(type(a)) # class <int>

str = "Hello world"
print(type(str)) # class <str>

b="32.2"
print(type(b)) # class <str>

# A number can be converted into a string and vice versa (if possible)
# There are many functions to convert one data type into another.
c = float(b)
print(type(c)) #<class 'float'>

# str(31) =>"31" # integer to string conversion
# int("32") => 32 # string to integer conversion
# float(32) => 32.0 # integer to float conversion
# … and so, on
# Here "31" is a string literal and 31 a numeric literal
