<img src="./images/sending-email.png" width="700"/>

# Sending Emails
> DIFFICULTY: **INTERMEDIATE**

This Python project uses the standard **smtplib**, **EmailMessage**, and **datetime** modules to send automated birthday emails.
In addition you need pandas and openpyxl (these need to be pip installed).

This program reads data from an excel sheet that contains all of your friends’ details. Then it sends them an email if today is their birthday, before making a note in your spreadsheet to say they’ve received their email.

## TODO

1. Use pandas to read excel sheet file and save the data in a pandas dataframe.
2. Use the smtplib and EmailMessage modules to create an SSL connection to your email account and send message.
3. When sending an email, make sure that no email has been sent to that person before.
3. Use a pandas dataframe to add current year to Last Sent column in the excel sheet.

## Generating App Password

Since May 2022, Google has tightened its restrictions on ‘less secure apps’ accessing Gmail. You’ll need to follow some extra steps to use this code with your Gmail account. But don’t worry, they’re easy to do, and we’ve listed them for you.

1. Go to the ‘manage account’ page for your google account
2. Click on Security
3. Enable 2FA (use whichever method you prefer)
4. Click on ‘App Passwords’
5. Click on ‘Select App’ and select ‘Mail’
6. Click on ‘Select Device’ & select ‘Other (custom name)’, enter ‘Python Birthday App’
7. Click on ‘Generate’ then save this password

## Before You Run

1. Replace your gmail and app password in following lines in the code:
```python
GMAIL_ID = 'your_email_here'
GMAIL_PWD = 'your_app_password_here'
```
2. Complete the excel sheet columns in data/birthday.xlsx with your friends information as following: 
- Name: your friend name
- Email: your friend email
- Birthday: should fill with (MM/DD/YYYY) format
- Last Sent: leave it empty, will fill by your code automatically





