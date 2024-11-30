"""
Challenge: Prime Number Checker 🔢

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to determine if a given integer is a prime number.

A prime number is a natural number greater than 1 that is divisible only by 1 and itself.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to input an integer.
    - Allow the user to quit the program by entering `0`.

2. Logic:
    - A number is prime if:
        - It is greater than 1.
        - It is not divisible by any number other than 1 and itself.
    - Use efficient methods to check for prime status:
        - Immediately return `False` for numbers ≤ 1.
        - Skip even numbers greater than 2.
        - Check divisors only up to the square root of the number.

3. Output:
    - For valid inputs, display whether the number is prime or not.
    - For invalid inputs (non-integer), display an appropriate error message.

4. Loop:
    - Allow the user to check multiple numbers without restarting the program.
    - Exit gracefully when the user enters `0`.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `is_prime(number)` that:
    - Takes an integer as input.
    - Returns `True` if the number is prime, otherwise returns `False`.

2. Handle user input and provide feedback:
    - Validate that the input is a valid integer.
    - Display an error message for invalid inputs and prompt the user again.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Optimize the `is_prime` function to skip even numbers and only check divisors up to the square root.
2. Extend the program to display all prime numbers less than a given input (e.g., find all primes < 50).
3. Add performance measurements to compare the efficiency of your solution with a simpler brute-force approach.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Writing efficient algorithms for mathematical problems.
- Handling user input with validation and feedback.
- Using loops for continuous interaction.
- Applying modular arithmetic and mathematical reasoning in programming.
"""


def is_prime(number):

    if number <= 1:
        return False  
    if number == 2:
        return True  
    if number % 2 == 0:
        return False  
    
    # Check odd divisors from 3 to sqrt(number)
    for i in range(3, int(number**0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True

  
while True:
    user_input = input("Enter a valid integer (or 0 to quit): ")

    try:
        integer_to_test = int(user_input)
        if integer_to_test == 0:
            print("Quiting application.")
            break
        print(f"The number {integer_to_test} is prime: {is_prime(integer_to_test)}")
    
    except ValueError:
        print("Invalid input. Please enter a valid integer (or 0 to quit).")
