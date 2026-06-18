str = input ("Enter string : ")
freq = {}
for char in str:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(f"Frequency of each character in {str} is : ",freq)