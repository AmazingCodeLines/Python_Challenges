"""
Challenge 2: Random Password Generator 🔐

Create a Python program that generates a random password based on user-defined criteria. The program should:

Prompt the user to input the number of letters, digits, and symbols they want in their password.
Generate a set of random letters (both uppercase and lowercase), digits, and symbols according to the specified quantities.
Combine all the characters into a single collection.
Shuffle the characters to ensure randomness.
Display the final, randomly generated password.
"""


import random
import string

password = []

number_of_letters = input("Number of letters: ")
number_of_digits = input("Number of digits: ")
number_of_symbols = input("Number of symbols: ")

letters = "".join(random.choices(string.ascii_letters, k=int(number_of_letters)))
digits = "".join(random.choices(string.digits, k=int(number_of_digits)))
symbols = "".join(random.choices(string.punctuation, k=int(number_of_symbols)))

password.extend(letters)
password.extend(digits)
password.extend(symbols)

random.shuffle(password)

final_password = "".join(password)

print(f"Final password: {final_password}")

