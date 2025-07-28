while True:
    try:
        name = str(input("Enter your name :"))
        
        age = int(input("How old are you :"))
        if age < 0:
            print("please try agin.")
            continue
            
        grade = int(input("What is your grade :"))
        break
        
    except ValueError:
        print("Pleas try again.")