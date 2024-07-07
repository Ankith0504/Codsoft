class ContactBook:
    def _init_(self):
        self.contacts = []

    def add_contact(self, name, phone, email, address):
        contact = {'name': name, 'phone': phone, 'email': email, 'address': address}
        self.contacts.append(contact)

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
        else:
            for i, contact in enumerate(self.contacts, start=1):
                print(f"{i}. {contact['name']} - {contact['phone']}, {contact['email']}, {contact['address']}")

    def search_contact(self, search_term):
        results = [contact for contact in self.contacts if search_term.lower() in contact['name'].lower() or search_term in contact['phone']]
        if not results:
            print("No contacts found.")
        else:
            for contact in results:
                print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

    def update_contact(self, name, new_phone, new_email, new_address):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                contact['phone'] = new_phone
                contact['email'] = new_email
                contact['address'] = new_address
                print("Contact updated successfully.")
                return
        print("Contact not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact['name'].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return
        print("Contact not found.")

def main():
    contact_book = ContactBook()
    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact_book.add_contact(name, phone, email, address)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ")
            contact_book.search_contact(search_term)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            new_phone = input("Enter new phone number: ")
            new_email = input("Enter new email: ")
            new_address = input("Enter new address: ")
            contact_book.update_contact(name, new_phone, new_email, new_address)
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
        elif choice == '6':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if _name_ == "_main_":
    main()