from collections import defaultdict


class ContactBook:
    def __init__(self):
        self.contacts = defaultdict(dict)

    def add_contact(self, name: str, phone: str, email: str = None):
        """
        Add a contact to the contact book.

        :param name: Name of the contact to be added.
        :param phone: Phone number of the contact to be added.
        :param email: Email of the contact to be added, defaults to None
        """
        if name in self.contacts:
            print("Contact Already Exits!")
            return

        self.contacts[name]['phone'] = phone
        self.contacts[name]['email'] = email

    def view_contacts(self):
        """
        View all contacts in the contact book.
        """
        for name, info in self.contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['phone']}")
            print(f"Email: {info['email']}")
            print('-' * 50)

    def delete_contact(self, name: str):
        """
        Delete a contact from the contact book.

        :param name: Name of the contact to be deleted.
        """
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

    def update_contact(self, name: str, phone: str = None, email: str = None):
        """
        Update a contact in the contact book.

        :param name: Name of the contact to be updated.
        :param phone: Phone number of the contact to be updated, defaults to None
        :param email: Email of the contact to be updated, defaults to None
        """
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email

            print('Contact updated successfully!')
            return

        print('Contact not found!')


if __name__ == '__main__':
    book = ContactBook()

    while True:
        print('\n\nWelcome to contact book application!')
        print('1. Add Contact')
        print('2. Edit Contact')
        print('3. View Contacts')
        print('4. Delete Contact')
        print('5. Quit')

        user_choice = input('Please choose an option: ')

        if user_choice == '5':
            break

        elif user_choice == '1':
            name = input('\nEnter contact name: ')
            phone = input('Enter contact phone: ')
            email = input('Enter contact email: ')

            book.add_contact(name, phone, email)

        elif user_choice == '2':
            name = input('\nEnter contact name: ')
            phone = input('Enter contact phone: ')
            email = input('Enter contact email: ')

            book.update_contact(name, phone, email)

        elif user_choice == '3':
            print('\n\nList of contacts:')
            book.view_contacts()

        elif user_choice == '4':
            name = input('\nEnter contact name: ')
            book.delete_contact(name)
