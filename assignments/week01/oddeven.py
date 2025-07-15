
num = []
odd = []
even = []

while True:
    try:
        
        x1 = int(input('How many number do u want to enter :'))
        if x1 < 0:
            print('number must more than 0.')
            continue
        
        for i in range(1, x1 + 1):
            while True:
                try:
                    number = int(input(f'Number {i} : '))
                    if number < 0:
                        print('number must more than 0.')
                        continue
                    break
                except ValueError:
                    print('Please enter a valid number.')
                    continue
            num.append(number)
            if number % 2 == 0:
                even.append(number)
            else:
                odd.append(number)
                
        print(f'Even numbers : {even}')
        print(f'Odd numbers : {odd}')
        print(f'Total numbers : {num}')
        print(f"Sum of even numbers: {sum(even)}")
        print(f"Sum of odd numbers: {sum(odd)}")
        print(f'Total sum of number : {sum(num)}')
        break
            
    except ValueError:
        print('Please enter number.')
        continue

    jdnwjdnwjndjwdnjw