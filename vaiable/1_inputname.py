name = input("Enter your name :")
print("Hello " + name)
age = int(input("Enter your age :" ))
if (type(age) == int):
    print("You are " + str(age) + " years old.")
else:
    print("Invalid input. Please enter a valid age.")
