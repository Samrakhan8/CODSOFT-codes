contacts = []

def add_contact():
    print("\n--- Add Contact ---")
    name = input("Name: ")
    phone = input("Phone Number: ")
    email = input("Email: ")
    address = input("Address: ")
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    })
    print("Contact added successfully.")

def view_contacts():
    print("\n--- Contact List ---")
    if not contacts:
        print("No contacts found.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. {contact['name']} - {contact['phone']}")

def search_contact():
    query = input("Search by name or phone number: ").lower()
    found = False
    for contact in contacts:
        if query in contact['name'].lower() or query in contact['phone']:
            print("\n--- Contact Found ---")
            print(f"Name   : {contact['name']}")
            print(f"Phone  : {contact['phone']}")
            print(f"Email  : {contact['email']}")
            print(f"Address: {contact['address']}")
            found = True
            break
    if not found:
        print("No contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print("Leave field empty to keep current value.")
            new_name = input(f"New name ({contact['name']}): ") or contact['name']
            new_phone = input(f"New phone ({contact['phone']}): ") or contact['phone']
            new_email = input(f"New email ({contact['email']}): ") or contact['email']
            new_address = input(f"New address ({contact['address']}): ") or contact['address']
            
            contact.update({
                "name": new_name,
                "phone": new_phone,
                "email": new_email,
                "address": new_address
            })
            print("Contact updated.")
            return
    print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ").lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            contacts.remove(contact)
            print("Contact deleted.")
            return
    print("Contact not found.")

def show_menu():
    print("\n--- Contact Book Menu ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

# Main Loop
while True:
    show_menu()
    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")
