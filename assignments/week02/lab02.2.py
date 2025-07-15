print('============ Currency Converter ============')

while True:
    try:
        choice = int(input('Which choice do you want? 1.THB to USD or 2.USD to THB : '))
        
        if choice == 1:
            print("You chose: THB to USD")
            
            while True:
                try:
                    bath = float(input('How many bath :'))
                    if bath > 0:
                        usd = bath / 35.5
                        print(f"{bath:.2f} THB = {usd:.2f} USD")
                        break
                    else:
                        print("Bath must more than 0.")
                except ValueError:
                    print("Invalid")


        elif choice == 2:
            print("You chose: USD to THB")

            while True:
                try:
                    usd = float(input('How many dollar :'))
                    if usd > 0:
                        bath = usd * 35.5
                        print(f"{usd:.2f} USD = {bath:.2f} THB")
                        break
                    else:
                        print('Dollar must more than 0.')
                except ValueError:
                    print('Invalid')

        else:
            print('Invalid choice. Please enter 1 or 2.')

    except ValueError:
        print("Invalid input. Please enter a number.")
