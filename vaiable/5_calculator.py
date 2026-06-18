# calculator
a =input("Enter the first number : ")
b =input("Enter the second number : ")
c =input("Enter the operation (+, -, *, /,%) : ")
while c not in ["+", "-", "*", "/", "%"]:
        print("Invalid operation. Please enter a valid operator (+, -, *, /, %).")
        c=input("Enter the operation (+, -, *, /,%) : ")
       
if c == "+":
        print("The sum is : " + str(float(a) + float(b)))
elif c == "-":
        print("The difference is : " + str(float(a) - float(b)))
elif c == "*":
        print("The product is : " + str(float(a) * float(b)))
elif c == "/":
        print("The quotient is : " + str(float(a) / float(b)))
elif c == "%":
        print("The modulus is : " + str(float(a) % float(b)))
