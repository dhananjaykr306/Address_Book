"""
    @Author: Dhananjay Kumar
    @Date: 11-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 11-11-2024
    @Title : Address Book 

"""
import logger

log = logger.logger_init('AddressBook')

class Contact:
    def __init__(self):
        self.first_name = input("Enter first name: ")
        self.last_name = input("Enter last name: ")
        self.address = input("Enter address: ")
        self.city = input("Enter city: ")
        self.state = input("Enter state: ")
        self.zip_code = input("Enter ZIP code: ")
        self.phone = input("Enter phone number: ")
        self.email = input("Enter email address: ")

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.address}, {self.city}, "
                f"{self.state}, {self.zip_code}, {self.phone}, {self.email}")

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        key = f"{contact.first_name} {contact.last_name}"
        if key not in self.contacts:
            self.contacts[key] = contact
            log.info("Current contacts: %s", list(self.contacts.keys()))
            log.info(f"Contact {key} added successfully.")
        else:
            log.info(f"Contact {key} already exists in the address book.")

    def edit_contact(self, f_name, l_name):
        key = f"{f_name} {l_name}"
        contact = self.contacts.get(key)
        if contact:
            print("Editing Contact Details (leave blank to keep current value):")
            contact.address = input(f"New address [{contact.address}]: ") or contact.address
            contact.city = input(f"New city [{contact.city}]: ") or contact.city
            contact.state = input(f"New state [{contact.state}]: ") or contact.state
            contact.zip_code = input(f"New ZIP code [{contact.zip_code}]: ") or contact.zip_code
            contact.phone = input(f"New phone number [{contact.phone}]: ") or contact.phone
            contact.email = input(f"New email [{contact.email}]: ") or contact.email
            log.info(f"Contact {key} updated successfully.")
        else:
            log.info(f"Contact {key} not found in the address book.")

    def delete_contact(self, f_name, l_name):
        key = f"{f_name} {l_name}"
        if key in self.contacts:
            del self.contacts[key]
            log.info(f"Contact {key} deleted successfully.")
        else:
            log.info(f"Contact {key} not found in the address book.")

    def display_contacts(self):
        if self.contacts:
            for contact in self.contacts.values():
                log.info(contact)
        else:
            log.info("No contacts in the address book.")

class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()

    def add_contact(self):
        contact = Contact()
        self.address_book.add_contact(contact)

    def edit_contact(self):
        f_name = input("Enter the first name of the contact to edit: ")
        l_name = input("Enter the last name of the contact to edit: ")
        self.address_book.edit_contact(f_name, l_name)

    def delete_contact(self):
        f_name = input("Enter the first name of the contact to delete: ")
        l_name = input("Enter the last name of the contact to delete: ")
        self.address_book.delete_contact(f_name, l_name)

    def run(self):
        while True:
            print("\n--- Address Book ---")
            print("1. Add New Contact")
            print("2. Edit Contact")
            print("3. Display Contacts")
            print("4. Delete Contact")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact()
            elif choice == "2":
                self.edit_contact()
            elif choice == "3":
                self.address_book.display_contacts()
            elif choice == "4":
                self.delete_contact()
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    address_main = AddressBookMain()
    address_main.run()