# Dictionaries are mutable, unordered collection of key-value pairs.
# Each key must be unique and immutable (like strings, numbers, or tuples), while values can be of any data type and can be duplicated.
# Dictionaries are defined using curly braces {} or the dict() constructor.
# Here are some common dictionary methods in Python:
# 1. keys(): Returns a view object that displays a list of all the keys in the dictionary.
# 2. values(): Returns a view object that displays a list of all the values in the dictionary.
# 3. items(): Returns a view object that displays a list of key-value pairs in the dictionary.
# 4. get(): Returns the value for a specified key. If the key is not found, it returns a default value (None if not specified).
# 5. pop(): Removes the specified key and returns its value. Raises a KeyError if the key is not found.
# 6. popitem(): Removes and returns an arbitrary key-value pair from the dictionary. Raises a KeyError if the dictionary is empty.
# 7. clear(): Removes all items from the dictionary.
# 8. update(): Updates the dictionary with key-value pairs from another dictionary or an iterable of key-value pairs.
# 9. copy(): Returns a shallow copy of the dictionary.
# 10. len(): Returns the number of key-value pairs in the dictionary.
# 11. in: Checks if a key is in the dictionary.
# 12. not in: Checks if a key is not in the dictionary.


# Example usage of dictionary methods:
# Creating a dictionary
my_dict = {"name": "Rajbhar", "age": 23, "city": "Bhairahawa"}
# Getting the keys of the dictionary
print("Keys:", my_dict.keys())  # Output: dict_keys(['name', 'age', 'city'])
# Getting the values of the dictionary
print("Values:", my_dict.values())  # Output: dict_values(['Rajbhar', 23, 'Bhairahawa'])
# Getting the items of the dictionary
print("Items:", my_dict.items())  # Output: dict_items([('name', 'Rajbhar'), ('age', 23), ('city', 'Bhairahawa')])
# Getting the value for a specific key
print("Name:", my_dict.get("name"))  # Output: Rajbhar
# Removing a key-value pair from the dictionary
removed_value = my_dict.pop("age")
print("Removed value:", removed_value)  # Output: 23
print("After popping age:", my_dict)  # Output: {'name': 'Rajbhar', 'city': 'Bhairahawa'}
# Removing an arbitrary key-value pair from the dictionary
removed_item = my_dict.popitem()
print("Removed item:", removed_item)  # Output: ('city', 'Bhairahawa')
print("After popping an item:", my_dict)  # Output: {'name': 'Rajbhar'}