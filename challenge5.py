"""
Challenge 5: Temperature Converter 🌡️

Create a Python program that converts temperatures between Celsius and Fahrenheit. The program should:

Define two functions:
One for converting Celsius to Fahrenheit.
Another for converting Fahrenheit to Celsius.
Prompt the user to:
Enter a temperature in Celsius (or skip by pressing Enter).
Enter a temperature in Fahrenheit (or skip by pressing Enter).
Perform the appropriate conversions based on the user's input.
Display the converted temperatures with two decimal places.
Handle invalid inputs gracefully by displaying an error message when non-numeric values are entered.
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
