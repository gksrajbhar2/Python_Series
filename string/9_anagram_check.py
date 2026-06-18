# s1 = input ("Enter first string : ")
# s2 = input ("Enter second string : ")
# if sorted(s1)==sorted(s2) :
#     print(f"{s1} and {s2} are anagrams.")
# else :
#     print(f"{s1} and {s2} are not anagrams.")


#without using sorted function
s1 = input ("Enter first string : ")
s2 = input ("Enter second string : ")
if len(s1) != len(s2) :
    print(f"{s1} and {s2} are not anagrams.")
else :
    freq = {}
    for char in s1 :
        freq[char] = freq.get(char ,0) +1
    for char in s2 :
        freq[char] = freq.get(char ,0) -1
    if all(value == 0 for value in freq.values()) :
        print(f"{s1} and {s2} are anagrams.")
    else :
        print(f"{s1} and {s2} are not anagrams.")
