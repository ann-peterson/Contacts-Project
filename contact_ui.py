"""
This file is a textual UI layer on top of the contacts manager.
It will allow a user to view, add, edit, and delete contacts.
"""

import contact_manager


def display_menu():
    # print "Select one of the following options: "
    print """
    0 - Main Menu,
    1 - Show all contacts,
    2 - Add a new contact,
    3 - Edit a contact,
    4 - Delete a contact,
    5 - Exit the program
    """


def display_contacts():
    current_list = contact_manager.current_contact_list()
    print current_list
    for item in current_list:
        print item.first_name, item.last_name, item.mobile_phone


def main():
    menu_choice = "5" #raw_input("Select one of the following options from the menu:")
    while (True): 
        display_menu()
        if menu_choice == "5":
            break


    

def test():
    contact_manager.add_new_contact("Steve", "Smith")
    contact_manager.add_new_contact("Ed", "Edwardson")
    display_contacts()



if __name__ == '__main__':
    test()

#Contact GitHub API Training Shop Blog About
