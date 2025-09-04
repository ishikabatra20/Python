# Set is a collection of non-repetitive elements.

setEx = {1, 2, 3}
print(type(setEx))

emptySet = set()    #Don't use {} for empty set as it means empty dictionary
print(type(emptySet))

# PROPERTIES OF SETS
s = {23, 34, 23, 45, 1, 67, 2}
# 1. Sets are unordered => Element’s order doesn’t matter

# 2. Sets are unindexed => Cannot access elements by index
# print(s[2]) TypeError: 'set' object is not subscriptable

# 3. Sets cannot contain duplicate values.
print(s)   #{1, 2, 34, 67, 23, 45}

# 4. There is no way to change items in sets.
# s[3] = 34
#print(s)    #TypeError: 'set' object does not support item assignment

#5. Any type of data types can be added in sets
s1 = {23, 45, "Ravi", 67, 89, True}
print(s1, type(s1))                     #{True, 67, 23, 89, 'Ravi', 45} <class 'set'>
s1.add(345)

s1.add("Aman")
print(s1, type(s1))                     #{True, 'Ravi', 67, 'Aman', 23, 345, 89, 45} <class 'set'>
