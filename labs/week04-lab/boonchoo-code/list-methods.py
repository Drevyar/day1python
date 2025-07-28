# Sample data
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
fruits = ["apple", "banana", "apple", "orange"]

# Length and counting
print(f"Length: {len(numbers)}")           # 9
print(f"Count of 1: {numbers.count(1)}")   # 2
print(f"Count of apple: {fruits.count('apple')}")  # 2

# Finding elements
print(f"Index of 4: {numbers.index(4)}")   # 2
print(f"Index of banana: {fruits.index('banana')}")  # 1

# Sorting
numbers_copy = numbers.copy()
numbers_copy.sort()                         # Sort in place
print(f"Sorted: {numbers_copy}")           # [1, 1, 2, 3, 4, 5, 5, 6, 9]

numbers_copy.sort(reverse=True)             # Sort descending
print(f"Reverse sorted: {numbers_copy}")   # [9, 6, 5, 5, 4, 3, 2, 1, 1]

# sorted() function - returns new list
sorted_numbers = sorted(numbers)
print(f"Original: {numbers}")              # [3, 1, 4, 1, 5, 9, 2, 6, 5]
print(f"New sorted: {sorted_numbers}")     # [1, 1, 2, 3, 4, 5, 5, 6, 9]

# Reversing
fruits.reverse()
print(f"Reversed fruits: {fruits}")        # ['orange', 'apple', 'banana', 'apple']

# Min, max, sum (for numeric lists)
print(f"Min: {min(numbers)}")              # 1
print(f"Max: {max(numbers)}")              # 9
print(f"Sum: {sum(numbers)}")              # 36