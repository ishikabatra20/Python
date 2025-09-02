# 1. Arithmetic operators: +, -, *, / etc.
a=2
b=3
c=a+b
print(c)

# 2. Assignment operators: =, +=, -= etc

a = 4-2
b = 6
b += 3  #increment the value of b by 3 and then assign it to b

print(a)
print (b)
b -= 3
print (b)

# 3. Comparison operators: ==, >, >=, <, != etc.-> always return boolean
d=5<4
print(d)

e=4<5
print(e)

print(5==5)

print(5!=6)

#4. Logical operators: and, or, not.

# Truth table of 'or' 
print("True or False is ", True or False)
print("True or True is ", True or True)
print("False or True is ", False or True)
print("False or False is ", False or False)

# Truth table of 'and'  
print("True and False is ", True and False)
print("True and True is ", True and True)
print("False and True is ", False and True)
print("False and False is ", False and False)

print(not(True))
print(not(False))