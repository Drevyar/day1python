# Basic set operations
fruits = {"apple", "banana", "orange", "grape"}
citrus = {"orange", "lemon", "lime", "grapefruit"}

print(f"Fruits: {fruits}")
print(f"Citrus: {citrus}")

# Adding elements
fruits.add("strawberry")
print(f"After adding strawberry: {fruits}")

# Adding multiple elements
fruits.update(["kiwi", "mango"])
print(f"After adding multiple: {fruits}")

# Removing elements
fruits.remove("banana")  # Raises error if not found
print(f"After removing banana: {fruits}")

fruits.discard("pineapple")  # No error if not found
print(f"After discarding pineapple: {fruits}")

removed_fruit = fruits.pop()  # Remove arbitrary element
print(f"Removed: {removed_fruit}")
print(f"Remaining fruits: {fruits}")

# Set mathematical operations
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

print(f"Set A: {set_a}")
print(f"Set B: {set_b}")

# Union (all elements from both sets)
union = set_a | set_b  # or set_a.union(set_b)
print(f"Union (A | B): {union}")

# Intersection (common elements)
intersection = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection (A & B): {intersection}")

# Difference (elements in A but not in B)
difference = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference (A - B): {difference}")

# Symmetric difference (elements in either A or B, but not both)
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference (A ^ B): {sym_diff}")