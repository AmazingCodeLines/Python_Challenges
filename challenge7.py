"""
Challenge: Caesar Cipher Encryption 🛡️

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program that encrypts text using the Caesar cipher.

The Caesar cipher shifts each letter in the text by a fixed number of positions in the alphabet. Spaces and punctuation are preserved.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to input a text string to encrypt.
    - Prompt the user to input the shift value (an integer).
    - Allow the user to quit the program by typing `quit`.

2. Logic:
    - For each letter in the text:
        - If the letter is uppercase, shift it within the uppercase alphabet.
        - If the letter is lowercase, shift it within the lowercase alphabet.
        - If the character is not a letter (e.g., punctuation or space), keep it unchanged.
    - Handle wrap-around for letters at the end of the alphabet (e.g., shifting `Z` by 1 gives `A`).

3. Output:
    - Display the encrypted text after applying the Caesar cipher.
    - Handle invalid input for the shift value gracefully.

4. Loop:
    - Allow the user to encrypt multiple texts without restarting the program.
    - Exit gracefully when the user types `quit`.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `encrypt(secret_text, shift)` that:
    - Takes a string and a shift value as inputs.
    - Returns the encrypted text as output.

2. Handle user input:
    - Validate the shift value to ensure it is an integer.
    - Provide appropriate error messages for invalid inputs.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Modify the program to handle decryption:
    - Add a function `decrypt(encrypted_text, shift)` to reverse the encryption.
2. Allow the shift value to be negative for leftward shifting.
3. Extend the program to allow the user to choose between encryption and decryption.
4. Optimize for large shift values by reducing the shift to within the range of 0-25.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Implementing string manipulation techniques.
- Using modular arithmetic for wrap-around logic.
- Handling user input with validation and feedback.
- Working with Python's `string` library for character operations.
"""


import string

uppercase_letters = string.ascii_uppercase
lowercase_letters = string.ascii_lowercase

def encrypt(secret_text, shift):
    encrypted_text = ""
    
    for letter in secret_text:
        if letter in uppercase_letters:
            # wrap-around the 26 letter of the alphabet
            encrypted_text += uppercase_letters[(uppercase_letters.index(letter) + shift) % 26]
        elif letter in lowercase_letters:
            encrypted_text += lowercase_letters[(lowercase_letters.index(letter) + shift) % 26]
        else:
            # Preserve spaces and punctuation
            encrypted_text += letter

    return encrypted_text

while True:
    try:
        text_to_encrypt = input("Enter the text you want to encrypt (or 'quit' to exit): ")
        if text_to_encrypt.lower() == 'quit':
            print("Quiting... Goodbye!")
            break
        
        shift = int(input("Enter the desired shift (number): "))
        print("Encrypted text:", encrypt(text_to_encrypt, shift))

    except ValueError:
        print("Invalid shift value. Please enter a number.")
        


       



