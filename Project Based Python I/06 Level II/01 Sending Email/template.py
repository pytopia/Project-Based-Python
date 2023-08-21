# Import modules

def send_email(recipient, subject, msg):
    # Use EmailMessage and smtplib.SMTP_SSL to send email
    pass

def send_bday_emails(bday_file):
    # Read excel sheet data
    # Create arguments of send_email function and use it.
    # Add current year to Last Sent column in excel
    pass

    
if __name__ == '__main__':
    send_bday_emails(bday_file='data/birthday.xlsx')