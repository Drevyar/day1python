friend = []
while True:
    try:
        n = int(input('How many friend you want to enter :'))
        if n <= 0:
            print('plase try again.')
            continue
        else:
            break
    except ValueError:
        print('Please enter a valid number.')
        
for i in range(n):
    name = input(f'Friend {i+1} : ').strip()
    friend.append(name)
    
print('===== display =====')
for f in friend:
    print(f)