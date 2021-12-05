# This program is a command line based address book created by Brenton O'Brien
# The purpose of this program is to practice my object orientated programming and interacting with files

# Imports
import csv
import os

# Check for directory that saves contacts in address book, if it doesnt exist then create empty folder
# Public folder is selected so there is no permission errors
path = 'C:/Users/Public/cmd-address-book-contacts'
if os.path.exists(path):
    pass
else:
    os.mkdir(path)


# Each new contact will be saved as a 'Person' Object
class Person:
    def __init__(self, first, last, phone, email_address):
        self.first = first
        self.last = last
        self.phone = phone
        self.email_address = email_address

    # Prints First name and Last name
    def full_name(self):
        return f"{self.first} {self.last}"

    # Allows you to print out all the Person's details when converted to a string
    def __str__(self):
        return f"{self.first} {self.last} : {self.phone} : {self.email_address}"


# Clears the terminal screen
def cls():
    os.system('cls')


# Displays the menu screen and awaits user input
def main_menu():
    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n-------------- MAIN MENU --------------')
    print('1) View contacts')
    print('2) Add contact')
    print('3) Remove contact')
    print('4) EXIT')
    print('---------------------------------------')
    user_input = input('Make a selection: ')

    if user_input == '1':
        cls()
        view_contacts()

    elif user_input == '2':
        cls()
        add_contact()

    elif user_input == '3':
        cls()
        remove_contact()

    elif user_input == '4':
        cls()
        exit()

    else:
        cls()
        main_menu()


# Opens the CSV file if it exists, for each row it will create a new Person Object, and print its string representation
# Once contacts are displayed, it will await user input
def view_contacts():
    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ VIEW CONTACTS ------------\n')
    try:
        with open('C:/Users/Public/cmd-address-book-contacts/contacts.csv', "r+", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                next_contact = Person(row[0], row[1], row[2], row[3])
                print(str(next_contact))

    except FileNotFoundError:
        print('No contacts found.')

    print('\n---------------------------------------')
    print('1) Return to menu')
    print('2) EXIT')
    print('---------------------------------------')
    user_input = input('Make a selection: ')

    if user_input == '1':
        cls()
        main_menu()

    elif user_input == '2':
        cls()
        exit()

    else:
        cls()
        view_contacts()


def add_contact():
    # Asks for each Person Class attributes. Clears the screen upon each new prompt
    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ ADD CONTACTS -------------')
    first_name = input('First name: ')
    cls()

    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ ADD CONTACTS -------------')
    last_name = input('Last name: ')
    cls()

    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ ADD CONTACTS -------------')
    phone_number = input('Phone number: ')
    cls()

    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ ADD CONTACTS -------------')
    email_address = input('Email address: ')
    cls()

    # Creates a new person object called 'new contact' based on user input
    new_contact = Person(first_name, last_name, phone_number, email_address)

    # Saves the person to a csv file. the writer takes each object attribute and saves it into separate columns
    # This is so the person can be reconstructed into an object if required
    with open('C:/Users/Public/cmd-address-book-contacts/contacts.csv', "a+", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([new_contact.first, new_contact.last, new_contact.phone, new_contact.email_address])

    # Gives the user feedback to say the operation was successful and returns to the main menu
    print('---------------------------------------')
    print(f"{new_contact.full_name()} has been added to your contacts")
    print('---------------------------------------')
    main_menu()


def remove_contact():
    # Asks for first name and last name. Clears the screen upon each new prompt
    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ REMOVE CONTACTS ----------')
    first = input('Enter the first name: ')
    cls()

    print('\n----- WELCOME TO THE ADDRESS BOOK -----')
    print('\n------------ REMOVE CONTACTS ----------')
    last = input('Enter the last name: ')
    cls()

    # Opens contact csv file and searches for the person row by row.
    # If the name is on a row, tell the user the person has been removed, and don't add them to the temp csv file
    # If the person not found on a row, save them to a temporary csv file
    try:
        with open('C:/Users/Public/cmd-address-book-contacts/contacts.csv', "r+", newline="") as f:
            reader = csv.reader(f)
            for row in reader:
                if first == row[0] and last == row[1]:
                    print('---------------------------------------')
                    print(f'{row[0]} {row[1]} has been removed from your contacts')
                    print('---------------------------------------')
                else:
                    with open('C:/Users/Public/cmd-address-book-contacts/contacts_temp.csv', 'a', newline='') as t:
                        writer = csv.writer(t)
                        writer.writerow([row[0], row[1], row[2], row[3]])

        # The original csv is deleted, and the temp file takes place of the original. This is to 'delete' any names that matched the search
        os.remove('C:/Users/Public/cmd-address-book-contacts/contacts.csv')
        os.rename('C:/Users/Public/cmd-address-book-contacts/contacts_temp.csv', 'C:/Users/Public/cmd-address-book-contacts/contacts.csv')

    except FileNotFoundError:
        print('No contacts found.')

    # Return to menu once deleting contact is complete
    main_menu()

# Open main menu as soon as the program is run
main_menu()
