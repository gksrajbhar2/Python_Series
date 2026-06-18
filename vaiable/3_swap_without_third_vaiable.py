# swaping two numbers without using third variable
a = int(input("Enter the first number (a): "))
b = int(input("Enter the second number (b): "))
print("before swapping:")
print("a =", a)
print("b =", b)
a ,b =b ,a
print("after swapping:")
print("a =", a)
print("b =", b)
