# For Lists:

# Sum of List Elements: Write a program that calculates the sum of all elements in a list.

x = [1,2,3,4,5,6,7]

def sum_of_items(some_list):
    total = 0
    for item in some_list:
        total += item
    return total
print(sum_of_items(x))

# Find the Maximum and Minimum: Find the maximum and minimum values in a list without using built-in functions.

def max_value(some_list):
    max = some_list[0]
    for item in some_list:
        if item > max:
            max = item
    return max

print(max_value(x))


# Filtering: Create a new list that contains only even or odd numbers from an existing list.

def only_even(some_list):
    even_num = []
    for num in some_list:
        if num % 2 == 0:
            even_num.append(num)
    return even_num

print(only_even(x))

def odd_num(some_list):
    odd_num = []
    for num in some_list:
        if num % 2 != 0:
            odd_num.append(num)
    return odd_num

print(odd_num(x))

# Search: Write a function to find the index of a specific element in a list.

# Remove Duplicates: Remove duplicates from a list while maintaining the original order.

# List Comprehensions: Use list comprehensions to create new lists based on existing ones, e.g., square all elements in a list.

# Sorting: Implement sorting algorithms like bubble sort or merge sort on a list.

# Sublists: Find all sublists of a given list.












































# For Dictionaries:

# Iterate Over Keys: Write a program that iterates through the keys of a dictionary and prints each key.

# Iterate Over Values: Iterate through the values in a dictionary and perform an operation on each value.

# Iterate Over Key-Value Pairs: Loop through a dictionary and print both the key and value for each item.

# Find Keys by Value: Write a function that finds keys in a dictionary based on a given value.

# Merging Dictionaries: Combine multiple dictionaries into one.

# Counting Elements: Count the occurrences of each element in a list and store the results in a dictionary.

# Filtering Dictionary: Create a new dictionary that contains only key-value pairs meeting specific criteria.

# Nested Dictionaries: Work with dictionaries of dictionaries. Iterate through nested dictionaries and access their values.

# Dictionary Comprehensions: Practice creating new dictionaries based on existing ones using dictionary comprehensions.

# Sorting: Sort a dictionary based on keys or values.