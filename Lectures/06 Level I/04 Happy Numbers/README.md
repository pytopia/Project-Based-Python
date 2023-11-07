<img src="./images/banner.png" width="800">

# Happy Numbers

In this python project, you'll be diving into the world of "happy" numbers. A number is considered "happy" if by following a specific sequence, it results in 1. The sequence is as follows: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. These numbers for which this process ends in 1 are happy numbers.

For example, 19 is a happy number. Here's why:

- 1² + 9² = 82
- 8² + 2² = 68
- 6² + 8² = 100
- 1² + 0² + 0² = 1

As you can see, we eventually reached 1, which makes 19 a "happy" number. This project tasks you with creating a program that can accurately determine whether any given positive integer is a happy number or not.

## Project Structure

```
README.md
requirements.txt
src/
    happy_number.py
```

## Requirements

- Python 3.7+
- A basic understanding of Python and its core concepts

## Learning Outcomes

This project will help you practice:

1. Using Python's core functionality, such as lists, loops, and sets, to solve a complex problem.
2. Incorporating mathematical concepts in a programming environment.
3. Writing and running unit tests to ensure that your code is working as intended.
4. Improve your problem-solving abilities and debugging skills.
