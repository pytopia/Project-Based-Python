import random
import string
from typing import List, Optional


def generate_random_password(length: int = 8, include_numbers: bool = False, include_symbols: bool = False) -> str:
    """
    Generate a random password.
    """
    characters: str = string.ascii_letters
    if include_numbers:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation

    return ''.join(random.choice(characters) for _ in range(length))


def generate_memorable_password(
    no_of_words: int = 5,
    separator: str = "-",
    capitalization: bool = False,
    vocabulary: Optional[List[str]] = None
) -> str:
    """
    Generate a memorable password from a list of vocabulary words.
    """
    if vocabulary is None:
        vocabulary = ['apple', 'banana', 'cherry', 'dates']  # edit this to any vocabulary list you want

    password_words = random.sample(vocabulary, no_of_words)

    if capitalization:
        password_words = [word.capitalize() for word in password_words]

    return separator.join(password_words)


def generate_pin(length: int = 4) -> str:
    """
    Generate a numeric pin code.
    """
    return ''.join(random.choice(string.digits) for _ in range(length))


def test_random_password_generator():
    password = generate_random_password(10, True, True)
    print(password)
    assert len(password) == 10
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)


def test_memorable_password_generator():
    password = generate_memorable_password(4, '-', True)
    print(password)
    assert len(password.split('-')) == 4
    assert all(word[0].isupper() for word in password.split('-'))


def test_pin_generator():
    pin = generate_pin(4)
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def main():
    print("Testing Random Password Generator:")
    test_random_password_generator()
    print("Testing Memorable Password Generator:")
    test_memorable_password_generator()
    print("Testing Pincode Generator:")
    test_pin_generator()


if __name__ == "__main__":
    main()
