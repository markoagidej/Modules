# Task 1: Contact List Manager

import contacts_manager

contacts = ["Dude", "Dudette"]

while True:
    print("Contact Manager")
    print("1. Add Contact")
    print("2. Remove Contact")
    print("3. Display Contacts")
    print("4. Quit")
    choice = input("Enter the number of a menu option: ")

    if choice == "1":
        contacts = contacts_manager.add_contact(contacts)
    elif choice == "2":
        contacts = contacts_manager.remove_contact(contacts)
    elif choice == "3":
        print("Displaying Contacts:")
        contacts_manager.display_contacts(contacts)
    elif choice == "4":
        print("Goodbye!")
        quit()
    else:
        print("Not a valid choice!")

    print("")