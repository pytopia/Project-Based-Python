<img src="./images/banner.png" width="800">

# Birthday Discount Emailer Project

The Birthday Discount Emailer is a Python programming project where the goal is to create an automated system that reads a list of individuals and their birthdays from a CSV file and subsequently sends personalized birthday emails with discount codes to each person on their birthday.

This project is intended to provide practical experience with several Python concepts, including file I/O, data manipulation, working with dates, and email communication through the SMTP protocol.

## Project Objectives
- Learn how to read and parse CSV files using Python.
- Understand how to work with the `datetime` module to handle dates.
- Use Python's `smtplib` and `email` modules to compose and send emails.
- Explore best practices for managing sensitive information like email credentials.

## Recommended Implementation Steps
1. **CSV File Parsing**: Write a script to read a CSV file containing the names, email addresses, birthdays, and discount codes.

2. **Date Checking**: Implement functionality to check the current date against the birthdays listed in the CSV file to determine whose birthday is today.

3. **Email Composition**: Craft an email template that can be personalized for each recipient, incorporating their name and the discount code.

4. **Sending Emails**: Utilize `smtplib` to connect to an SMTP server and send the email to the birthday person.

## Deliverables
- **README.md**: A guide on how to use the project, with instructions for setting up and running the script.
- `requirements.txt`: A list of the Python libraries required to run the project.
- ‍‍`src/`: A directory containing the source code for the project.
   - `birthday_emailer.py`: The main Python script that orchestrates the reading, checking, and emailing processes.
- `data/`: A directory containing an example CSV file with dummy data.
- `templates/`: A directory for email templates.

## Potential Extensions
- Allow customization of the email message through a template system.
- Implement a system for generating unique discount codes.
- Provide a web interface where non-technical users can upload the CSV file and manage email templates.

## What You Will Learn
By completing this project, you will gain hands-on experience with automating email sending in Python, which is a valuable skill for many software development and data analysis tasks.
