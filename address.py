'''
    @Author: Dhananjay Kumar
    @Date: 11-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 11-11-2024
    @Title : Address Book 

'''

'''
    @Author: Dhananjay Kumar
    @Date: 11-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 11-11-2024
    @Title : Address Book 

'''

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
        return (f"{self.first_name} {self.last_name}, {self.address},{self.city}, {self.state}, {self.zip_code}, {self.phone}, {self.email}")

class AddressBook:
    """Stores and manages a collection of contacts."""
    def __init__(self):
        self.contacts = {}

    def add_contact(self, contact):
        """Adds a new contact to the address book if it doesn't already exist."""
        contact_key = f"{contact.first_name} {contact.last_name}"
        
        if contact_key not in self.contacts:
            self.contacts[contact_key] = contact
            log.info("Current contacts: %s", list(self.contacts.keys()))
            log.info("Successfully added contact: %s", contact_key)
        else:
            log.info("Contact already exists: %s", contact_key)

# Create an instance
address_book = AddressBook()
new_contact = Contact()
address_book.add_contact(new_contact)