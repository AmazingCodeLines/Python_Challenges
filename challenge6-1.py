
"""
Challenge: Optimized Prime Number Checker 🔢

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to check if a number is a prime number, using an optimized algorithm for efficiency.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter a number to test for primality.

2. Logic:
    - A prime number is a natural number greater than 1, divisible only by 1 and itself.
    - Use an optimized algorithm to check primality:
        - Eliminate non-prime numbers ≤ 3 with special cases.
        - Skip even numbers and multiples of 3.
        - Test divisors up to the square root of the number, incrementing by 6 to check only potential factors.

3. Output:
    - Display whether the number is prime or not.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `is_prime(number)` that:
    - Accepts an integer as input.
    - Returns `True` if the number is prime, and `False` otherwise.
    - Implements the optimized algorithm for primality testing.

2. Handle edge cases:
    - Numbers ≤ 1 should return `False`.
    - Numbers 2 and 3 should return `True`.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to find all prime numbers in a given range.
2. Add functionality to count the total number of prime numbers in a range.
3. Measure and compare the performance of the optimized algorithm against a naive approach.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Implementing optimized algorithms for mathematical problems.
- Reducing computational complexity by skipping unnecessary checks.
- Using loops and conditional logic effectively.
"""


def is_prime(number):
    if number <= 1:
        return False  # 0 and 1 are not prime numbers
    if number <= 3:
        return True   # 2 and 3 are prime numbers
    if number % 2 == 0 or number % 3 == 0:
        return False  # Eliminate multiples of 2 and 3

    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False  # Divisible by a number other than 1 and itself
        i += 6  # Check next potential factors
    return True


