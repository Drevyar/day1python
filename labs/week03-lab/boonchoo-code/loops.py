# Example: Print only even numbers from 1 to 10
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even")
    else:
        print(f"{i} is odd")
        
# Example: Input validation
password = ""
while len(password) < 8:
    password = input("Enter a password (at least 8 characters): ")
    if len(password) < 8:
        print("Password too short! Try again.")
print("Password accepted!")


# Example: Multiplication table
for i in range(1, 4):  # rows
    for j in range(1, 4):  # columns
        print(f"{i} x {j} = {i*j}", end="\t")
    print()  # new line after each row
    
    
    
# Break example: Find first number divisible by 7
for num in range(1, 100):
    if num % 7 == 0:
        print(f"First number divisible by 7: {num}")
        break

# Continue example: Skip negative numbers
numbers = [5, -3, 8, -1, 12, -7, 4]
for num in numbers:
    if num < 0:
        continue  # skip negative numbers
    print(f"Positive number: {num}")