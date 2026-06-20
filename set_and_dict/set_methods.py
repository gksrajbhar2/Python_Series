# Sets are unordered collections of unique elements. 
# They are mutable, meaning you can add or remove elements from a set after it has been created.
#  Sets are defined using curly braces {} or the set() constructor.
# Sets are useful for performing mathematical set operations like union, intersection, difference, 
# and symmetric difference.
# Here are some common set methods in Python:
# 1. add(): Adds an element to the set.
# 2. remove(): Removes an element from the set. Raises a KeyError if the element is not found.
# 3. discard(): Removes an element from the set if it is present. Does not raise an error if the element is not found.
# 4. pop(): Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.
# 5. clear(): Removes all elements from the set.
# 6. union(): Returns a new set that is the union of two sets.
# 7. intersection(): Returns a new set that is the intersection of two sets.
# 8. difference(): Returns a new set that is the difference of two sets.
# 9. symmetric_difference(): Returns a new set that is the symmetric difference of two sets.
# 10. issubset(): Returns True if the set is a subset of another set.
# 11. issuperset(): Returns True if the set is a superset of another set.
# 12. copy(): Returns a shallow copy of the set.
# 13. len(): Returns the number of elements in the set.
# 14. in: Checks if an element is in the set.
# 15. not in: Checks if an element is not in the set.
# 16. frozenset(): Returns an immutable version of a set.






# Example usage of set methods:
# Creating a set
my_set = {1, 2, 3}
# Adding an element to the set
my_set.add(4)
print("After adding 4:", my_set)  # Output: {1, 2, 3, 4}
# Removing an element from the set
my_set.remove(4)
print("After removing 4:", my_set)  # Output: {1, 2, 3}
# Discarding an element from the set
my_set.discard(6)
print("After discarding 6:", my_set)  # Output: {1, 2, 3}
# Popping an element from the set
popped_element = my_set.pop()
print("Popped element:", popped_element)  # Output: 1 (or 2 or 3, since sets are unordered)
print("After popping:", my_set)  # Output: {2, 3} (or {1, 3} or {1, 2}, depending on which element was popped)