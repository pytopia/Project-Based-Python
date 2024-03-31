# Daily Inspirational Quotes Emailer

This project provides a Python solution for automatically sending daily inspirational quotes to a list of subscribers via email. It aims to spread positivity and motivation with minimal effort, leveraging automation to ensure consistency in sending these daily doses of inspiration.

## Project Objective

The objective of this solution is to demonstrate a practical application of Python for automation, specifically focusing on:
- Fetching a random inspirational quote from a predefined list.
- Reading subscriber details from a CSV file.
- Personalizing and sending emails to each subscriber with their name and the quote of the day.
- Automating the execution of the script to run daily.

## Requirements

Before running this script, ensure you have the following:
- **Python 3.x** installed on your system.
- Access to an **SMTP server** (the example uses Gmail).
- A **CSV file** named `recipients.csv` with the following format:

    ```
    name,email
    John Doe,johndoe@example.com
    Jane Smith,janesmith@example.com
    ```

- **Required Python packages**: While this solution primarily uses Python's standard library (`smtplib`, `email.mime`, `csv`, `random`), ensure all are available in your environment.

## Setup and Configuration

1. **SMTP Configuration**: If you're using Gmail as your SMTP server, you may need to enable "Less secure app access" in your Google Account settings or set up an App Password if 2FA is enabled. This is necessary for the script to log in to your email account to send messages.

2. **Environment Variables**: For security reasons, it's recommended to store your email credentials (email and password) as environment variables. This solution assumes the following environment variables are set:

    - `EMAIL_USER` for your email username.
    - `EMAIL_PASS` for your email password.

    You can set these variables in your operating system or directly in your script for testing (not recommended for production).

3. **Dependencies**: No additional Python packages are required beyond the Python standard library.

## Running the Script

To run the script, simply execute it with Python from your terminal or command prompt:

```bash
python daily_inspirational_quotes.py
```

Ensure you're in the same directory as the `daily_inspirational_quotes.py` script and your `recipients.csv` file.

## Future Enhancements

While this solution meets the basic requirements, consider the following enhancements for a more robust application:

- **External Quote API**: Integrate an external API to fetch new and unique quotes daily, providing variety and freshness to the recipients.
- **Email Template**: Implement HTML email templates for more visually appealing messages.
- **Subscription Management**: Develop a simple web app for managing subscriptions, allowing users to subscribe, unsubscribe, and set preferences.
- **Security Enhancements**: Implement OAuth for SMTP authentication to enhance security and avoid having to lower security settings on your email account.
- **Logging and Monitoring**: Add logging to track the script's execution and errors, and consider a monitoring solution to alert you if the script fails.

## Conclusion

This project serves as a practical example of automating daily tasks with Python, providing a framework that can be expanded with additional features and integrations. It's an excellent starting point for those looking to apply their Python skills in real-world scenarios.
