# List are mutable, ordered, and allow duplicate elements.
#  They are defined using square brackets [] and can contain elements of different data types. 
# Lists support various methods that allow you to manipulate and access their elements efficiently.


# some important list methods are :
# append() - adds an element at the end of the list
# extend() - adds all the elements of a list to another list
# insert() - adds an element at the specified position
# remove() - removes the first item with the specified value
# pop() - removes the element at the specified position
# reverse() - reverses the order of the list
# sort() - sorts the list in ascending order
# sorted() - returns a sorted list without modifying the original list
# index() - returns the index of the first item with the specified value
# count() - returns the number of times a specified value appears in the list
# len() - returns the number of items in the list


l = [1, 2, 3, 4, 5]
print(l)
l.append([5,7])
print("After appending [5,7] : ",l)
l.extend([7, 8, 9])
print("After extending with [7, 8, 9] : ",l)
l.insert(0, 0)
print("After inserting 0 at index 0 : ",l)
l.remove(5)
print("After removing 5 : ",l)
l.pop(0)
print("After popping element at index 0 : ",l)
l.reverse()
print("After reversing : ",l)
l.sort()
print("After sorting : ",l)
print("Sorted list without modifying original : ",sorted(l))