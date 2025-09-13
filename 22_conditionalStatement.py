userAge = int(input("Enter your age: "))
print(type(userAge))
if(userAge>=18):
    print("You are eligible.")



elif(userAge<0):
    print("Enter correct input")

else:
    print("You are not eligible")
