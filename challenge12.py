
"""
Challenge 12: Build a Simple Calculator 🧮

Create a Python calculator that can perform basic arithmetic operations. The program should:

Define separate functions for:
Addition: Adds two numbers.
Subtraction: Subtracts the second number from the first.
Multiplication: Multiplies two numbers.
Division: Divides the first number by the second, handling division by zero with an appropriate error message.
Use a dictionary to map mathematical operators (+, -, *, /) to the corresponding functions.
Implement robust input validation:
Prompt the user repeatedly until they provide a valid numeric input.
Ensure the user selects a valid mathematical operation.
Continuously allow calculations until the user chooses to exit:
After displaying each result, ask if the user wants to perform another calculation.
Exit gracefully if the user chooses not to continue.
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
