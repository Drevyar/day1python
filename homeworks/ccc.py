fruits = ('Aplle', 'Mango', ' Banana', 'Orange')

while True:
    try:
        print('===== Menu =====')
        print('1. Display all fruits')
        print('2. Add fruits')
        print('3. Remove fruits ')
        print('4. Exit')
        
        choice = int(input('Enter your choice :'))
        
        if choice == 1:
            print(fruits)
        elif choice == 2:
            new = input('Enter fruits :').strip()
            fruits.__add__(new)
        elif choice == 3:
            print(fruits)
            remove = input('Which fruits do you want to delete :')
            fruits.
        