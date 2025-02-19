"""
Challenge 14: Leap Year Checker 📅

Create a Python program that checks whether a given year is a leap year. The program should:

Define a function that:
Returns True if the year is a leap year based on the following conditions:
The year is divisible by 4, and
The year is not divisible by 100, unless it is also divisible by 400.
Returns False otherwise.
Prompt the user to enter a year.
Display whether the entered year is a leap year or not.
"""


def is_leap_year(year):
 
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


year_to_check = int(input("Enter a year to check if it's a leap year: "))
print(f"Is {year_to_check} a leap year? {is_leap_year(year_to_check)}")
