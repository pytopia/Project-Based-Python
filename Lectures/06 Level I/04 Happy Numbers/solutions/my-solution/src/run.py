def is_happy(n: int):
    """
    A happy numbers is a number defined by the following process:
    Starting with any positive integer, replace the number by the sum of the
    squares of its digits, and repeat the process until the number equals
    1 (where it will stay), or it loops endlessly in a cycle which does not include 1.

    :param n: Input number
    :return: True if n is a happy number, False otherwise

    Examples:

    >>> is_happy(19)
    True

    >>> is_happy(2)
    False

    >>> is_happy(44)
    True
    """
    seen_numbers = set()
    while (n != 1) and (n not in seen_numbers):
        seen_numbers.add(n)
        n = sum([int(i) ** 2 for i in str(n)])

    return n == 1


if __name__ == '__main__':
    assert is_happy(4) is True
    assert is_happy(7) is True
    assert is_happy(45) is False
    assert is_happy(44) is True
