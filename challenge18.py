"""
Challenge 18: Random City Selector 🌍

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to randomly select a specified number of cities from a predefined list.

The program should:
    - Allow the user to specify how many cities to select.
    - Randomly select the specified number of cities from the list.
    - Ensure the selection is valid (i.e., not more than the total number of cities available).

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Accept the number of cities to select as an integer.
    - Allow the user to quit the program by entering `0`.

2. Logic:
    - Use the `random.sample()` function to randomly select unique cities from the list.
    - Validate the user's input to ensure it is within the range of 1 to the number of available cities.
    - Handle cases where the user enters invalid input (e.g., non-integer values or numbers out of range).

3. Output:
    - Display the randomly selected cities.
    - Provide meaningful error messages for invalid inputs.

---------------------------------------------------
Examples
---------------------------------------------------
1. Input:
    - Number of cities to select: `3`
   Output: `["London", "Tokyo", "Sydney"]` (results may vary due to randomness)

2. Input:
    - Number of cities to select: `0`
   Output: `"Goodbye!"`

3. Input:
    - Number of cities to select: `10`
   Output: `"Error: Number of cities to select exceeds the available cities."`

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `choose_city(cities, number)` that:
    - Accepts a list of cities and the number of cities to select.
    - Returns a list of randomly selected cities.
    - Raises a `ValueError` if the number of cities to select exceeds the total available.

2. Use a loop to allow multiple selections until the user chooses to quit.

3. Ensure robust error handling for invalid inputs.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to allow the user to add or remove cities from the list dynamically.
2. Display the remaining cities after each selection.
3. Prevent duplicate cities from being added to the list.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using Python's `random` module for randomness.
- Validating and handling user input.
- Iterating through user interactions with loops.
- Implementing exception handling with `try` and `except`.
"""


import random

# Predefined list of cities
cities = ["New York", "Tokyo", "London", "Paris", "Sydney", "Berlin", "Toronto", "Dubai"]



def choose_city(cities, number):
  
    if number > len(cities):
        raise ValueError("Number of cities to select exceeds the available cities.")
    return random.sample(cities, k=number)


while True:
    user_input = input(f"Enter the number of cities to select (1-{len(cities)}), or 0 to quit: ")
    try:
        num = int(user_input)
        if num == 0:
            print("Goodbye!")
            break
        selected = choose_city(cities, num)
        print("Selected Cities:", selected)
    except ValueError as ve:
        print("Error:", ve)
