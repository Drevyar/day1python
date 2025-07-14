print("\n=== Student Grade Calculator ===")

while True:
    try:
        s_mathematics = float(input('what is your mathematics scrore ?/100 :'))
        if s_mathematics < 0 or s_mathematics > 100:
            print('Please enter a score between 0 and 100.')
            continue
        
        s_english = float(input('what is your english scrore ?/100 :'))
        if s_english < 0 or s_english > 100:
            print('Please enter a score between 0 and 100.')
            continue
        
        s_science = float(input('what is your science scrore ?/100 :'))
        if s_science < 0 or s_science > 100:
            print('Please enter a score between 0 and 100.')
            continue
        
        average = (s_mathematics + s_english + s_science) / 3
        print(f"Your average score is: {average:.2f}")
        break
    
    except ValueError:
        print("Please enter valid numbers.")
        continue