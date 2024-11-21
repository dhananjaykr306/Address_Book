'''
    @Author: Dhananjay Kumar
    @Date: 12-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 12-11-2024
    @Title : Address Book System with Multiple Address Books, Duplicate Check, and Location Search
'''

import logger

log = logger.logger_init('AddressBookSystem')

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

    def __eq__(self, other):
        if isinstance(other, Contact):
            return self.first_name == other.first_name and self.last_name == other.last_name
        return False

    def __hash__(self):
        return hash((self.first_name, self.last_name))


class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        if contact in self.contacts.values():
            log.info(f"Contact {contact.first_name} {contact.last_name} already exists in the address book.")
        else:
            key = f"{contact.first_name} {contact.last_name}"
            self.contacts[key] = contact
            log.info(f"Contact {key} added successfully.")

    def search_by_city_or_state(self, location):
        # Return a list of contacts matching the city or state
        return [contact for contact in self.contacts.values() if contact.city == location or contact.state == location]

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


class AddressBookSystem:
    def __init__(self):
        self.address_books = {}

    def create_address_book(self):
        name = input("Enter a unique name for the new address book: ")
        if name not in self.address_books:
            self.address_books[name] = AddressBook()
            log.info(f"Address book '{name}' created successfully.")
        else:
            log.info(f"An address book with the name '{name}' already exists.")

    def select_address_book(self):
        name = input("Enter the name of the address book to select: ")
        return self.address_books.get(name)

    def display_address_books(self):
        if self.address_books:
            log.info("Available Address Books:")
            for name in self.address_books.keys():
                log.info(f" - {name}")
        else:
            log.info("No address books available.")

    def search_person_by_location(self, location):
        results = []
        for book_name, address_book in self.address_books.items():
            contacts = address_book.search_by_city_or_state(location)
            for contact in contacts:
                results.append((book_name, contact))
        if results:
            log.info(f"Contacts found in {location}:")
            for book_name, contact in results:
                log.info(f"[{book_name}] {contact}")
        else:
            log.info(f"No contacts found in '{location}'.")


class AddressBookMain:
    def __init__(self):
        self.system = AddressBookSystem()

    def add_contact_to_selected_book(self, address_book):
        contact = Contact()
        address_book.add_contact(contact)

    def add_multiple_contacts_to_selected_book(self, address_book):
        try:
            num_contacts = int(input("Enter the number of contacts you want to add: "))
            for _ in range(num_contacts):
                print("\nAdding new contact:")
                self.add_contact_to_selected_book(address_book)
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    def edit_contact_in_selected_book(self, address_book):
        f_name = input("Enter the first name of the contact to edit: ")
        l_name = input("Enter the last name of the contact to edit: ")
        address_book.edit_contact(f_name, l_name)

    def delete_contact_in_selected_book(self, address_book):
        f_name = input("Enter the first name of the contact to delete: ")
        l_name = input("Enter the last name of the contact to delete: ")
        address_book.delete_contact(f_name, l_name)

    def run(self):
        while True:
            print("\n--- Address Book System ---")
            print("1. Create New Address Book")
            print("2. Select Address Book")
            print("3. Display All Address Books")
            print("4. Search Person by City or State")
            print("0. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.system.create_address_book()
            elif choice == "2":
                self.system.display_address_books()
                address_book = self.system.select_address_book()
                if address_book:
                    while True:
                        print("\n--- Address Book Operations ---")
                        print("1. Add New Contact")
                        print("2. Add Multiple Contacts")
                        print("3. Edit Contact")
                        print("4. Display Contacts")
                        print("5. Delete Contact")
                        print("0. Back to Main Menu")
                        sub_choice = input("Enter your choice: ")

                        if sub_choice == "1":
                            self.add_contact_to_selected_book(address_book)
                        elif sub_choice == "2":
                            self.add_multiple_contacts_to_selected_book(address_book)
                        elif sub_choice == "3":
                            self.edit_contact_in_selected_book(address_book)
                        elif sub_choice == "4":
                            address_book.display_contacts()
                        elif sub_choice == "5":
                            self.delete_contact_in_selected_book(address_book)
                        elif sub_choice == "0":
                            break
                        else:
                            print("Invalid choice. Please try again.")
                else:
                    print("Selected address book not found.")
            elif choice == "3":
                self.system.display_address_books()
            elif choice == "4":
                location = input("Enter the city or state to search for contacts: ")
                self.system.search_person_by_location(location)
            elif choice == "0":
                break
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    address_main = AddressBookMain()
    address_main.run()