# =============================================================================
# Python Functions - Complete Code Examples for Lab Demonstration
# =============================================================================

# =============================================================================
# PART 1: BASIC FUNCTIONS
# =============================================================================
print("=== PART 1: BASIC FUNCTIONS ===")

# Example 1: Simple function without parameters
def say_hello():
    """A simple function that prints a greeting"""
    print("Hello, World!")
    print("Welcome to Python functions!")

# Calling the function
print("Calling say_hello():")
say_hello()
print()

# Example 2: Function that performs a task
def draw_separator():
    """Draws a line separator"""
    print("-" * 40)

draw_separator()
print("This is between separators")
draw_separator()
print()

# =============================================================================
# PART 2: FUNCTIONS WITH PARAMETERS
# =============================================================================
print("\n=== PART 2: FUNCTIONS WITH PARAMETERS ===")

# Example 1: Function with one parameter
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()

# Example 2: Function with multiple parameters
def introduce_person(name, age, city):
    """Introduces a person with their details"""
    print(f"Hi! My name is {name}.")
    print(f"I am {age} years old.")
    print(f"I live in {city}.")
    print()

print("Calling introduce_person:")
introduce_person("Diana", 25, "New York")
introduce_person("Eve", 30, "Los Angeles")

# Example 3: Mathematical function
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)

# =============================================================================
# PART 3: FUNCTIONS WITH RETURN VALUES
# =============================================================================
print("\n=== PART 3: FUNCTIONS WITH RETURN VALUES ===")

# Example 1: Function that returns a value
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()

# Example 2: Function returning multiple values
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()

# Example 3: Using returned values in expressions
def multiply(x, y):
    """Multiplies two numbers"""
    return x * y

def square(n):
    """Returns the square of a number"""
    return n * n

print("Using return values in expressions:")
result = multiply(4, 5) + square(3)
print(f"multiply(4, 5) + square(3) = {multiply(4, 5)} + {square(3)} = {result}")
print()

# =============================================================================
# PART 4: DEFAULT PARAMETERS
# =============================================================================
print("\n=== PART 4: DEFAULT PARAMETERS ===")

# Example 1: Function with default parameter
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

