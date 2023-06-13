# Source Code Link:
# https://hackr.io/blog/python-projects

import pandas as pd
from datetime import datetime
import smtplib
from email.message import EmailMessage


def send_email(recipient, subject, msg):
    GMAIL_ID = 'your_email_here'
    GMAIL_PWD = 'your_app_password_here'

    email = EmailMessage()
    email['Subject'] = subject
    email['From'] = GMAIL_ID
    email['To'] = recipient
    email.set_content(msg)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as gmail_obj:
        gmail_obj.ehlo()
        gmail_obj.login(GMAIL_ID, GMAIL_PWD)
        gmail_obj.send_message(email)

    print('Email sent to ' + str(recipient) + ' with Subject: \''
            + str(subject) + '\' and Message: \'' + str(msg) + '\'')


def send_bday_emails(bday_file):

    bdays_df = pd.read_excel(bday_file)
    today = datetime.now().strftime('%m-%d')
    year_now = datetime.now().strftime('%Y')
    sent_index = []

    for idx, item in bdays_df.iterrows():
        bday = item['Birthday'].to_pydatetime().strftime('%m-%d')
        if (today == bday) and year_now not in str(item['Last Sent']):
            msg = 'Happy Birthday ' + str(item['Name'] + '!!')
            send_email(item['Email'], 'Happy Birthday', msg)
            sent_index.append(idx)

    
    # add current year to Last Sent column in excel
    for idx in sent_index:
        bdays_df.loc[idx, 'Last Sent'] = str(year_now)

    bdays_df.to_excel(bday_file, index=False)


if __name__ == '__main__':
    send_bday_emails(bday_file='data/birthday.xlsx')