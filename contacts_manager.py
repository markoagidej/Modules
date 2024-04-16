
def add_contact(contact_list):
    name = input("Enter the name of your new contact: ")
    contact_list.append(name)
    return contact_list


def remove_contact(contact_list):
    print("Displaying contacts to remove:")
    # contacts = enumerate(contact_list, 1)
    for number, name in enumerate(contact_list, 1):
        print(f"{number}. {name}")
        
    try:
        to_remove = int(input("Choose the number of the contact you would like to remove: "))
    except:
        print("Enter a number from the contact list!")
        return contact_list
    else:
        for number, name in enumerate(contact_list, 1):
            if to_remove == number:
                del contact_list[number - 1]
                return contact_list
            
        print("Enter only a number seen in the contact list!")
        return contact_list
    

def display_contacts(contact_list):
    for contact in contact_list:
        print(contact)