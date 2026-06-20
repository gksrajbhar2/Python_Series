# Tuple are imutable ,ordered and allow duplicate elements
# They are defined using parentheses () and can contain elements of different data types.
# Tuples support various methods that allow you to access their elements efficiently.
# some important tuple methods are :
# count() - returns the number of times a specified value appears in the tuple
# index() - returns the index of the first item with the specified value
# len() - returns the number of items in the tuple
# sorted() - returns a sorted list of the tuple's elements without modifying the original tuple
# Note: Since tuples are immutable, they do not support methods that modify the tuple, such as append(),
#       extend(), insert(), remove(), pop(), reverse(), and sort().

t = (1, 2, 3, 4, 5, 1, 2, 1)
print(t)
print("The number of times 1 appears in the tuple : ",t.count(1))
print("The index of the first occurrence of 2 in the tuple : ",t.index(2))
print("The number of items in the tuple : ",len(t))
print("Sorted list of the tuple's elements : ",sorted(t))
