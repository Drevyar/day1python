def contact_book():
    contacts = {
        'John Doe': {'phone': '123-456-7890', 'email': 'john@example.com', 'category': 'friend'},
        'Jane Smith': {'phone': '987-654-3210', 'email': 'jane@example.com', 'category': 'work'},
    }

    def add_contact():
        print('\n=== Add New Contact ===')
        name = input('Enter contact name: ').strip()

        if name in contacts:
            choice = input('Contact already exists. Do you want to update it? (yes/no): ').strip().lower()
            if choice != 'yes':
                print('Contact not updated.')
                return
        else:
            print(f'Adding new contact: {name}')

        phone = input('Enter phone number: ').strip()
        email = input('Enter email address: ').strip()
        category = input('Enter category (family/friend/work/other): ').strip().lower()

        contacts[name] = {
            'phone': phone,
            'email': email,
            'category': category
        }
        print(f'Contact \'{name}\' added/updated successfully!')

    def view_contact():
        print('\n=== View Contact ===')
        name = input('Enter contact name: ').strip()

        if name in contacts:
            print('\n=== Contact Details ===')
            print(f'Name: {name}')
            print(f'Phone: {contacts[name]["phone"]}')
            print(f'Email: {contacts[name]["email"]}')
            print(f'Category: {contacts[name]["category"]}')
        else:
            print('Contact not found.')

    def search_contacts():
        print('\n=== Search Contacts ===')
        search_term = input('Enter search term (name/phone/email): ').strip()

        for name, details in contacts.items():
            if (search_term == name or
                search_term == details['phone'] or
                search_term == details['email']):
                print('\n=== Contact Details ===')
                print(f'Name: {name}')
                print(f'Phone: {details["phone"]}')
                print(f'Email: {details["email"]}')
                print(f'Category: {details["category"]}')
                return

        print('Contact not found.')

    def list_all_contacts():
        print('\n=== All Contacts ===')
        if not contacts:
            print('No contacts found.')
            return

        print(f'{"Name":<20} {"Phone":<15} {"Email":<25} {"Category":<10}')
        print('-' * 70)
        for name, details in contacts.items():
            print(f'{name:<20} {details["phone"]:<15} {details["email"]:<25} {details["category"]:<10}')

    def update_contact():
        print('\n=== Update Contact ===')
        name = input('Enter name: ').strip()

        if name in contacts:
            print('\n=== Contact Details ===')
            print(f'Name: {name}')
            print(f'Phone: {contacts[name]["phone"]}')
            print(f'Email: {contacts[name]["email"]}')
            print(f'Category: {contacts[name]["category"]}')

            print('\nWhich field do you want to update?')
            print('1. Phone')
            print('2. Email')
            print('3. Category')

            choice = input('Enter your choice (1-3): ').strip()

            if choice == '1':
                new_phone = input('Enter new phone number: ').strip()
                contacts[name]['phone'] = new_phone
            elif choice == '2':
                new_email = input('Enter new email: ').strip()
                contacts[name]['email'] = new_email
            elif choice == '3':
                new_category = input('Enter new category: ').strip()
                contacts[name]['category'] = new_category
            else:
                print('Invalid choice.')

            print(f'\nContact \'{name}\' updated successfully!')
        else:
            print('Contact not found.')

    def delete_contact():
        print('\n=== Delete Contact ===')
        name = input('Enter contact name to delete: ').strip()

        if name not in contacts:
            print('No contacts found!')
            return

        confirm = input(f'Are you sure you want to delete \'{name}\'? (yes/no): ').strip().lower()
        if confirm == 'yes':
            del contacts[name]
            print(f'Contact \'{name}\' deleted successfully!')
        else:
            print('Delete cancelled.')

    while True:
        print('\n=== Contact Book Menu ===')
        print('1. Add Contact')
        print('2. View Contact')
        print('3. Search Contacts')
        print('4. List All Contacts')
        print('5. Update Contact')
        print('6. Delete Contact')
        print('7. Exit')
        print('-' * 50)

        choice = input('Enter your choice (1-7): ').strip()

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contact()
        elif choice == '3':
            search_contacts()
        elif choice == '4':
            list_all_contacts()
        elif choice == '5':
            update_contact()
        elif choice == '6':
            delete_contact()
        elif choice == '7':
            print('Thank you for using Contact Book Manager!')
            break
        else:
            print('Invalid choice.')

if __name__ == '__main__':
    print('Starting Contact Book Manager...')
    contact_book()
