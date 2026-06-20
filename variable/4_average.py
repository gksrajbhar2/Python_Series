a=[]
n=int(input("Enter the number of elements: "))
for i in range(n):
    element=int(input("Enter element: "))
    a.append(element)
sum=0
for i in a:
    sum=sum+i
average =sum/len(a)
print("The average is:", average)
