
str = input("Enter string : ")
count = 0
for char in str.lower() :
    if char in "aeiou":
        count += 1
        
print (f"The number of vowel in {str } is : ",count)