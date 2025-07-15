# =============================================================================
# DEMO 1: Basic Arithmetic Operators
# =============================================================================

print("=" * 50)
print("DEMO 1: Basic Arithmetic Operators")
print("=" * 50)

a = 15
b = 4

print(f"a = {a}, b = {b}")
print()

# Addition (+)
result_add = a + b
print(f"Addition:       {a} + {b} = {result_add}")

# Subtraction (-)
result_sub = a - b
print(f"Subtraction:    {a} - {b} = {result_sub}")

# Multiplication (*)
result_mul = a * b
print(f"Multiplication: {a} * {b} = {result_mul}")

# Division (/)
result_div = a / b
print(f"Division:       {a} / {b} = {result_div}")

# Floor Division (//)
result_floor = a // b
print(f"Floor Division: {a} // {b} = {result_floor}")

# Modulo (%)
result_mod = a % b
print(f"Modulo:         {a} % {b} = {result_mod}")

# Exponentiation (**)
result_exp = a ** b
print(f"Exponentiation: {a} ** {b} = {result_exp}")

print()

# =============================================================================
# DEMO 2: Interactive Calculator
# =============================================================================

print("=" * 50)
print("DEMO 2: Interactive Calculator")
print("=" * 50)

# รับ input จากผู้ใช้
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print(f"\nCalculations with {num1} and {num2}:")
print(f"{num1} + {num2} = {num1 + num2}")
print(f"{num1} - {num2} = {num1 - num2}")
print(f"{num1} * {num2} = {num1 * num2}")

# ตรวจสอบการหารด้วยศูนย์
if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
    print(f"{num1} // {num2} = {num1 // num2}")
    print(f"{num1} % {num2} = {num1 % num2}")
else:
    print("Cannot divide by zero!")

print(f"{num1} ** {num2} = {num1 ** num2}")

print()

# =============================================================================
# DEMO 3: Operator Precedence
# =============================================================================

print("=" * 50)
print("DEMO 3: Operator Precedence")
print("=" * 50)

# ตัวอย่างลำดับการคำนวณ
expression1 = "2 + 3 * 4"
result1 = 2 + 3 * 4
print(f"{expression1} = {result1}")
print("Explanation: * has higher precedence than +")
print("So: 2 + (3 * 4) = 2 + 12 = 14")
print()

expression2 = "(2 + 3) * 4"
result2 = (2 + 3) * 4
print(f"{expression2} = {result2}")
print("Explanation: Parentheses have highest precedence")
print("So: (2 + 3) * 4 = 5 * 4 = 20")
print()

expression3 = "2 ** 3 * 4"
result3 = 2 ** 3 * 4
print(f"{expression3} = {result3}")
print("Explanation: ** has higher precedence than *")
print("So: (2 ** 3) * 4 = 8 * 4 = 32")
print()

expression4 = "10 / 2 * 3"
result4 = 10 / 2 * 3
print(f"{expression4} = {result4}")
print("Explanation: / and * have same precedence, evaluate left to right")
print("So: (10 / 2) * 3 = 5.0 * 3 = 15.0")
print()

# =============================================================================
# DEMO 4: Practical Examples
# =============================================================================

print("=" * 50)
print("DEMO 4: Practical Examples")
print("=" * 50)

# ตัวอย่างที่ 1: คำนวณพื้นที่และปริมตรสี่เหลี่ยม
print("Rectangle Calculator")
print("-" * 20)
length = float(input("Enter rectangle length: "))
width = float(input("Enter rectangle width: "))

area = length * width
perimeter = 2 * (length + width)

print(f"Area = length * width = {length} * {width} = {area}")
print(f"Perimeter = 2 * (length + width) = 2 * ({length} + {width}) = {perimeter}")
print()

# ตัวอย่างที่ 2: แปลงหน่วยอุณหภูมิ
print("Temperature Converter")
print("-" * 25)
celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32
kelvin = celsius + 273.15

print(f"Celsius: {celsius}°C")
print(f"Fahrenheit: (celsius * 9/5) + 32 = ({celsius} * 9/5) + 32 = {fahrenheit}°F")
print(f"Kelvin: celsius + 273.15 = {celsius} + 273.15 = {kelvin}K")
print()

# ตัวอย่างที่ 3: คำนวณค่าใช้จ่ายแบ่งเท่าๆ กัน
print("Bill Splitter")
print("-" * 15)
total_bill = float(input("Enter total bill amount: "))
num_people = int(input("Enter number of people: "))
tip_percent = float(input("Enter tip percentage (e.g., 15 for 15%): "))

