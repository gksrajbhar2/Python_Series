sentence = input ("Enter a sentence : ")
count = 0
for word in sentence.split():
    count +=1
print(f"Number of words in the sentence: {count}")