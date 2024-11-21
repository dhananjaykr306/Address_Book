'''
    @Author: Dhananjay Kumar
    @Date: 12-11-2024
    @Last Modified by: Dhananjay Kumar
    @Last Modified time: 12-11-2024
    @Title : Address Book 

'''

import logger
import csv
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
        self.contacts = {}
        self.address_book_collection = defaultdict(dict)
        self.city_person = {}
        self.state_person = {}

    def add_contact(self,address_book_name, contact):
        main_key = address_book_name
        if main_key not in self.address_book_collection:
            key = f"{contact.first_name} {contact.last_name}"
            if key not in self.address_book_collection[main_key]: #UC7 ensuring that there is no duplicate
                self.contacts[key]=contact
                self.address_book_collection[main_key]= self.contacts
                log.info(self.contacts.items())
                log.info(f"Contact {key} added successfully.")

                if contact.city not in self.city_person:
                    self.city_person[contact.city] = []
                self.city_person[contact.city].append(contact)
                
                if contact.state not in self.state_person:
                    self.state_person[contact.state] = []
                self.state_person[contact.state].append(contact)
            else:
                log.info(f"Contact {key} already exists in the address book.")
        else:
            key = f"{contact.first_name} {contact.last_name}"
            if key not in self.address_book_collection[main_key]:
                self.contacts[key]=contact
                self.address_book_collection[main_key]= self.contacts
                log.info(self.contacts.items())
                log.info(f"Contact {key} added successfully.")
                if contact.city not in self.city_person:
                    self.city_person[contact.city] = []
                self.city_person[contact.city].append(contact)
                
                if contact.state not in self.state_person:
                    self.state_person[contact.state] = []
                self.state_person[contact.state].append(contact)
            else:
                log.info(f"Contact {key} already exists in the address book.")
    
    def edit_contact(self, f_name, l_name):
        key = f"{f_name} {l_name}"
        if key not in self.contacts:
            log.info(f"{key} not found in Contacts")
        else:
            self.contacts[key].address = input("Enter new address: ")
            self.contacts[key].city = input("Enter new city: ")
            self.contacts[key].state = input("Enter new state: ")
            self.contacts[key].zip_code = input("Enter new zipcode: ")
            self.contacts[key].phone = input("Enter new phone number: ")
            self.contacts[key].email = input("Enter new email: ")

    #UC8
    def search_by_city_state(self, city, state):
        if self.address_book_collection:
            for contacts in self.address_book_collection.values():
                for contact in contacts.values():
                    if contact.city == city or contact.state==state:
                        log.info(f"{contact}")
        else:
            log.warning("Address book is empty")

    def display_city_persons(self):
        for city, person in self.city_person.items():
            log.info(f"City: {city}: ")
            count=0
            for contact in person:
                count+=1
                log.info(f" First Name:{contact.first_name} last Name:{contact.last_name} Address:{contact.address} Email:{contact.email}")
            log.info(f"{count} person in {city} city.")

    def display_state_persons(self):
        for state, person in self.state_person.items():
            log.info(f"state: {state}: ")
            count = 0
            for contact in person:
                count+=1
                log.info(f" First Name:{contact.first_name} last Name:{contact.last_name} Address:{contact.address} Email:{contact.email}")
            log.info(f"{count} person in {state} state.")

    """"def sort_by_name(self):
        if self.address_book_collection:
            for contacts in self.address_book_collection.values():
                for contact in sorted(contacts.keys()):
                    log.info(f" Name:{contacts[contact].first_name} ")"""

    def sort_by_name(self):
        
        sorted_contacts = sorted(self.contacts.keys(), key=lambda c: c.f_name)
        log.info("Contacts sorted by Name:")
        for contact in sorted_contacts:
            log.info(contacts[contact].values())


    def sort_by_city(self):
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.city)
        log.info("Contacts sorted by city:")
        for contact in sorted_contacts:
            log.info(contact)

    def sort_by_state(self):
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.state)
        log.info("Contacts sorted by state:")
        for contact in sorted_contacts:
            log.info(contact)

    def sort_by_zip(self):
        sorted_contacts = sorted(self.contacts.values(), key=lambda c: c.zip_code)
        log.info("Contacts sorted by zip:")
        for contact in sorted_contacts:
            log.info(contact)

    def sort_contacts(self, by='name'):
        if self.contacts:
            key_map = {
                'name': lambda c: f"{c.first_name} {c.last_name}",
                'city': lambda c: c.city,
                'state': lambda c: c.state,
                'zip': lambda c: c.zip_code
            }
        if by in key_map:
            sorted_contacts = sorted(self.contacts.values(), key=key_map[by])
            log.info(f"Contacts sorted by {by}:")
            for contact in sorted_contacts:
                log.info(contact)
        else:
            log.warning("Invalid sort key.")




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


    def display_contacts(self):
        if self.address_book_collection:
            for books,contacts in self.address_book_collection.items():
                    log.info(f"{books}")
                    for contact in contacts.values():
                        log.info(contact)
        else:
            log.info("No address book is present.")

    
