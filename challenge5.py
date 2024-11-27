"""
Challenge: Temperature Converter 🌡️

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program that converts temperatures between Celsius and Fahrenheit.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to input a temperature in Celsius (optional).
    - Prompt the user to input a temperature in Fahrenheit (optional).
    - Allow the user to skip either input by pressing "Enter".

2. Logic:
    - If a Celsius temperature is provided, convert it to Fahrenheit using the formula:
        Fahrenheit = (Celsius × 9/5) + 32
    - If a Fahrenheit temperature is provided, convert it to Celsius using the formula:
        Celsius = (Fahrenheit − 32) × 5/9
    - Validate that the inputs are numeric. If not, display an error message.

3. Output:
    - Display the results with appropriate formatting (e.g., 2 decimal places).
    - Ensure the output clearly shows which temperature was converted.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write two separate functions:
    - `celsius_to_fahrenheit(celsius)` for converting Celsius to Fahrenheit.
    - `fahrenheit_to_celsius(fahrenheit)` for converting Fahrenheit to Celsius.

2. Handle user input with error handling:
    - Validate the input to ensure it is numeric.
    - Allow the program to gracefully handle invalid inputs (e.g., non-numeric values).

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to allow the user to perform multiple conversions without restarting.
2. Add a feature to handle temperatures below absolute zero (Celsius < -273.15 or Fahrenheit < -459.67) with a warning.
3. Format the output with units and proper alignment for readability.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Writing functions to perform specific tasks.
- Handling user input with validation.
- Applying mathematical formulas in programming.
- Formatting numerical output for better readability.
"""



def celsius_to_fahrenheit(celsius):
    fahrenheit = ((9 / 5) * celsius) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * (5 / 9)
    return celsius

try:
    celsius_input = input("Enter the temperture in degrees Celsius (or press enter to continue): ")
    fahrenheit_input = input("Enter the temperature in degrees Fahrenheit (or press enter to continue): ")

    celsius = None
    fahrenheit = None

    if celsius_input.strip():
        celsius = float(celsius_input)
    if fahrenheit_input.strip():
        fahrenheit = float(fahrenheit_input)

    if celsius is not None:
        print(f"Celsius {celsius}°C is {celsius_to_fahrenheit(celsius):.2f}°F.")
    if fahrenheit is not None:
        print(f"Fahrenheit {fahrenheit}°F is {fahrenheit_to_celsius(fahrenheit):.2f}°F")

except ValueError:
    print("Invalid input. Please enter valid numbers.")
