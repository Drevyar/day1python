person_info = ("Morfor", 19, "Bangkok", "Thailand")
hobbies = ["Reading", "Traveling"]

while True:
    print("\n--- Personal Information Manager ---")
    print("1. Display all information")
    print("2. Add new hobby")
    print("3. Remove hobby")
    print("4. Update age")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        print("\n--- All Information ---")
        print(f"Name: {person_info[0]}")
        print(f"Age: {person_info[1]}")
        print(f"City: {person_info[2]}")
        print(f"Country: {person_info[3]}")
        print(f"Hobbies: {hobbies}")

    elif choice == "2":
        new_hobby = input("Enter new hobby: ")
        hobbies.append(new_hobby)
        print("Hobby added successfully!")

    elif choice == "3":
        remove_hobby = input("Enter hobby to remove: ")
        if remove_hobby in hobbies:
            hobbies.remove(remove_hobby)
            print("Hobby removed successfully!")
        else:
            print("Hobby not found!")

    elif choice == "4":
        new_age = int(input("Enter new age: "))
        person_info = (person_info[0], new_age, person_info[2], person_info[3])
        print("Age updated successfully!")
        break
    
    else:
        print("Invalid choice, please try again.")
