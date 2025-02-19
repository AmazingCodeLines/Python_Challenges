"""
Challenge 7: Caesar Cipher Encryption 🛡️

Create a Python program that encrypts text using a simple Caesar cipher. The program should:

Define a function that:
Takes a secret text and a shift value as input.
Shifts each letter by the specified amount while maintaining:
Uppercase letters as uppercase.
Lowercase letters as lowercase.
Wraps around the alphabet when the shift moves past 'Z' or 'z'.
Preserves spaces, punctuation, and other non-alphabetic characters unchanged.
Implement a loop that:
Prompts the user for text to encrypt.
Allows the user to exit by typing 'quit'.
Asks the user for the desired numerical shift.
Displays the encrypted text using the defined encryption function.
Handles invalid input for the shift value with appropriate error messages.
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
        


       



