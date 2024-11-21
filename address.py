'''
    @Author: Dhananjay Kumar
    @Date: 12-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 12-11-2024
    @Title : Address Book System with Multiple Address Books, Duplicate Check, and Location Search,sorting by name city, state, and zip code.
'''

import logger
from collections import defaultdict

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
        # Using defaultdict to store persons by city, state, and zip_code
        self.city_dict = defaultdict(list)
        self.state_dict = defaultdict(list)
        self.zip_dict = defaultdict(list)

    def add_contact(self, contact):
        if contact in self.contacts.values():
            log.info(f"Contact {contact.first_name} {contact.last_name} already exists in the address book.")
        else:
            key = f"{contact.first_name} {contact.last_name}"
            self.contacts[key] = contact
            # Add contact to city, state, and zip dictionaries
            self.city_dict[contact.city].append(contact)
            self.state_dict[contact.state].append(contact)
            self.zip_dict[contact.zip_code].append(contact)
            log.info(f"Contact {key} added successfully.")

    def search_by_city(self, city):
        return self.city_dict.get(city, [])

    def search_by_state(self, state):
        return self.state_dict.get(state, [])

    def search_by_zip(self, zip_code):
        return self.zip_dict.get(zip_code, [])

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
            contact = self.contacts.pop(key)
            # Remove contact from city, state, and zip dictionaries
            self.city_dict[contact.city].remove(contact)
            self.state_dict[contact.state].remove(contact)
            self.zip_dict[contact.zip_code].remove(contact)
            log.info(f"Contact {key} deleted successfully.")
        else:
            log.info(f"Contact {key} not found in the address book.")

    def display_contacts(self):
        if self.contacts:
            # Sort contacts alphabetically by first name and last name
            sorted_contacts = sorted(self.contacts.values(), key=lambda contact: (contact.first_name, contact.last_name))
            for contact in sorted_contacts:
                log.info(contact)
        else:
            log.info("No contacts in the address book.")

    def sort_contacts_by_city(self):
        """ Sort contacts by city. """
        sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.city)
        for contact in sorted_contacts:
            log.info(contact)

    def sort_contacts_by_state(self):
        """ Sort contacts by state. """
        sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.state)
        for contact in sorted_contacts:
            log.info(contact)

    def sort_contacts_by_zip(self):
        """ Sort contacts by ZIP code. """
        sorted_contacts = sorted(self.contacts.values(), key=lambda contact: contact.zip_code)
        for contact in sorted_contacts:
            log.info(contact)


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
        city_count = 0
        state_count = 0
        zip_count = 0
        for book_name, address_book in self.address_books.items():
            # Search by city, state, or zip code
            contacts_in_city = address_book.search_by_city(location)
            contacts_in_state = address_book.search_by_state(location)
            contacts_in_zip = address_book.search_by_zip(location)
            results.extend([(book_name, contact) for contact in contacts_in_city + contacts_in_state + contacts_in_zip])

            city_count += len(contacts_in_city)
            state_count += len(contacts_in_state)
            zip_count += len(contacts_in_zip)

        if results:
            log.info(f"Contacts found in {location}:")
            for book_name, contact in results:
                log.info(f"[{book_name}] {contact}")
            
            if city_count > 0:
                log.info(f"\nTotal contacts found in city '{location}': {city_count}")
            if state_count > 0:
                log.info(f"Total contacts found in state '{location}': {state_count}")
            if zip_count > 0:
                log.info(f"Total contacts found in ZIP code '{location}': {zip_count}")
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
            print("4. Search Person by City, State, or Zip")
            print("5. Sort Contacts")
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
                        print("6. Sort Contacts Alphabetically")
                        print("7. Sort Contacts by City")
                        print("8. Sort Contacts by State")
                        print("9. Sort Contacts by ZIP")
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
                        elif sub_choice == "6":
                            address_book.display_contacts()
                        elif sub_choice == "7":
                            address_book.sort_contacts_by_city()
                        elif sub_choice == "8":
                            address_book.sort_contacts_by_state()
                        elif sub_choice == "9":
                            address_book.sort_contacts_by_zip()
                        elif sub_choice == "0":
                            break
                        else:
                            print("Invalid choice.")
            elif choice == "3":
                self.system.display_address_books()
            elif choice == "4":
                location = input("Enter the city, state, or ZIP code to search for: ")
                self.system.search_person_by_location(location)
            elif choice == "5":
                print("\n--- Sorting Contacts ---")
                print("1. Sort by City")
                print("2. Sort by State")
                print("3. Sort by ZIP code")
                sort_choice = input("Enter your choice: ")
                if sort_choice == "1":
                    address_book.sort_contacts_by_city()
                elif sort_choice == "2":
                    address_book.sort_contacts_by_state()
                elif sort_choice == "3":
                    address_book.sort_contacts_by_zip()
                else:
                    print("Invalid choice.")
            elif choice == "0":
                break
            else:
                print("Invalid choice.")


if __name__ == "__main__":
    address_book_system = AddressBookMain()
    address_book_system.run()