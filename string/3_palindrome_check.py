str = input("Enter string : ")
rev = str[::-1]
if rev == str :
    print(f"{str} is a palindrome.")
else:
    print(f"{str} is not a palindrome.")