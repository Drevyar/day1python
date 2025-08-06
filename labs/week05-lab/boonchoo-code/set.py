# Empty set (note: {} creates empty dict, not set)
empty_set = set()

# Set with initial values
colors = {"red", "green", "blue", "yellow"}
numbers = {1, 2, 3, 4, 5}
mixed_set = {1, "hello", 3.14, True}

# Set from list (removes duplicates)
list_with_duplicates = [1, 2, 2, 3, 3, 3, 4, 5]
unique_numbers = set(list_with_duplicates)
print(f"Original list: {list_with_duplicates}")
print(f"Set (unique): {unique_numbers}")

# Set from string
char_set = set("hello")
print(f"Characters in 'hello': {char_set}")

# Set comprehension
squares = {x**2 for x in range(1, 6)}
print(f"Squares: {squares}")

print(f"Colors: {colors}")
print(f"Numbers: {numbers}")
print(f"Mixed: {mixed_set}")