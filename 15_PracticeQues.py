# 1. Write a program to store seven fruits in a list entered by the user.
fruitsList = []
f1 = input("Enter fruit 1: ")
fruitsList.append(f1)
f2 = input("Enter fruit 2: ")
fruitsList.append(f2)
f3 = input("Enter fruit 3: ")
fruitsList.append(f3)
f4 = input("Enter fruit 4: ")
fruitsList.append(f4)
f5 = input("Enter fruit 5: ")
fruitsList.append(f5)
f6 = input("Enter fruit 6: ")
fruitsList.append(f6)

print(fruitsList)
# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.

marks = []
f1 = int(input("Enter maks of student 1: "))
marks.append(f1)
f2 = int(input("Enter maks of student 2: "))
marks.append(f2)
f3 = int(input("Enter maks of student 3: "))
marks.append(f3)
f4 = int(input("Enter maks of student 4: "))
marks.append(f4)
f5 = int(input("Enter maks of student 5: "))
marks.append(f5)
f6 = int(input("Enter maks of student 6: "))
marks.append(f6)

print(f"Marks: {marks}")
marks.sort()
print(f"Sorted Marks: {marks}")

# 3. Check that a tuple type can be changed to list type in python.
tupleEx = (1,2,3,4)
print(type(tupleEx))
listEx = list(tupleEx)
print(type(listEx))
# 4. Write a program to sum a list with 4 numbers.
numberList = [20, 40, 50, 10]
total = sum(numberList)
print(f"Total:  {total}")
# 5. Write a program to count the number of zeros in the following tuple:
a = (7, 0, 8, 0, 0, 9)
print(a.count(0))