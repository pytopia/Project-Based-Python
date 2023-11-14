import random
import string
from abc import ABC, abstractmethod
from typing import List, Optional

import nltk

nltk.download('words')


class PasswordGenerator(ABC):
    """
    Base class for generating passwords.
    """
    @abstractmethod
    def generate(self) -> str:
        """
        Subclasses should override this method to generate password.
        """
        pass


class RandomPasswordGenerator(PasswordGenerator):
    """
    Class to generate a random password.
    """
    def __init__(self, length: int = 8, include_numbers: bool = False, include_symbols: bool = False):
        self.length = length
        self.characters: str = string.ascii_letters
        if include_numbers:
            self.characters += string.digits
        if include_symbols:
            self.characters += string.punctuation

    def generate(self) -> str:
        """
        Generate a password from specified characters.
        """
        return ''.join(random.choice(self.characters) for _ in range(self.length))


class MemorablePasswordGenerator(PasswordGenerator):
    """
    Class to generate a memorable password.
    """
    def __init__(
        self,
        no_of_words: int = 5,
        separator: str = "-",
        capitalization: bool = False,
        vocabulary: Optional[List[str]] = None
    ):
        if vocabulary is None:
            vocabulary = nltk.corpus.words.words()  # edit this to any vocabulary list you want

        self.no_of_words: int = no_of_words
        self.separator: str = separator
        self.capitalization: bool = capitalization
        self.vocabulary: List[str] = vocabulary

    def generate(self) -> str:
        """
        Generate a password from a list of vocabulary words.
        """
        password_words = [random.choice(self.vocabulary) for _ in range(self.no_of_words)]
        if self.capitalization:
            password_words = [word.upper() for word in password_words]
        return self.separator.join(password_words)


class PinCodeGenerator(PasswordGenerator):
    """
    Class to generate a numeric pin code.
    """
    def __init__(self, length: int = 4):
        self.length: int = length

    def generate(self) -> str:
        """
        Generate a numeric pin code.
        """
        return ''.join(random.choice(string.digits) for _ in range(self.length))


def test_random_password_generator():
    random_gen = RandomPasswordGenerator(length=10, include_numbers=True, include_symbols=True)
    password = random_gen.generate()
    print(password)
    assert len(password) == 10
    assert any(char in string.ascii_uppercase for char in password)
    assert any(char in string.digits for char in password)


def test_memorable_password_generator():
    memorable_gen = MemorablePasswordGenerator(
        no_of_words=4,
        separator="-",
        capitalization=True,
        vocabulary=nltk.corpus.words.words(),
    )
    password = memorable_gen.generate()
    print(password)
    assert len(password.split('-')) == 4
    assert all(word[0].isupper() for word in password.split('-'))


def test_pincode_generator():
    pin_gen = PinCodeGenerator(length=4)
    pin = pin_gen.generate()
    print(pin)
    assert len(pin) == 4
    assert all(char in string.digits for char in pin)


def main():
    print("Testing RandomPasswordGenerator:")
    test_random_password_generator()
    print("Testing MemorablePasswordGenerator:")
    test_memorable_password_generator()
    print("Testing PinCodeGenerator:")
    test_pincode_generator()


if __name__ == "__main__":
    main()