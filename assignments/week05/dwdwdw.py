students {}

try:
    n = int(input('How many student you want to input :'))
    for i in range(n):
        
    sid = int(input(f'Student Id {i+1}: '))
    name = input(f'Student name {i+1} : ')
    students[sid] = name
except ValueError:
    print('Invalid ')
    
    print(===== Display =====)
    for sid, name in students.items():
        print(f'Id : {sid} | Name : {name}')
        
search_id = input("\nEnter student ID to search: ").strip()
if search_id in students:
    print(f"Student found: {students[search_id]}")
else:
    print("Student not found.")
        