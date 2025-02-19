"""
Challenge 18: Random City Selector 🌍

Create a Python program that randomly selects a specified number of cities from a predefined list. The program should:

Define a list containing several city names.
Implement a function that:
Takes the list of cities and a number representing how many cities to select.
Returns a random selection of the specified number of unique cities.
Raises an error if the requested number exceeds the available number of cities.
Continuously prompt the user to:
Enter the number of cities they want to select.
Display the selected cities.
Exit the program if the user enters zero.
Handle invalid inputs and provide appropriate error messages.
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
