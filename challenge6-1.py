
"""
Challenge 6-1: Optimized Prime Number Checker 🔢

Write a Python function that determines whether a given number is a prime number. The function should:

Return False if the number is less than or equal to 1, as these are not prime numbers.
Return True for the prime numbers 2 and 3.
Efficiently eliminate multiples of 2 and 3 early in the process.
Use a loop to check for divisibility by potential factors, optimizing by:
Checking only numbers up to the square root of the given number.
Skipping unnecessary checks by incrementing in steps of 6 (since prime numbers greater than 3 are of the form 6k ± 1).
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


