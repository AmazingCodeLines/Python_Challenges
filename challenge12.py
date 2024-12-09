
"""
Challenge: Build a Simple Calculator 🧮

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program that allows users to perform basic arithmetic operations interactively.

The calculator should:
    - Add, subtract, multiply, and divide two numbers.
    - Handle invalid inputs gracefully.
    - Allow users to perform multiple calculations in a single session.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter two numbers (float or integer).
    - Prompt the user to choose an operation (`+`, `-`, `*`, `/`).
    - Allow the user to continue performing calculations or exit the program.

2. Logic:
    - Use separate functions for each arithmetic operation (addition, subtraction, multiplication, and division).
    - Use a dictionary to map operations (`+`, `-`, `*`, `/`) to their corresponding functions.
    - Handle division by zero with a clear error message.

3. Output:
    - Display the result of the chosen operation in a user-friendly format.
    - Provide error messages for invalid inputs or unsupported operations.

4. Loop:
    - Allow the user to perform calculations repeatedly until they choose to exit.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Implement the following functions:
    - `addition(first_number, second_number)`
    - `subtraction(first_number, second_number)`
    - `multiplication(first_number, second_number)`
    - `division(first_number, second_number)` (ensure it handles division by zero).

2. Use a dictionary to manage the mapping between operations and functions.

3. Implement input validation for:
    - Numeric values.
    - Valid operations.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the calculator to support more operations, such as exponentiation (`^`) or modulo (`%`).
2. Add functionality to handle multiple operations in a single input, e.g., "5 + 3 - 2".
3. Allow the user to recall the result of the last calculation and use it in the next operation.
4. Provide a history of all calculations performed during the session.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Writing reusable functions for specific tasks.
- Handling user input and validation in interactive programs.
- Using dictionaries to map operations to functions dynamically.
- Implementing loops for continuous interaction with the user.
"""



def addition(first_number, second_number):
    return first_number + second_number

def subtraction(first_number, second_number):
    return first_number - second_number

def multiplication(first_number, second_number):
    return first_number * second_number

def division(first_number, second_number):
    if second_number == 0:
        raise ValueError("Cannot divide by zero")
    return first_number / second_number

operations_dictionary = {
    "+": addition,
    "-": subtraction,
    "/": division,
    "*": multiplication
}

def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a numeric value.")

def get_operation() -> str:
    while True:
        operation = input(
            "Choose an operation:\n"
            "[+] Addition\n"
            "[-] Subtraction\n"
            "[*] Multiplication\n"
            "[/] Division\n"
            "Enter your choice: "
        )
        if operation in operations_dictionary:
            return operation
        else:
            print("Invalid operation. Please choose a valid operator.")


print("=== Welcome to the Python Calculator ===")

while True:
    first_number = get_number("Enter the first number: ")
    operation = get_operation()
    second_number = get_number("Enter the second number: ")

    try:
        result = operations_dictionary[operation](first_number, second_number)
        print(f"\nResult: {first_number} {operation} {second_number} = {result}\n")
    except ValueError as e:
        print(f"Error: {e}\n")

    continue_calculation = input("Do you want to perform another calculation? (y/n): ").strip().lower()

    if continue_calculation != "y":
        print("Thank you for using the Python Calculator. Goodbye!")
        break
