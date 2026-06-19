# mini-project : text analyser
#Gyanendra Kumar Rajbhar

text = input("Enter  a text : ")
characters = words = vowels = consonants = digits = uppercase = lowercase = special_characters = whitespace = 0

for char in text :
    characters += 1
    if char.isalpha():
        if char.lower() in "aeiou":
            vowels += 1
        else:
            consonants += 1
        if char.isupper():
            uppercase += 1
        elif char.islower():
            lowercase += 1      
    elif char.isdigit():  
        digits += 1
    elif char == " ":
        whitespace += 1
    else:
        special_characters += 1
 
 
words = len(text.split())

print ("\n_____Text Analysis Report_____")
print (f"Characters: {characters}")
print (f"Words: {words}")
print (f"Vowels: {vowels}")
print (f"Consonants: {consonants}")
print (f"Digits: {digits}")
print (f"Uppercase: {uppercase}")
print (f"Lowercase: {lowercase}")
print (f"Special Characters: {special_characters}")
print (f"Whitespace: {whitespace}")