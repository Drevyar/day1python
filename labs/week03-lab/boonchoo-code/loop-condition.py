# =============================================================================
# Week 5: Loops & Conditional Statements - Complete Solutions
# =============================================================================

# =============================================================================
# DEMO CODE (สำหรับอาจารย์ใช้สอนในชั้นเรียน)
# =============================================================================

# demo_for_basic.py
print("=== Demo 1: Basic For Loop ===")

# Loop ผ่านตัวเลข
print("นับจาก 1 ถึง 5:")
for i in range(1, 6):
    print(f"รอบที่ {i}")

print("\nนับแบบขั้น:")
for i in range(0, 11, 2):  # 0, 2, 4, 6, 8, 10
    print(f"เลขคู่: {i}")

print("\nLoop ผ่าน string:")
name = "Python"
for letter in name:
    print(f"ตัวอักษร: {letter}")

print("\nLoop ผ่าน list:")
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(f"ผลไม้: {fruit}")

print("=" * 50)

# =============================================================================

# demo_while_basic.py
print("=== Demo 2: Basic While Loop ===")

# นับด้วย while
print("นับจาก 1 ถึง 5 ด้วย while:")
count = 1
while count <= 5:
    print(f"รอบที่ {count}")
    count += 1  # เพิ่มค่า count

print("\nDemo while กับ input (จำลอง):")
# จำลองการใช้งานโดยไม่ต้อง input จริง
responses = ["hello", "world", "quit"]
for simulated_input in responses:
    print(f"ผู้ใช้พิมพ์: {simulated_input}")
    if simulated_input != "quit":
        print(f"คุณพิมพ์: {simulated_input}")
    else:
        print("จบแล้ว!")
        break

print("=" * 50)

# =============================================================================

# demo_loops_conditions.py
print("=== Demo 3: Loops + Conditions ===")

# หาเลขคู่และคี่
print("แยกเลขคู่-คี่:")
for num in range(1, 11):
    if num % 2 == 0:
        print(f"{num} เป็นเลขคู่")
    else:
        print(f"{num} เป็นเลขคี่")

print("\nDemo เกมทายตัวเลข (จำลอง):")
import random
secret_number = 7  # ใช้เลขตายตัวเพื่อ demo
guesses = [5, 8, 7]  # จำลองการทาย
attempts = 0
max_attempts = 3

print(f"เลขลับคือ: {secret_number}")
for guess in guesses:
    attempts += 1
    print(f"ทายครั้งที่ {attempts}: {guess}")
    
    if guess == secret_number:
        print("🎉 ถูกต้อง!")
        break
    elif guess < secret_number:
        print("น้อยไป")
    else:
        print("มากไป")
    
    if attempts == max_attempts:
        print(f"หมดโอกาส! คำตอบคือ {secret_number}")

print("=" * 50)

# =============================================================================
# GUIDED PRACTICE SOLUTIONS
# =============================================================================

# solution_patterns.py
print("=== Pattern Generator - Solution ===")

# Pattern 1: Square numbers
print("1. กำลังสอง:")
for i in range(1, 6):
    square = i ** 2
    print(f"{i}² = {square}")

print("\n2. นับถอยหลัง:")
for i in range(10, -1, -1):  # 10 down to 0
    print(i, end=" ")
print()  # New line

print("\n3. สูตรคูณแม่ 7:")
for i in range(1, 13):
    result = 7 * i
    print(f"7 × {i} = {result}")

print("=" * 50)

# =============================================================================

# solution_validation.py
print("=== Input Validation - Solution ===")

# จำลองการตรวจสอบ input โดยไม่ใช้ input() จริง
print("1. ตรวจสอบอายุ (1-100):")
test_ages = [-5, 0, 25, 150, 30]  # จำลองข้อมูล
for age in test_ages:
    print(f"ทดสอบอายุ: {age}")
    if 1 <= age <= 100:
        print("✅ อายุถูกต้อง")
        break
    else:
        print("❌ อายุต้องอยู่ระหว่าง 1-100")

