ones = (
   'Zero', 'One', 'Two', 'Three', 'Four',
   'Five', 'Six', 'Seven', 'Eight', 'Nine'
   )

twos = (
   'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen',
    'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen'
   )

tens = (
   'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty',
    'Seventy', 'Eighty', 'Ninety', 'Hundred'
   )

suffixes = (
   '', 'Thousand', 'Million', 'Billion'
   )

def fetch_words(number, index):
    if number == '0': return 'Zero'

    number = number.zfill(3)
    hundreds_digit = int(number[0])
    tens_digit = int(number[1])
    ones_digit = int(number[2])

    words = '' if number[0] == '0' else ones[hundreds_digit]

    if words != '':
        words += ' Hundred '

    if tens_digit > 1:
        words += tens[tens_digit - 2]
        words += ' '
        words += ones[ones_digit]
    elif(tens_digit == 1):
        words += twos[((tens_digit + ones_digit) % 10) - 1]
    elif(tens_digit == 0):
        words += ones[ones_digit]

    if(words.endswith('Zero')):
        words = words[:-len('Zero')]
    else:
        words += ' '

    if len(words) != 0:
        words += suffixes[index]

    return words


def convert_to_words(number):
    length = len(str(number))
    if length > 12:
        return 'This program supports a maximum of 12 digit numbers.'

    count = length // 3 if length % 3 == 0 else length // 3 + 1
    copy = count
    words = []

    for i in range(length - 1, -1, -3):
        words.append(fetch_words(
           str(number)[0 if i - 2 < 0 else i - 2 : i + 1], copy - count))

        count -= 1

    final_words = ''
    for s in reversed(words):
        final_words += (s + ' ')

    return final_words

if __name__ == '__main__':
    number = int(input('Enter any number: '))
    print(f'{number} in words is: {convert_to_words(number)}')