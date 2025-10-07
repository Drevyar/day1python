"""
Create a grade processing system with the following requirements:

A global variable passing_grade = 50

(1) A function input_students(num_students) that:

- Creates and returns a list of dictionaries
- Each dictionary contains: {'name': str, 'scores': [list of 3 scores]}

(2) A function calculate_averages(students) that:

- Uses nested loops to calculate each student's average
- Adds an 'average' key to each student dictionary
- Modifies the original list (demonstrate list mutability)

(3) A function display_results(students) that:

- Loops through students
- Uses the global passing_grade to determine pass/fail
- Prints each student's name, average, and status (PASS/FAIL)
"""


passing_grade = 50 

 
def input_students(num_students):
    students = []
    for i in range(num_students):
        print(f'Enter student {i+1}')
        name = input('Name: ')

        scores = []
        for j in range(3):
            score = float(input(f'Enter score {j+1}: '))
            scores.append(score)
        
        student_data = {
            'name': name,
            'scores': scores
        }

        students.append(student_data)
    return students

def calculate_averages(students):
    for student in students:
        total = 0
        for score in student['scores']:
            total += score
        avg = total / len(student['scores'])
        student['average'] = avg

try:
    num = int(input("Enter number of students: "))
    students = input_students(num)
    calculate_averages(students)

    print("\nStudent Results:")
    for student in students:
        if student['average'] >= passing_grade:
            status = "PASS"
        else:
            status = "FAIL"
        print(f"{student['name']} - Average: {student['average']:.1f} - {status}")

except ValueError:
    print("Invalid input. Please enter a number.")