print("\n2. ตรวจสอบเกรด (A, B, C, D, F):")
test_grades = ["X", "G", "A"]  # จำลองข้อมูล
valid_grades = ["A", "B", "C", "D", "F"]
for grade in test_grades:
    print(f"ทดสอบเกรด: {grade}")
    if grade.upper() in valid_grades:
        print("✅ เกรดถูกต้อง")
        break
    else:
        print("❌ เกรดต้องเป็น A, B, C, D, หรือ F")

print("\n3. ตรวจสอบตัวเลขบวก:")
test_numbers = [-5, 0, 10]  # จำลองข้อมูล
for num in test_numbers:
    print(f"ทดสอบตัวเลข: {num}")
    if num > 0:
        print("✅ ตัวเลขบวกถูกต้อง")
        break
    else:
        print("❌ ต้องเป็นตัวเลขบวก")

print("=" * 50)

# =============================================================================

# solution_menu.py
print("=== Simple Calculator Menu - Solution ===")

# จำลองการใช้งานเมนู
menu_choices = ["1", "3", "5"]  # จำลองการเลือก
numbers = [(10, 5), (8, 4), (0, 0)]  # จำลองข้อมูล

choice_index = 0
for choice in menu_choices:
    print(f"\n--- เมนู ---")
    print("1. บวก")
    print("2. ลบ")
    print("3. คูณ")
    print("4. หาร")
    print("5. ออก")
    
    print(f"เลือก: {choice}")
    
    if choice == "1":
        a, b = numbers[choice_index]
        result = a + b
        print(f"{a} + {b} = {result}")
    elif choice == "2":
        a, b = numbers[choice_index]
        result = a - b
        print(f"{a} - {b} = {result}")
    elif choice == "3":
        a, b = numbers[choice_index]
        result = a * b
        print(f"{a} × {b} = {result}")
    elif choice == "4":
        a, b = numbers[choice_index]
        if b != 0:
            result = a / b
            print(f"{a} ÷ {b} = {result}")
        else:
            print("ไม่สามารถหารด้วยศูนย์ได้")
    elif choice == "5":
        print("ลาก่อน!")
        break
    else:
        print("ตัวเลือกไม่ถูกต้อง")
    
    choice_index += 1

print("=" * 50)

# =============================================================================
# MAIN PROJECT SOLUTIONS
# =============================================================================

# solution_grade_analyzer.py
print("=== Student Grade Analyzer - Solution ===")

# จำลองข้อมูลเกรด
scores = [85, 92, 78, 67, 95, 73, 88, 54, 91, 82]
num_students = len(scores)

print(f"วิเคราะห์เกรดของ {num_students} คน")
print(f"คะแนน: {scores}")

# คำนวณสถิติ
total_score = 0
highest_score = scores[0]
lowest_score = scores[0]
passing_students = 0

for score in scores:
    total_score += score
    if score > highest_score:
        highest_score = score
    if score < lowest_score:
        lowest_score = score
    if score >= 60:
        passing_students += 1

average = total_score / num_students

# แสดงผลลัพธ์
print(f"\n=== สรุปผลการสอบ ===")
print(f"จำนวนนักเรียน: {num_students} คน")
print(f"คะแนนเฉลี่ย: {average:.2f}")
print(f"คะแนนสูงสุด: {highest_score}")
print(f"คะแนนต่ำสุด: {lowest_score}")
print(f"ผ่านการสอบ: {passing_students} คน")
print(f"ไม่ผ่านการสอบ: {num_students - passing_students} คน")

# การแจกแจงเกรด
grade_counts = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0}

for score in scores:
    if score >= 80:
        grade_counts["A"] += 1
    elif score >= 70:
        grade_counts["B"] += 1
    elif score >= 60:
        grade_counts["C"] += 1
    elif score >= 50:
        grade_counts["D"] += 1
    else:
        grade_counts["F"] += 1

print(f"\n=== การแจกแจงเกรด ===")
for grade, count in grade_counts.items():
    percentage = (count / num_students) * 100
    print(f"เกรด {grade}: {count}")