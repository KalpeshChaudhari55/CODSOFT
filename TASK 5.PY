class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"{self.name} - {self.phone} - {self.email} - {self.address}"


class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter contact name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        self.contacts[name] = Contact(name, phone, email, address)
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for contact in self.contacts.values():
                print(contact)

    def search_contact(self):
        search_query = input("Enter name or phone number to search: ")
        found = False
        for contact in self.contacts.values():
            if search_query.lower() in contact.name.lower() or search_query in contact.phone:
                print(contact)
                found = True
        if not found:
            print("No matching contacts found.")

    def update_contact(self):
        name = input("Enter the name of the contact to update: ")
        if name in self.contacts:
            contact = self.contacts[name]
            print(f"Updating contact: {contact}")
            contact.phone = input(f"Enter new phone number (current: {contact.phone}): ") or contact.phone
            contact.email = input(f"Enter new email (current: {contact.email}): ") or contact.email
            contact.address = input(f"Enter new address (current: {contact.address}): ") or contact.address
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    def delete_contact(self):
        name = input("Enter the name of the contact to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted successfully!")
        else:
            print("Contact not found.")


def show_menu():
    print("\nContact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")


def main():
    manager = ContactManager()
    while True:
        show_menu()
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            manager.add_contact()
        elif choice == '2':
            manager.view_contacts()
        elif choice == '3':
            manager.search_contact()
        elif choice == '4':
            manager.update_contact()
        elif choice == '5':
            manager.delete_contact()
        elif choice == '6':
            print("Exiting the Contact Manager. Goodbye!")
            break
        else:
            print("Invalid choice! Please select a valid option.")


if __name__ == "__main__":
    main()
