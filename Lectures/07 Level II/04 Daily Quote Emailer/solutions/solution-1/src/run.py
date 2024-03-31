import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import csv

# Your email credentials
sender_email = "hejazizo.ali@gmail.com"
sender_password = "fwsi ewkn dsqy rdft"

# Path to your CSV file
csv_file_path = "recipients.csv"

# List of inspirational quotes
quotes = [
    "The best way to predict the future is to invent it. – Alan Kay",
    "A dream doesn't become reality through magic; it takes sweat, determination, and hard work. – Colin Powell",
    "Success is not the key to happiness. Happiness is the key to success. If you love what you are doing, you will be successful. – Albert Schweitzer",
    # Add more quotes as needed
]


# Function to send emails
def send_email(recipient_name, recipient_email, quote):
    subject = "Your Daily Inspirational Quote"
    body = f"Hello {recipient_name}, here is your daily inspirational quote:\n\n{quote}"

    # Setting up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Sending the email
    try:
        session = smtplib.SMTP('smtp.gmail.com', 587)  # use gmail with port
        session.starttls()  # enable security
        session.login(sender_email, sender_password)  # login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_email, recipient_email, text)
        session.quit()
        print(f"Mail Sent Successfully to {recipient_name} ({recipient_email})")
    except Exception as e:
        print(f"Failed to send email to {recipient_name} ({recipient_email}). Error: {e}")


# Read CSV and send emails
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        recipient_name = row['name']
        recipient_email = row['email']
        # Select a random quote
        quote_of_the_day = random.choice(quotes)
        send_email(recipient_name, recipient_email, quote_of_the_day)
