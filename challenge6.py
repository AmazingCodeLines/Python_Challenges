"""
Challenge 6: Prime Number Checker 🔢

Create a Python program that continuously checks whether a user-provided number is prime. The program should:

Define a function that:
Returns False for numbers less than or equal to 1, as these are not prime.
Returns True for the number 2.
Eliminates even numbers greater than 2 immediately.
Checks for divisibility only by odd numbers up to the square root of the input number for efficiency.
Implement a loop that:
Prompts the user to enter an integer.
Ends the loop and exits the application if the user enters 0.
Displays whether the entered number is prime using the defined function.
Handles invalid inputs gracefully by prompting the user again.
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
