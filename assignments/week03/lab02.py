balance = 1000
pin = 1234

while True:
    try:
        entered_pin = int(input('Enter PIN: '))
        if entered_pin == pin:
            print('PIN accepted')
            break
        else:
            print('Invalid PIN')
    except ValueError:
        print('Please enter PIN again.')


while True:
    try:
        print('\n1. Check Balance')
        print('2. Withdraw')
        print('3. Deposit')
        print('4. Exit')
        
        choice = int(input('Choose option: ')) 
        if choice == 1:
            print(f'Your balance is: {balance}')
        elif choice == 2:
            amount = int(input('Enter amount to withdraw: '))
            if amount > balance:
                print(f'You have {balance} in your balance')
            elif amount <= 0:
                print('Amount must be positive')
            else:
                balance -= amount
                print(f'Withdrew {amount}. New balance: {balance}')
        elif choice == 3:
            amount = int(input('Enter amount to deposit: '))
            if amount <= 0:
                print('Amount must be positive')
            else:
                balance += amount
                print(f'Deposited {amount}. New balance: {balance}')
        elif choice == 4:
            print('Thank you.')
            break
        else:
            print('Invalid choice.')
    except ValueError:
        print('Invalid choice. Please enter a number.')