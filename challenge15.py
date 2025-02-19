"""
Challenge 15 : Modular Exponentiation with pow() ⚡

Create a Python program that calculates the result of raising a base number to an exponent and then finding the remainder when divided by a modulus. The program should:

Define a function that:
Takes three integers: a base number, an exponent, and a modulus.
Returns the remainder after the base number is raised to the exponent and divided by the modulus.
Raises an error if the modulus is zero.
Prompt the user to enter values for the base, exponent, and modulus.
Display the final result of the calculation.
Handle invalid inputs by showing an appropriate error message.
"""



def modulo_power(x, y, z):
    """
    Parameters:
    x (int): The base integer.
    y (int): The exponent.
    z (int): The modulus.

    Returns:
    int: The result of (x^y) mod z.
    """
    if z == 0:
        raise ValueError("Modulus z cannot be zero.")
    return pow(x, y, z)

# Example Usage
try:
    x = int(input("Enter the base (x): "))
    y = int(input("Enter the exponent (y): "))
    z = int(input("Enter the modulus (z): "))
    print(f"The result of ({x}^{y}) % {z} is: {modulo_power(x, y, z)}")
except ValueError as e:
    print(f"Error: {e}")
