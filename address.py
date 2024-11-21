'''
    @Author: Dhananjay Kumar
    @Date: 12-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 12-11-2024
    @Title : Address Book
'''

import logger
import csv
import json
from collections import defaultdict

log = logger.logger_init('AddressBook')

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone = phone
        self.email = email

    def __str__(self):
        return (f"{self.first_name} {self.last_name}, {self.address}, {self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}")


class AddressBook:
    def __init__(self):
        self.address_book_collection = defaultdict(dict)  # Store contacts by address book name
        self.city_person = {}
        self.state_person = {}

    def add_contact(self, address_book_name, contact):
        main_key = address_book_name
        key = f"{contact.first_name} {contact.last_name}"

        # Ensure no duplicates in the address book
        if key not in self.address_book_collection[main_key]:
            self.address_book_collection[main_key][key] = contact
            log.info(f"Contact {key} added successfully in {main_key} address book.")

            # Add to city and state dictionaries for easy retrieval
            if contact.city not in self.city_person:
                self.city_person[contact.city] = []
            self.city_person[contact.city].append(contact)
            
            if contact.state not in self.state_person:
                self.state_person[contact.state] = []
            self.state_person[contact.state].append(contact)
        else:
            log.info(f"Contact {key} already exists in the address book.")

    def edit_contact(self, address_book_name, f_name, l_name):
        main_key = address_book_name
        key = f"{f_name} {l_name}"

        # Check if the contact exists in the specific address book
        if key not in self.address_book_collection[main_key]:
            log.info(f"{key} not found in {main_key} address book.")
        else:
            # Update contact details
            contact = self.address_book_collection[main_key][key]
            contact.address = input("Enter new address: ")
            contact.city = input("Enter new city: ")
            contact.state = input("Enter new state: ")
            contact.zip_code = input("Enter new zip code: ")
            contact.phone = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")

            log.info(f"Contact {key} updated successfully in {main_key} address book.")

    def search_by_city_state(self, city, state):
        if self.address_book_collection:
            for contacts in self.address_book_collection.values():
                for contact in contacts.values():
                    if contact.city == city or contact.state == state:
                        log.info(f"{contact}")
        else:
            log.warning("Address book is empty")

    def display_city_persons(self):
        for city, persons in self.city_person.items():
            log.info(f"City: {city}")
            count = 0
            for contact in persons:
                count += 1
                log.info(f"First Name: {contact.first_name} Last Name: {contact.last_name} Address: {contact.address} Email: {contact.email}")
            log.info(f"{count} person(s) in {city} city.")

    def display_state_persons(self):
        for state, persons in self.state_person.items():
            log.info(f"State: {state}")
            count = 0
            for contact in persons:
                count += 1
                log.info(f"First Name: {contact.first_name} Last Name: {contact.last_name} Address: {contact.address} Email: {contact.email}")
            log.info(f"{count} person(s) in {state} state.")

    def sort_contacts(self, by='name'):
        if self.address_book_collection:
            key_map = {
                'name': lambda c: f"{c.first_name} {c.last_name}",
                'city': lambda c: c.city,
                'state': lambda c: c.state,
                'zip': lambda c: c.zip_code
            }
            if by in key_map:
                for address_book, contacts in self.address_book_collection.items():
                    sorted_contacts = sorted(contacts.values(), key=key_map[by])
                    log.info(f"Contacts in {address_book} sorted by {by}:")
                    for contact in sorted_contacts:
                        log.info(contact)
            else:
                log.warning("Invalid sort key.")
        else:
            log.info("No contacts to sort.")

    def save_to_csv(self, filename='address_book.csv'):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['First Name', 'Last Name', 'Address', 'City', 'State', 'Zip Code', 'Phone', 'Email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for contacts in self.address_book_collection.values():
                for contact in contacts.values():
                    writer.writerow({
                        'First Name': contact.first_name,
                        'Last Name': contact.last_name,
                        'Address': contact.address,
                        'City': contact.city,
                        'State': contact.state,
                        'Zip Code': contact.zip_code,
                        'Phone': contact.phone,
                        'Email': contact.email
                    })
        log.info(f"Address book saved to {filename}")

    def save_to_json(self, filename='address_book.json'):
        json_data = {}
        for book_name, contacts in self.address_book_collection.items():
            json_data[book_name] = [
                {
                    'First Name': contact.first_name,
                    'Last Name': contact.last_name,
                    'Address': contact.address,
                    'City': contact.city,
                    'State': contact.state,
                    'Zip Code': contact.zip_code,
                    'Phone': contact.phone,
                    'Email': contact.email
                }
                for contact in contacts.values()
            ]
        with open(filename, 'w') as jsonfile:
            json.dump(json_data, jsonfile, indent=4)
        log.info(f"Address book saved to {filename}")

    def display_contacts(self):
        if self.address_book_collection:
            for book_name, contacts in self.address_book_collection.items():
                log.info(f"Address Book: {book_name}")
                for contact in contacts.values():
                    log.info(contact)
        else:
            log.info("No address book is present.")


class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()

    def add_contact_from_console(self):
        print("Enter the following contact details:")
        address_book_name = input("Enter the name of the address book: ")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.address_book.add_contact(address_book_name, contact)

    def edit_contact_from_console(self):
        print("Enter the following details:")
        address_book_name = input("Enter the address book name: ")
        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")
        self.address_book.edit_contact(address_book_name, f_name, l_name)

    def search_contact_by_city_state_from_console(self):
        city = input("Enter City: ")
        state = input("Enter State: ")
        self.address_book.search_by_city_state(city, state)

    def sort_contact_from_console(self):
        options = {"1": "name", "2": "city", "3": "state", "4": "zip"}
        print("Sort by:\n1. Name\n2. City\n3. State\n4. Zip")
        choice = input("Enter option number: ")
        sort_key = options.get(choice, "name")
        self.address_book.sort_contacts(sort_key)

    def run(self):
        while True:
            print("\n--- Address Book ---")
            print("1. Add New Contact")
            print("2. Edit Contact")
            print("3. Search Contact by City or State")
            print("4. Show Contacts by City")
            print("5. Show Contacts by State")
            print("6. Sort Contacts by Name/Ciy/State/Zip")
            print("10. Display Contacts")
            print("11. Save Contacts to CSV")
            print("12. Save Contacts to JSON")
            print("13. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.add_contact_from_console()
            elif choice == "2":
                self.edit_contact_from_console()
            elif choice == "3":
                self.search_contact_by_city_state_from_console()
            elif choice == "4":
                self.address_book.display_city_persons()
            elif choice == "5":
                self.address_book.display_state_persons()
            elif choice == "6":
                self.sort_contact_from_console()
            elif choice == "10":
                self.address_book.display_contacts()
            elif choice == "11":
                self.address_book.save_to_csv()
            elif choice == "12":
                self.address_book.save_to_json()
            elif choice == "13":
                break
            else:
                print("Invalid choice. Please try again.")

# Main
if __name__ == "__main__":
    app = AddressBookMain()
    app.run()