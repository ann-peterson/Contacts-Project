from contact import *

"""
Contacts Manager
This module manages the contacts list which holds instances of the Contact class.
You can view, add, edit, and delete contacts.
Bonus: write contacts to text file and read contacts in from a text file.
"""
contacts_list = []


def add_new_contact(first_name, last_name):
    # TODO:  handle cases and whitespace for name parameters
    # TODO:  handle if contact_list is empty
    # TODO:  iterate contact_list, check if contact already exists, print error
    # instantiate instance of Contact
    # add to contacts_list
    new_contact = Contact(first_name, last_name)
    contacts_list.append(new_contact)


def edit_existing_contact():
    pass


def delete_contact():
    pass


def current_contact_list():
    # todo: return a sorted list of objects from contacts_list
    return contacts_list


def write_contacts_to_file():
    pass


def read_contacts_from_file():
    pass


def main():
    # test add new contact
    # test edit contact
    # test delete contact
    # test show all contacts
    add_new_contact("Steve", "Smith")
    add_new_contact("Ed", "Edwardson")

    for item in current_contact_list():
        print item.first_name, item.last_name, item.mobile_phone


if __name__ == '__main__':
    main()
