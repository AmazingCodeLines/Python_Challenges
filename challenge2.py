"""
Challenge: Random Password Generator 🔐

---------------------------------------------------
Objective
---------------------------------------------------
Create a Python program that generates a random password based on user-defined criteria.

The password must:
    - Contain a specified number of letters.
    - Contain a specified number of digits.
    - Contain a specified number of symbols.
    - Be randomized to avoid predictable patterns.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter three separate numbers:
        - Number of letters.
        - Number of digits.
        - Number of symbols.

2. Randomness:
    - Ensure each category is filled with random characters (letters, digits, symbols).
    - Shuffle the characters to ensure the password is unpredictable.

3. Output:
    - Combine all the characters into a single randomized password.
    - Display the generated password.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. The program must:
    - Validate the user’s input to ensure it is a positive integer.
    - Generate random letters, digits, and symbols based on the input values.

2. Bonus Points:
    - Implement error handling for invalid inputs (e.g., non-integer values or negative numbers).
    - Add an option for the user to exclude ambiguous characters (e.g., `O`, `0`, `l`, `1`, etc.).
    - Allow the user to choose the total password length and automatically distribute letters, digits, and symbols.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using Python's `random` and `string` libraries for randomness.
- Working with user input and input validation.
- Combining and shuffling lists for secure password generation.

---------------------------------------------------"""


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

