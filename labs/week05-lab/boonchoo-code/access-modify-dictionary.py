student = {
    "name": "Alice Smith",
    "age": 20,
    "major": "Computer Science",
    "gpa": 3.8,
    "courses": ["Python", "Java", "Calculus"]
}

# Accessing values by key
print(f"Name: {student['name']}")           # Alice Smith
print(f"Age: {student['age']}")             # 20

# Using get() method (safer)
print(f"Major: {student.get('major')}")     # Computer Science
print(f"Phone: {student.get('phone')}")     # None (key doesn't exist)
print(f"Phone: {student.get('phone', 'Not provided')}")  # Default value

# Accessing nested data
print(f"First course: {student['courses'][0]}")  # Python

# Check if key exists
if 'gpa' in student:
    print(f"GPA: {student['gpa']}")

# Get all keys, values, and items
print(f"Keys: {list(student.keys())}")
print(f"Values: {list(student.values())}")
print(f"Items: {list(student.items())}")


""" modify dictionary """


# Creating a dictionary
inventory = {
    "apples": 50,
    "bananas": 30,
    "oranges": 25
}

print(f"Original inventory: {inventory}")

# Adding new items
inventory["grapes"] = 40
inventory["strawberries"] = 15
print(f"After adding items: {inventory}")

# Updating existing items
inventory["apples"] = 45  # Reduce apple count
inventory["bananas"] += 20  # Add more bananas
print(f"After updates: {inventory}")

# Using update() method
new_items = {"mangoes": 35, "pineapples": 10}
inventory.update(new_items)
print(f"After bulk update: {inventory}")

# Update with another syntax
inventory.update(apples=60, bananas=55)
print(f"After keyword update: {inventory}")

# Removing items
removed_item = inventory.pop("strawberries")  # Remove and return value
print(f"Removed {removed_item} strawberries")

del inventory["pineapples"]  # Remove without returning
print(f"After deletions: {inventory}")

# Remove last item (Python 3.7+)
last_item = inventory.popitem()
print(f"Last item removed: {last_item}")

# Clear all items
backup = inventory.copy()
inventory.clear()
print(f"After clear: {inventory}")
print(f"Backup: {backup}")