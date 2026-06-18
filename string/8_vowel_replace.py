str = input ("Enter string : ")
for char in str:
    if char.lower() in "aeious" :
        str = str.replace(char,"*")
print (f"String after replacing vowel by *   is : ",str)