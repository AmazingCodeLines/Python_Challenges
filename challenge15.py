"""
Challenge: Modular Exponentiation with pow() ⚡

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python function to compute `(x^y) mod z` efficiently using Python's built-in `pow()` function.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Accept three integers: `x` (base), `y` (exponent), and `z` (modulus).

2. Logic:
    - Use Python's built-in `pow()` function to calculate `(x^y) % z`.
    - Ensure the modulus `z` is non-zero. If `z` is zero, raise a `ValueError` with an appropriate error message.

3. Output:
    - Return the computed result of `(x^y) % z`.

---------------------------------------------------
Examples
---------------------------------------------------
1. Input: `x=5, y=3, z=7`
   Output: `6` (since `(5^3) % 7 = 125 % 7 = 6`)

2. Input: `x=2, y=10, z=3`
   Output: `1` (since `(2^10) % 3 = 1024 % 3 = 1`)

3. Input: `x=10, y=5, z=0`
   Output: Raises `ValueError: Modulus z cannot be zero.`

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `modulo_power(x, y, z)` that:
    - Accepts integers `x`, `y`, and `z`.
    - Computes `(x^y) % z` using `pow(x, y, z)`.

2. Handle Edge Cases:
    - If `z` is zero, raise a `ValueError`.

3. Test the function with various inputs to ensure correctness.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to allow the user to input values interactively.
2. Provide meaningful error messages for invalid inputs (e.g., non-integer values).
3. Explain the mathematical significance of modular exponentiation in cryptography and number theory.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using Python's `pow()` function for efficient modular arithmetic.
- Handling input validation and exceptions.
- Applying modular arithmetic in practical scenarios.
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
