while True:
    try:
        age = int(input("Enter age: "))
        if age < 0:
            print("Age must more than 0.")
        elif age <= 12:
            print("0-12: Child")
        elif age <= 19:
            print("13-19: Teenager")
        elif age <= 59:
            print("20-59: Adult")
        else:
            print("60+: Senior")
            break
    except ValueError:
        print("Invalid age")