# Example 2: Multiple default parameters
def create_profile(name, age=18, country="Unknown"):
    """Creates a user profile with default values"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
create_profile("Alice")  # All defaults
create_profile("Bob", 25)  # Age specified
create_profile("Charlie", 30, "USA")  # All specified
print()

# Example 3: Power function with default exponent
def power(base, exponent=2):
    """Calculates base raised to exponent (default: square)"""
    return base ** exponent

print("Power function with defaults:")
print(f"power(5) = {power(5)}")  # Square
print(f"power(5, 3) = {power(5, 3)}")  # Cube
print(f"power(2, 4) = {power(2, 4)}")  # Fourth power
print()

# =============================================================================
# PART 5: VARIABLE SCOPE
# =============================================================================
print("\n=== PART 5: VARIABLE SCOPE ===")

# Global variables
global_message = "I'm a global variable"
counter = 0

def demonstrate_scope():
    """Demonstrates local vs global scope"""
    # Local variable
    local_message = "I'm a local variable"
    
    # Accessing global variable
    print(f"Inside function - Global: {global_message}")
    print(f"Inside function - Local: {local_message}")
    
    # Modifying global variable (need global keyword)
    global counter
    counter += 1
    print(f"Counter inside function: {counter}")

print("Scope demonstration:")
print(f"Before function call - Counter: {counter}")
demonstrate_scope()
print(f"After function call - Counter: {counter}")
print(f"Outside function - Global: {global_message}")
# print(local_message)  # This would cause an error!
print()

# =============================================================================
# PART 6: PRACTICAL EXAMPLES
# =============================================================================
print("\n=== PART 6: PRACTICAL EXAMPLES ===")

# Example 1: Grade calculator
def calculate_grade(score):
    """Converts numerical score to letter grade"""
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

print("Grade Calculator:")
test_scores = [95, 87, 73, 68, 45]
for score in test_scores:
    grade = calculate_grade(score)
    print(f"Score {score} = Grade {grade}")
print()

# Example 2: Password validator
def is_strong_password(password):
    """Checks if password meets strength requirements"""
    if len(password) < 8:
        return False, "Password too short (minimum 8 characters)"
    
    has_letter = any(c.isalpha() for c in password)
    has_number = any(c.isdigit() for c in password)
    
    if not has_letter:
        return False, "Password must contain at least one letter"
    if not has_number:
        return False, "Password must contain at least one number"
    
    return True, "Password is strong!"

print("Password Validator:")
passwords = ["abc123", "password", "mypass123", "str0ng!", "weak"]
for pwd in passwords:
    is_strong, message = is_strong_password(pwd)
    status = "✓" if is_strong else "✗"
    print(f"{status} '{pwd}': {message}")
print()

# Example 3: Temperature converter
def celsius_to_fahrenheit(celsius):
    """Converts Celsius to Fahrenheit"""
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    """Converts Fahrenheit to Celsius"""
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def convert_temperature(temp, scale):
    """Converts temperature between scales"""
    if scale.upper() == "C":
        converted = celsius_to_fahrenheit(temp)
        return f"{temp}°C = {converted:.1f}°F"
    elif scale.upper() == "F":
        converted = fahrenheit_to_celsius(temp)
        return f"{temp}°F = {converted:.1f}°C"
    else:
        return "Invalid scale. Use 'C' or 'F'"

print("Temperature Converter:")
print(convert_temperature(25, "C"))
print(convert_temperature(77, "F"))
print(convert_temperature(0, "C"))
print(convert_temperature(32, "F"))
print()

# Example 4: Simple calculator functions
def add(a, b):
    """Addition"""
    return a + b

def subtract(a, b):
    """Subtraction"""
    return a - b

def multiply(a, b):
    """Multiplication"""
    return a * b

def divide(a, b):
    """Division with zero check"""
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b

print("Calculator Functions:")
x, y = 12, 4
print(f"{x} + {y} = {add(x, y)}")
print(f"{x} - {y} = {subtract(x, y)}")
print(f"{x} × {y} = {multiply(x, y)}")
print(f"{x} ÷ {y} = {divide(x, y)}")
print(f"{x} ÷ 0 = {divide(x, 0)}")
print()

# =============================================================================
# PART 7: ADVANCED EXAMPLES
# =============================================================================
print("\n=== PART 7: ADVANCED EXAMPLES ===")

# Example 1: Text analyzer
def analyze_text(text):
    """Analyzes text and returns statistics"""
    words = len(text.split())
    chars_with_spaces = len(text)
    chars_without_spaces = len(text.replace(" ", ""))
    sentences = text.count('.') + text.count('!') + text.count('?')
    
    return {
        'words': words,
        'characters_with_spaces': chars_with_spaces,
        'characters_without_spaces': chars_without_spaces,
        'sentences': sentences
    }

sample_text = "Hello world! How are you today? This is a sample text for analysis."
print("Text Analysis:")
print(f"Text: {sample_text}")
stats = analyze_text(sample_text)
for key, value in stats.items():
    print(f"{key.replace('_', ' ').title()}: {value}")
print()

# Example 2: List statistics
def calculate_stats(numbers):
    """Calculates statistics for a list of numbers"""
    if not numbers:
        return "Empty list"
    
    total = sum(numbers)
    count = len(numbers)
    average = total / count
    minimum = min(numbers)
    maximum = max(numbers)
    
    return {
        'sum': total,
        'count': count,
        'average': round(average, 2),
        'minimum': minimum,
        'maximum': maximum
    }

print("List Statistics:")
sample_numbers = [10, 25, 8, 42, 17, 33, 5]
print(f"Numbers: {sample_numbers}")
stats = calculate_stats(sample_numbers)
for key, value in stats.items():
    print(f"{key.title()}: {value}")
print()

# Example 3: Fibonacci sequence
def fibonacci(n):
    """Returns the nth Fibonacci number"""
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print("Fibonacci Sequence:")
print("First 10 Fibonacci numbers:")
for i in range(10):
    print(f"F({i}) = {fibonacci(i)}")
print()

# Example 4: Prime number checker
def is_prime(number):
    """Checks if a number is prime"""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

print("Prime Number Checker:")
test_numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 17, 25, 29]
for num in test_numbers:
    result = "is prime" if is_prime(num) else "is not prime"
    print(f"{num} {result}")
print()

# =============================================================================
# PART 8: FUNCTION DOCUMENTATION AND BEST PRACTICES
# =============================================================================
print("\n=== PART 8: FUNCTION DOCUMENTATION ===")

def calculate_bmi(weight, height):
    """
    Calculate Body Mass Index (BMI)
    
    BMI is a measure of body fat based on height and weight.
    
    Args:
        weight (float): Weight in kilograms
        height (float): Height in meters
    
    Returns:
        dict: Dictionary containing BMI value and category
        
    Example:
        >>> bmi_info = calculate_bmi(70, 1.75)
        >>> print(bmi_info['bmi'])
        22.86
    """
    if height <= 0 or weight <= 0:
        return {"error": "Height and weight must be positive"}
    
    bmi = weight / (height ** 2)
    bmi = round(bmi, 2)
    
    # Determine BMI category
    if bmi < 18.5:
        category = "Underweight"
    elif bmi < 25:
        category = "Normal weight"
    elif bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return {
        'bmi': bmi,
        'category': category,
        'weight': weight,
        'height': height
    }

print("BMI Calculator (with comprehensive documentation):")
bmi_result = calculate_bmi(70, 1.75)
print(f"Weight: {bmi_result['weight']} kg")
print(f"Height: {bmi_result['height']} m")
print(f"BMI: {bmi_result['bmi']}")
print(f"Category: {bmi_result['category']}")

# Display the function's documentation
print("\nFunction documentation:")
print(calculate_bmi.__doc__)

print("\n" + "="*60)
print("END OF FUNCTION EXAMPLES")
print("="*60)