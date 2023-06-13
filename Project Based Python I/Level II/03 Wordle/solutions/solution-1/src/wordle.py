import random
import string

import numpy

from src.utils import print_error, print_success, print_warning

random.seed(42)


class Wordle:
    def __init__(self, file_path: str, word_len: int = 5, limit: int = 10_000):
        self.word_len = word_len
        self.words = self.generate_word_frequency(file_path, word_len, limit)

    def generate_word_frequency(self, file_path: str, word_len: int, limit: int):
        """
        Generate top words (top `limit` words) that have word_len letters.

        :param file_path: Words frequency data txt file
        :param word_len: Word length (M)
        :param limit: Top N words
        :return: List of words
        """
        # Build data
        words_freq = []
        with open(file_path) as f:
            for line in f:
                word, frequency = line.split(', ')
                frequency = int(frequency)
                words_freq.append((word, frequency))

        # word_len letters words
        words = list(filter(lambda w_freq: len(w_freq[0]) == word_len, words_freq))

        # Sort Data
        words_freq = sorted(words_freq, key=lambda w_freq: w_freq[1], reverse=True)

        # Limit Data
        words_freq = words_freq[:limit]

        # Drop Frequency Data
        words = [w_freq[0] for w_freq in words_freq]

        return words

    def check_word(self, word, guess_word):
        for w_letter, g_letter in zip(word, guess_word):
            if w_letter == g_letter:
                print_success(f' {g_letter} ', end='')
                print(' ', end='')
            elif g_letter in word:
                print_warning(f' {g_letter} ', end='')
                print(' ', end='')
            else:
                print_error(f' {g_letter} ', end='')
                print(' ', end='')
        print()

    def run(self, ):
        # Random Word
        word = random.choice(self.words)
        word = word.upper()

        # Start Game
        num_try = 6
        success = False
        while num_try:
            guess_word = input(f'Enter a {self.word_len} letter word (or q to exit): ')
            if guess_word.lower() == 'q':
                break
            guess_word = guess_word.upper()

            # Word length
            if len(guess_word) != 5:
                print(f'Word must have {self.word_len} letters. You entered {len(guess_word)}!')
                continue

            # Check valid word
            if guess_word.lower() not in self.words:
                print_warning('Word is not valid!')
                continue

            # Check valid, invalid positions, invalid characters
            self.check_word(word, guess_word)

            if word == guess_word:
                print()
                print_success(' Congratulations! ')
                success = True
                break

            num_try -= 1

        if not success:
            print_warning(f'Game over: The word was "{word}".')
