# Source Code Link:
# https://hackr.io/blog/python-projects

def get_digits(number):
    digits = []
    while number:
        digits.append(number % 10)
        number //= 10
    digits.reverse()
    return digits

#---------------------------------------
def is_happy_number(number):
    previous_numbers = []
    while True:
        digits = get_digits(number)
        sum_of_squared_digits = sum(list(map(lambda x: x **2, digits)))
        if sum_of_squared_digits == 1:
            return True
        elif sum_of_squared_digits in previous_numbers:
            return False
        else:
            number = sum_of_squared_digits
            previous_numbers.append(number)
            
#----------------------------------------------
def print_happy_number(number):
    happy_numbers = []
    count = 0
    while count < 8:
        if is_happy_number(number):
            happy_numbers.append(number)
            count += 1
        number += 1
    return happy_numbers

#---------------------------------------------
if __name__ == '__main__':
    number = int(input('Enter the number: '))

    print(print_happy_number(number))