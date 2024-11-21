
"""these are nested lsits, a nested list is a sublist within a list, there can be an
infite number of nested lists within one list"""
nested_list = [[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]]
print(nested_list[2])  # This prints the 3rd sublist: [5, 6, 7, 8]
print(nested_list[2][3:4])  # This prints elements 1 to 2 of the 3rd sublist: [6, 7]

nested_list = [[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]]


# Remove first occurrence of the value 3
nested_list[0].remove(3)  # Removes 3 from the first sublist

print(nested_list)  # Output: [[1, 2, 4], [4, 3, 2, 1], [5, 6, 7, 8]]
"""slicing a list in different ways """
sliced_list = nested_list[:]  # Copies the entire list
print(sliced_list)  # Output: [[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8]]

sliced_list = nested_list[1:]  # Gets sublists starting from index 1 to the end
print(sliced_list)  # Output: [[4, 3, 2, 1], [5, 6, 7, 8]]

sliced_inside = nested_list[0][:3]  # Gets the first 3 elements of the first sublist
print(sliced_inside)  # Output: [1, 2, 3]

sliced_step = nested_list[::2]  # Gets every second sublist
print(sliced_step)  # Output: [[1, 2, 3, 4], [5, 6, 7, 8]]

sliced_nested = [sublist[:2] for sublist in nested_list]
print(sliced_nested)  # Output: [[1, 2], [4, 3], [5, 6]]


"""the slice notation [start:stop:step] in Python allows you to extract a portion of a list by specifying the start, stop, and step values. Here's how it works:

start: The index where the slice starts (inclusive). If not provided, it defaults to 0 (the beginning of the list).
stop: The index where the slice ends (exclusive). If not provided, it defaults to the end of the list.
step: The step size or interval between the elements you want to include in the slice. If not provided, it defaults to 1.
General Syntax:
python
Copy code
list[start:stop:step]
Examples
Let's use the following list for examples:"""

nested_list = [[1, 2, 3, 4], [4, 3, 2, 1], [5, 6, 7, 8], [9, 10, 11, 12]]
"""1. Basic Slice (start:stop)
You can slice a list from index start to stop."""

sliced_list = nested_list[1:3]  # Slices from index 1 to index 2 (index 3 is exclusive)
print(sliced_list)
# Output: [[4, 3, 2, 1], [5, 6, 7, 8]]
"""2. Start from an index (start:)
If you omit the stop, the slice goes until the end of the list."""



sliced_list = nested_list[2:]  # Slices from index 2 to the end
print(sliced_list)
# Output: [[5, 6, 7, 8], [9, 10, 11, 12]]
"""3. Slice up to an index (:stop)
If you omit the start, it starts from the beginning and slices up to the stop index."""


sliced_list = nested_list[:2]  # Slices from the beginning to index 1
print(sliced_list)
# Output: [[1, 2, 3, 4], [4, 3, 2, 1]]
"""4. Step (start:stop:step)
The step defines the interval between items in the slice. For example, getting every second element from the list:"""


sliced_list = nested_list[::2]  # Slices every second sublist
print(sliced_list)
# Output: [[1, 2, 3, 4], [5, 6, 7, 8]]

list_150 = [i for i in range (1,150)]