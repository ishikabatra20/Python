# 1. Write a python program to display a user entered name followed by Good Afternoon using input () function

name = input("Enter your name: ")
print("Good Morning!", name)
# OR

#fstring - appropriate method
print(f"Good Morning! {name}")

# 2. Write a program to fill in a letter template given below with name and date.
letter = '''Dear <|Name|>, 
You are selected! 
<|Date|> '''
date = "03-09-2025"
print(letter.replace("<|Name|>", name).replace("<|Date|>", date))

#3. Write a program to detect double space in a string.
course = "Pyth  on pro gra  mming."
print(course.find("  "))

#4. Replace the double space from problem 3 with single spaces.
name = "Python Programming is a good  programming language   and scripting language "

print(name.replace("  ", " "))

#5. Write a program to format the following letter using escape sequence characters.
letter = "Dear Aman,\n\tThis python course is nice.\nThanks!"

print(letter)