yourtrolley = ['Chip', 'Orange']

def addTrolley(): #เพิ่มของ
    print('===== Add Trolley =====')
    while True:
        newitem = input('Enter your new item (or "quit" to stop): ').strip()
        if newitem.lower() == 'quit':
            break
        if newitem:  # ตรวจสอบว่า input ไม่ว่าง
            yourtrolley.append(newitem)
            print('===== Your new trolley =====')
            print(yourtrolley)
            while True:  # ลูปย่อยสำหรับถาม yes/no
                choice = input('Do you want to add more item? (yes/no): ').strip().lower()
                if choice in ['yes', 'no']:
                    break
                print('Please answer yes or no.')
            if choice == 'no':
                break
        else:
            print('Please enter a valid item!')
            
def displayTrolley(): #แสดงของ
    print('===== Display Trolley =====')
    print(f'{yourtrolley}')
    
def removeitem():
    print('===== Remove Item =====')
    while True:
        print(f'{yourtrolley}')
        item = input('Which item do you want to remove? (or "quit" to stop): ').strip().lower()
        if item.lower() == 'quit':
            break
        if item in yourtrolley:
            yourtrolley.remove(item)
            print(yourtrolley)
        else:
            print('Item not found in trolley!')

while True:
    print('===== Your Trolley =====')
    print('1. Add Trolley')
    print('2. Display Trolley')
    print('3. Remove Item')
    print('4. Exit')
    choice = input('Enter your choice: ').strip()
    try:
        choice = int(choice)
        if choice == 1:
            addTrolley()
        elif choice == 2:
            displayTrolley()
        elif choice == 3:
            removeitem()
        elif choice == 4:
            print('Thank you.')
            break
        else:
            print('Invalid choice! Please enter 1.')
    except ValueError:
        print('Please enter a valid number!')