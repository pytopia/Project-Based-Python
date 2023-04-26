import string
import os

def check_password_strength():
    password = input('Enter the password: ')
    strength = 0
    lower_count = upper_count = num_count = special_count = 0

    for char in password:
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    remarks = ''

    if strength == 1:
        remarks = 'VERY WEAK'
    elif strength == 2:
        remarks = 'WEAK'
    elif strength == 3:
        remarks = 'MEDIUM'
    elif strength == 4:
        remarks = 'STRONG'

    print('Your password has:-')
    print(f'{lower_count} lowercase letters')
    print(f'{upper_count} uppercase letters')
    print(f'{num_count} digits')
    print(f'{special_count} special characters')
    print(f'Password Score: {strength / 4}')
    print(f'Remarks: {remarks}')


if __name__ == '__main__':
    print('===== Welcome to Password Strength Checker =====')
    while True:
        check_password_strength()
        ans = input('\nCheck another password? y/n ?')
        if ans[0].lower() == 'n':
            print('Bye!')
            break
        else:
            os.system('clear')
            continue
           