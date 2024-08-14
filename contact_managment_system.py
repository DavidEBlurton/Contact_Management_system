import re

contacts = {}

def display_menu():
    print('''\nContact Management System

    1. Add a new contact
    2. Edit an existing contact
    3. Delete a contact
    4. Search for a contact
    5. Display all contacts
    6. Export contacts to a text file
    7. Import contacts from a text file
    8. Quit''')
    return input("\nChoose an option: ")

def validate_phone(phone):
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return pattern.match(phone)

def validate_email(email):
    pattern = re.compile(r'^[\w\.-]+@[\w\.-]+\.\w+$')
    return pattern.match(email)

def add_contact():
    print("\nAdd a New Contact")
    name = input("Name: ")
    phone = input("Phone (format 123-456-7890): ")
    if not validate_phone(phone):
        print("Invalid phone number format.")
        return
    email = input("Email: ")
    if not validate_email(email):
        print("Invalid email format.")
        return
    address = input("Address: ")
    notes = input("Notes: ")

    contacts[email] = {
        'name': name,
        'phone': phone,
        'address': address,
        'notes': notes
    }
    print("Contact added successfully.")

def edit_contact():
    print("\nEdit a Contact")
    email = input("Enter the contact's email: ")
    if email not in contacts:
        print("Contact not found.")
        return
    
    name = input("New Name (press Enter to keep current): ")
    phone = input("New Phone (press Enter to keep current, format 123-456-7890): ")
    if phone and not validate_phone(phone):
        print("Invalid phone number format.")
        return
    email = input("New Email (press Enter to keep current): ")
    if email and not validate_email(email):
        print("Invalid email format.")
        return
    address = input("New Address (press Enter to keep current): ")
    notes = input("New Notes (press Enter to keep current): ")

    contact = contacts[email]
    if name:
        contact['name'] = name
    if phone:
        contact['phone'] = phone
    if address:
        contact['address'] = address
    if notes:
        contact['notes'] = notes

    print("Contact updated successfully.")

def delete_contact():
    print("\nDelete a Contact")
    email = input("Enter the contact's email: ")
    if email in contacts:
        del contacts[email]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")

def search_contact():
    print("\nSearch for a Contact")
    email = input("Enter the contact's email: ")
    if email in contacts:
        contact = contacts[email]
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Address: {contact['address']}")
        print(f"Notes: {contact['notes']}")
    else:
        print("Contact not found.")

def display_all_contacts():
    print("\nAll Contacts")
    for email, details in contacts.items():
        print(f"\nEmail: {email}")
        print(f"Name: {details['name']}")
        print(f"Phone: {details['phone']}")
        print(f"Address: {details['address']}")
        print(f"Notes: {details['notes']}")

def export_contacts():
    pass

def import_contacts():
    pass

def main():
    while True:
        choice = display_menu()
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            edit_contact()
        elif choice == '3':
            delete_contact()
        elif choice == '4':
            search_contact()
        elif choice == '5':
            display_all_contacts()
        elif choice == '6':
            export_contacts()
        elif choice == '7':
            import_contacts()
        elif choice == '8':
            print("Quitting the program.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == '__main__':
    main()