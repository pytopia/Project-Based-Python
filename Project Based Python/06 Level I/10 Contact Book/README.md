# Contact Book Project

## Description
This project is designed for intermediate level students who already have the basic understanding of Python. It focuses on creating a Contact Book application that allows users to store, retrieve, modify, and delete their contacts. The information stored can include the contact's name, phone number, email, and physical address. Optionally, we will be adding a Streamlit dashboard for a visual representation and user-friendly interaction with the app.

## Project Structure
The project will be structured as follows:

```
.
├── README.md
├── requirements.txt
└── src
    ├── __init__.py
    ├── contact_book.py
    ├── dashboard.py
    └── utils
        └── helper_functions.py
```
- `README.md`: This File
- `requirements.txt`: Python requirements file
- `src/contact_book.py`: Main Python script
- `src/dashboard.py`: Streamlit Dashboard script for visual representation
- `src/utils/helper_functions.py`: File where we keep our helper functions.

## Requirements
- Python 3.x
- [Streamlit](https://streamlit.io/) (optional)


You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Hints
- Incorporate Streamlit's functionality to make your application more interactive and user-friendly.
- Keep track of your dependencies (libraries and modules) for easy setup and reproduction of your project.

## Learning Outcomes
This project will help you understand:
- Basics of WebApp creation using Streamlit
- Creating and managing a clean and organized project structure
- Reading, writing and manipulating data with user-friendly interface
- App deployment and software design principles

## Starting the Streamlit Dashboard (Optional)

To start the Streamlit app, go to your terminal, navigate to this project's directory and run:

```bash
streamlit run src/dashboard.py
```
## Conclusion
This project should test your Python abilities and challenge you to build an effective, working application. The optional Streamlit dashboard will take your project to a new level, allowing end-users to interact with your application more easily and efficiently. Happy coding!
