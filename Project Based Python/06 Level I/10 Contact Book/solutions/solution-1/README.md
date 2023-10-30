# Contact Book

The Python Contact Book Project provides an interactive console text-based application where users can store, retrieve, edit, and delete their contacts. User can store their contact's name, phone number, email, and address.

## Project Implementation
The primary data structure was a built-in Python dictionary, which was tasked with managing contact entries. This structure was chosen due to its efficiency in handling these particular operations (O(1) average complexity for add, delete, get operations).

# Project Structure
The project consists of the following files and directories.

```
.
├── README.md
├── contact_book.py
└── main.py
```

The project structure was designed to be simple and clean.

- `README.md`: this document providing project description and documentation
- `contact_book.py`: the Python script that defines the ContactBook class which encapsulates the core functionalities of the application
- `main.py`: the main script which interacts with the user and uses ContactBook class methods to provide the desired functionality

### ContactBook Class

The core logic of the application is implemented in `ContactBook` class:

- The `add_contact` method allows for new entries to be made to the 'book'. Each entry must be unique by name.
- The `edit_contact` method permits updates to contact information.

- The `view_contacts` method lists all contacts in the address book along with their information.
- The `delete_contact` method allows for existing contacts to be removed from the book.


The `main.py` file serves as an interface between the user and the `ContactBook` class instance. It gets user inputs, calls the necessary methods and handles the application flow.

## User Interface
The interface is a simple console-based menu that offers users options to add, view, edit, delete contacts or quit the program.

## Installation and Usage
To run the program, navigate to the project directory and run the following command:

```bash
python main.py
```
