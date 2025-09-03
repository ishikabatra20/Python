str = "Programming"

#len () function – This function returns the length of the strings.
print(len(str))

print(str.upper())
print(str.lower())

# String.endswith("rry") – This function_ tells whether the variable string ends with
# the string "rry" or not. If string is "harry", it returns true for "rry" since Harry ends
# with rry.
print(str.endswith("ing"))
print(str.startswith("pr"))
print(str.startswith("Pr"))

# the first character of a given string.
print(str.capitalize())

# string.count("c") – counts the total number of occurrences of any character.
print(str.count('m'))

# string.find(word) – This function friends a word and returns the index of first
# occurrence of that word in the string.
print(str.find('i'))

# string.replace (old word, new word ) – This function replace the old word with
# new word in the entire string.
print(str.replace('m','n'))
