
odd = []
even = []

while True:
    try:
        
        x1 = int(input('How many number do u want to enter :'))
        if x1 < 0:
            print('number must more than 0.')
            continue
        
        for i in range(1, x1 + 1):
            number = int(input(f'Number {i} : '))
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
                
        print(f'Even numbers : {even}')
        print(f'Odd numbers : {odd}')
        print(f"Sum of even numbers: {sum(even)}")
        print(f"Sum of odd numbers: {sum(odd)}")
        break
            
    except ValueError:
        print('Please enter number.')
        continue