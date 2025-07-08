# Exercise 1: Basic Input
# Ask the user for their name and greet them
print("=== Exercise 1: Basic Input ===")
user_name = input("What is your name? ")
print("Hello,", user_name, "!")
print("Nice to meet you,", user_name)

# Exercise 2: Input with Numbers
# Note: input() always returns a string, so we need to convert to numbers
print("\n=== Exercise 2: Working with Numbers ===")
age_string = input("How old are you? ")
age = int(age_string)  # Convert string to integer
print("You are", age, "years old")
print("Next year you will be", age + 1, "years old")

# Exercise 3: Multiple Inputs
print("\n=== Exercise 3: Multiple Inputs ===")
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
birth_year = int(input("Enter your birth year: "))

current_year = 2025
calculated_age = current_year - birth_year

print("Full name:", first_name + " " + last_name)
print("Calculated age:", calculated_age)

# Exercise 4: Different Print Formats
print("\n=== Exercise 4: Print Formatting ===")
name = "Alice"
score = 95
subject = "Math"

# Different ways to print the same information
print("Student:", name, "Score:", score, "Subject:", subject)
print("Student: " + name + " Score: " + str(score) + " Subject: " + subject)
print("Student:", name, "scored", score, "in", subject)

# Exercise 5: Input Validation Practice
print("\n=== Exercise 5: Your Turn ===")
# Complete the following:

# Ask user for their favorite number and convert it to float
favorite_num_str = input("What's your favorite number? ")
favorite_num = float(favorite_num_str)
print("Your favorite number times 2 is:", favorite_num * 2)

# Ask for two numbers and show their sum
print("Let's add two numbers!")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
result = num1 + num2
print("The sum of", num1, "and", num2, "is", result)

# Exercise 6: Personal Information Collector
print("\n=== Exercise 6: Personal Information ===")
# Create a program that asks for and displays:
# - Name
# - Age  
# - Favorite color
# - Hometown
# Then display all information in a nice format

# Write your code here:
name = input("Enter your name: ")
age = int(input("Enter your age: "))
color = input("Enter your favorite color: ")
hometown = input("Enter your hometown: ")

print("\n--- Your Information ---")
print("Name:", name)
print("Age:", age)
print("Favorite Color:", color)
print("Hometown:", hometown)
print("Thank you for sharing!")

# Exercise 7: Simple Calculator
print("\n=== Exercise 7: Simple Calculator ===")
# Ask user for two numbers and an operation
# Display the result

print("Simple Calculator")
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = number1 + number2
elif operation == "-":
    result = number1 - number2
elif operation == "*":
    result = number1 * number2
elif operation == "/":
    result = number1 / number2
else:
    result = "Invalid operation"

print("Result:", number1, operation, number2, "=", result)

# Exercise 8: Practice Problems
print("\n=== Exercise 8: Practice Problems ===")

# Problem 1: Ask for user's name and age, then calculate birth year
user_name = input("What's your name? ")
user_age = int(input("How old are you? "))
birth_year = 2024 - user_age
print(user_name + ", you were born in approximately", birth_year)

# Problem 2: Convert temperature from Celsius to Fahrenheit
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(celsius, "degrees Celsius is", fahrenheit, "degrees Fahrenheit")

# Problem 3: Calculate rectangle area
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))
area = length * width
print("The area of a rectangle with length", length, "and width", width, "is", area)