class AddressBookMain:
    def __init__(self):
        self.address_book = AddressBook()
        #self.address_book = {}

    def add_contact_from_console(self):
        print("Enter the following contact details:")

        address_book_name = input(f"Enter the name of the address book: {self.address_book.address_book_collection}")
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        address = input("Address: ")
        city = input("City: ")
        state = input("State: ")
        zip_code = input("Zip Code: ")
        phone = input("Phone Number: ")
        email = input("Email: ")

        contact = Contact(first_name, last_name, address, city, state, zip_code, phone, email)
        self.address_book.add_contact(address_book_name,contact)

    def edit_contact_from_console(self):
        print("Enter the Following Details: ")

        f_name = input("Enter first name: ")
        l_name = input("Enter last name: ")

        self.address_book.edit_contact(f_name,l_name)

    def search_contact_by_city_state_from_console(self):
        print("Enter the details below: ")
        city = input("Enter City: ")
        state = input("Enter state: ")

        self.address_book.search_by_city_state(city,state)

    def sort_contact_from_console(self):
        print("Sort by: ")
        print("1.name")
        print("2.city")
        print("3.state")
        print("4.zip")
        by = input("Enter option number: ")
        if by=='1':
            self.address_book.sort_contacts()
        elif by=='2':
            self.address_book.sort_contacts("city")
        elif by=='3':
            self.address_book.sort_contacts("state")
        elif by=='4':
            self.address_book.sort_contacts("zip")


    def run(self):
        while True:
            print("\n--- Address Book ---")
            print("1. Add New Contact")
            print("2. Edit Contact")
            print("3. Search contact by City or State")
            print("4. Show contact by city")
            print("5. Show contact by state")
            print("6. Sort by name")
            print("7. Sort by City")
            print("8. Sort by state")
            print("9. Sort by Zip")
            print("10. Display Contact")
            print("11.Exit")
            print("12. sort contacts")
            print("13. Save person contact to .txt file")
            print("14. Save person contact to .csv file")
    
    
            choice = input("Enter your choice: ")

            if choice == "1":
                count = int(input("How many contacts you want to add? "))
                while count>0:
                    self.add_contact_from_console()
                    count-=1
            elif choice == "2":
                self.edit_contact_from_console()
            elif choice =="3":
                self.search_contact_by_city_state_from_console()
            elif choice == "4":
                self.address_book.display_city_persons()
            elif choice == "5":
                self.address_book.display_state_persons()
            elif choice =="6":
                self.address_book.sort_by_name()
            elif choice =="7":
                self.address_book.sort_by_city()
            elif choice =="8":
                self.address_book.sort_by_state()
            elif choice =="9":
                self.address_book.sort_by_zip()
            elif choice == "10":
                self.address_book.display_contacts()
            elif choice =="11":
                break
            elif choice == "12":
                self.sort_contact_from_console()
            elif choice == "13":
                self.address_book.save_to_txt()
            elif choice == "14":
                self.address_book.save_to_csv()
            else:
                print("Invalid choice. Please try again.")

if __name__=="__main__":
    address_main = AddressBookMain()
    address_main.run()