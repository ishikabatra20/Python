# # 1. Write a program to create a dictionary of Hindi words with values as their English
# # translation. Provide user with an option to look it up!
words={
    "madad": "help",
    "kursi":"chair"
}
word = input("Enter the word: ")
print(words[word])

# #3. Can we have a set with 18 (int) and '18' (str) as a value in it?

s1={18,'18'}
print(s1)
print(type(s1))
# # 4. What will be the length of following set s:
s = set()
print(20==20.0)
s.add(20)
s.add(20.0)
s.add('20')
s.add(20.2)
print(s)      
print(len(s))     #3
# # 5. s = {} What is the type of 's'?
s2 = {}
print(type(s2))  #<class 'dict'>
# # 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# # value and use key as their names. Assume that the names are unique.
favorite_languages = {}

# Take input from 4 friends
name1 = input("Enter first friend's name: ")
lang1 = input(f"Enter {name1}'s favorite language: ")
favorite_languages[name1] = lang1

name2 = input("Enter second friend's name: ")
lang2 = input(f"Enter {name2}'s favorite language: ")
favorite_languages[name2] = lang2

name3 = input("Enter third friend's name: ")
lang3 = input(f"Enter {name3}'s favorite language: ")
favorite_languages[name3] = lang3

name4 = input("Enter fourth friend's name: ")
lang4 = input(f"Enter {name4}'s favorite language: ")
favorite_languages[name4] = lang4

print(favorite_languages)

# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
# o/p:- {'Aman': 'm1', 'Manan': 'm2', 'Manan ': 'm3', 'Yash': 'm4'}
# 8. If languages of two friends are same; what will happen to the program in problem 6?
# o/p:-{'f1 ': 'm1', 'f2': 'm3', 'f3': 'm3', 'f4': 'm4'}
# 9. Can you change the values inside a list which is contained in set S?
s= {8, 7, 12, "Harry", [1,2]}
print(s)

# no , list can't be added in sets and then also we can't change values