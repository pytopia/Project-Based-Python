<img src="./images/otp.png" width="700"/>

# OTP Verification
> DIFFICULTY: **EASY**

This Python project uses the standard **smtplib**, **math**, and **random** modules to send OTP (One Time Password) verification message. You need an **App Password** for your gmail account. If you don't have any app password, follow the steps which will explain later.

OTP Verification is the process of verifying a user by sending a unique password so that the user can be verified before completing a registration or payment process. Most of the time, we get an OTP when we make an online payment, or when we forget our password, or when creating an account on any online platform. Thus, the sole purpose of an OTP is to verify the identity of a user by sending a unique password. The most common form of OTP is generating a random 6-digit number.

## TODO

1. Import the necessary Python modules.
2. Create a 6-digit random number.
3. Store the number in a variable.
4. Write a program to send emails and use OTP as a message.
5. Request two user inputs, first for the user’s email and then for the OTP that the user has received.
6. If the OTP entered by user is correct print **Verified**

## Generating App Password

Since May 2022, Google has tightened its restrictions on ‘less secure apps’ accessing Gmail. You’ll need to follow some extra steps to use this code with your Gmail account. But don’t worry, they’re easy to do, and we’ve listed them for you.

1. Go to the ‘manage account’ page for your google account
2. Click on Security
3. Enable 2FA (use whichever method you prefer)
4. Click on ‘App Passwords’
5. Click on ‘Select App’ and select ‘Mail’
6. Click on ‘Select Device’ & select ‘Other (custom name)’, enter ‘Python Birthday App’
7. Click on ‘Generate’ then save this password