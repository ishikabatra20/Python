# Sequence of characters after backslash "\" → Escape Sequence characters
# Escape Sequence characters comprise of more than one character but represent one
# character when used within the strings.


a = "Python for AI/ML. \n Also used for scripting."
print(a)
b= "\nPython for AI/ML. \t Also used for scripting."
print(b)
c= "\nPython for AI/ML.Also used for \"scripting\"."
print(c)
d= "\nPython for AI/ML.Also used for \'scripting\'."
print(d)
