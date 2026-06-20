# calculator

try:
    a = float(input("Enter the first number : "))
    b = float(input("Enter the second number : "))
    c = input("Enter the operation (+, -, *, /,%) : ")
    while c not in ["+", "-", "*", "/", "%"]:
        print("Invalid operation. Please enter a valid operator (+, -, *, /, %).")
        c = input("Enter the operation (+, -, *, /,%) : ")
       
    if c == "+":
        print("The sum is : " + str(a + b))
    elif c == "-":
        print("The difference is : " + str(a - b))
    elif c == "*":
        print("The product is : " + str(a * b))
    elif c == "/":
        if b != 0:
            print("The quotient is : " + str(a / b))
        else:
            print("Error: Division by zero is not allowed.")
    elif c == "%":
        if b != 0:
            print("The modulus is : " + str(a % b))
        else:
            print("Error: Modulus by zero is not allowed.")
except ValueError:
    print("Invalid input. Please enter numeric values for the numbers.")
