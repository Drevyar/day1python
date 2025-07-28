fruits = ["apple", "banana", "orange", "grape", "kiwi"]

# Positive indexing (0-based)
print(f"First fruit: {fruits[0]}")      # apple
print(f"Second fruit: {fruits[1]}")     # banana
print(f"Last fruit: {fruits[4]}")       # kiwi

# Negative indexing
print(f"Last fruit: {fruits[-1]}")      # kiwi
print(f"Second last: {fruits[-2]}")     # grape

# List slicing
print(f"First 3 fruits: {fruits[0:3]}")     # ['apple', 'banana', 'orange']
print(f"From index 2: {fruits[2:]}")        # ['orange', 'grape', 'kiwi']
print(f"Last 2 fruits: {fruits[-2:]}")      # ['grape', 'kiwi']
print(f"Every 2nd fruit: {fruits[::2]}")    # ['apple', 'orange', 'kiwi']
print(f"Reverse list: {fruits[::-1]}")      # ['kiwi', 'grape', 'orange', 'banana', 'apple']

# Changing single elements
fruits = ["apple", "banana", "orange"]
fruits[1] = "mango"
print(fruits)  # ['apple', 'mango', 'orange']

# Changing multiple elements
fruits[0:2] = ["pear", "cherry"]
print(fruits)  # ['pear', 'cherry', 'orange']

# Adding elements
fruits.append("grape")           # Add to end
print(fruits)  # ['pear', 'cherry', 'orange', 'grape']

fruits.insert(1, "banana")       # Insert at specific position
print(fruits)  # ['pear', 'banana', 'cherry', 'orange', 'grape']

fruits.extend(["kiwi", "apple"]) # Add multiple elements
print(fruits)  # ['pear', 'banana', 'cherry', 'orange', 'grape', 'kiwi', 'apple']

# Removing elements
fruits.remove("banana")          # Remove first occurrence
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi', 'apple']

removed_fruit = fruits.pop()     # Remove and return last element
print(f"Removed: {removed_fruit}")  # apple
print(fruits)  # ['pear', 'cherry', 'orange', 'grape', 'kiwi']

removed_fruit = fruits.pop(1)    # Remove and return element at index 1
print(f"Removed: {removed_fruit}")  # cherry
print(fruits)  # ['pear', 'orange', 'grape', 'kiwi']

del fruits[0]                    # Delete element at index 0
print(fruits)  # ['orange', 'grape', 'kiwi']

fruits.clear()                   # Remove all elements
print(fruits)  # []