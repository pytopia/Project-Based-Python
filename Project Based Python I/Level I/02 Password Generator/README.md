<img src="./images/password-generator.png" width="700"/>

# Password Manager
## Password Generator
> DIFFICULTY: **EASY**

This is an interesting Python project that uses the **secrets** and **string** modules to generate a strong and secure password, much like you can with popular password managers.

The string module obtains all possible letters, digits, and special characters, while the secrets module allows us to obtain cryptographically secure passwords.

The code for this project is relatively simple as it uses a loop to continually generate passwords until it contains at least one special character and two digits. You can, of course, modify this to fit your own super-strong password rules!

## Check Password Strength

This Python project lets you check whether your password is strong enough.
It does this by checking the number of letters, digits and special characters within a given password and generating a score based on these results.

## TODO

For password generator:
1. Use ascii letters, didits and punctuation for generating password.
2. Use secret module to generate stong password.
3. Check if the password is strong.
4. If the password is not strong enough, create a new password until it meets the necessary rules

For password checker:
1. Get the password from the user
2. Check it with string module for having:
    - lowercase characters
    - uppercase characters
    - special charecters
    - digits  
3. Define a score for password strength
4. Show details and score of input password
5. Ask the user to continue