tip_amount = total_bill * (tip_percent / 100)
total_with_tip = total_bill + tip_amount
amount_per_person = total_with_tip / num_people

print(f"\nBill Breakdown:")
print(f"Original bill: ${total_bill}")
print(f"Tip ({tip_percent}%): ${tip_amount:.2f}")
print(f"Total with tip: ${total_with_tip:.2f}")
print(f"Amount per person: ${amount_per_person:.2f}")
print()

# =============================================================================
# DEMO 5: Special Division Cases
# =============================================================================

print("=" * 50)
print("DEMO 5: Division Types Explained")
print("=" * 50)

dividend = 17
divisor = 5

print(f"Given: {dividend} ÷ {divisor}")
print()

# Regular division (/)
regular_div = dividend / divisor
print(f"Regular division (/):")
print(f"{dividend} / {divisor} = {regular_div}")
print("Result: Float number (decimal)")
print()

# Floor division (//)
floor_div = dividend // divisor
print(f"Floor division (//):")
print(f"{dividend} // {divisor} = {floor_div}")
print("Result: Integer (rounded down)")
print()

# Modulo (%)
modulo = dividend % divisor
print(f"Modulo (%):")
print(f"{dividend} % {divisor} = {modulo}")
print("Result: Remainder after division")
print()

# Verification
print("Verification:")
print(f"{divisor} * {floor_div} + {modulo} = {divisor * floor_div + modulo}")
print(f"Should equal {dividend}")
print()

# =============================================================================
# DEMO 6: Common Mistakes and Debugging
# =============================================================================

print("=" * 50)
print("DEMO 6: Common Mistakes")
print("=" * 50)

# Mistake 1: Integer division in older Python versions
print("Watch out for division:")
print("In Python 3: 5 / 2 =", 5 / 2, "(float)")
print("Floor division: 5 // 2 =", 5 // 2, "(integer)")
print()

# Mistake 2: Operator precedence
print("Remember operator precedence:")
print("2 + 3 * 4 =", 2 + 3 * 4, "(not 20!)")
print("(2 + 3) * 4 =", (2 + 3) * 4, "(use parentheses)")
print()

# Mistake 3: Division by zero
print("Division by zero:")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("10 / 0 = Error! Cannot divide by zero")
print()

# Mistake 4: Very large numbers
print("Very large numbers:")
large_num = 2 ** 100
print(f"2 ** 100 = {large_num}")
print("Python can handle very large integers!")
print()

# =============================================================================
# PRACTICE EXERCISES (FOR STUDENTS)
# =============================================================================

print("=" * 50)
print("PRACTICE EXERCISES")
print("=" * 50)

print("Now try these exercises:")
print()
print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

print("3. Compound Interest Calculator:")
print("   - Ask for principal, rate, and time")
print("   - Calculate: A = P * (1 + r/100) ** t")
print()

print("4. BMI Calculator:")
print("   - Ask for weight (kg) and height (m)")
print("   - Calculate: BMI = weight / (height ** 2)")
print()

print("5. Grade Average:")
print("   - Ask for 3 test scores")
print("   - Calculate average")
print("   - Show how many points needed for next letter grade")

# =============================================================================
# STARTER CODE TEMPLATES
# =============================================================================

print("\n" + "=" * 50)
print("STARTER CODE TEMPLATES")
print("=" * 50)

# Template 1: Circle Calculator
circle_calculator = '''
# Circle Calculator Template
import math

radius = float(input("Enter radius: "))

# TODO: Calculate area (π * r²)
# TODO: Calculate circumference (2 * π * r)
# TODO: Display results

# Hint: Use math.pi for more accurate π value
'''

# Template 2: Time Converter
time_converter = '''
# Time Converter Template

total_seconds = int(input("Enter total seconds: "))

# TODO: Calculate hours (hint: use // operator)
# TODO: Calculate remaining minutes
# TODO: Calculate remaining seconds
# TODO: Display in format "X hours, Y minutes, Z seconds"

# Hint: Use % operator for remainders
'''

# Template 3: Shopping Calculator
shopping_calculator = '''
# Shopping Calculator Template

item_price = float(input("Enter item price: "))
quantity = int(input("Enter quantity: "))
discount_percent = float(input("Enter discount %: "))
tax_percent = float(input("Enter tax %: "))

# TODO: Calculate subtotal
# TODO: Calculate discount amount
# TODO: Calculate price after discount
# TODO: Calculate tax amount
# TODO: Calculate final total
# TODO: Display itemized receipt
'''

print("Copy these templates to practice!")