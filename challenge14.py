"""
Challenge 18: Leap Year Checker 📅

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to determine whether a given year is a leap year.

A leap year occurs:
1. Every 4 years.
2. Except for years that are divisible by 100 but not divisible by 400.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter a year as an integer.

2. Logic:
    - A year is a leap year if:
        - It is divisible by 4, AND
        - It is NOT divisible by 100, unless it is also divisible by 400.

3. Output:
    - Display `True` if the year is a leap year.
    - Display `False` otherwise.

---------------------------------------------------
Examples
---------------------------------------------------
1. Input: `2000`
   Output: `True` (2000 is divisible by 400 and is a leap year).

2. Input: `1900`
   Output: `False` (1900 is divisible by 100 but not by 400).

3. Input: `2024`
   Output: `True` (2024 is divisible by 4 and not by 100).

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `is_leap_year(year)` that:
    - Accepts an integer as input.
    - Returns `True` if the year is a leap year, and `False` otherwise.

2. Use the leap year rules for accuracy.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to allow the user to check multiple years in a single session.
2. Add input validation to ensure the user enters a valid year (e.g., no negative years or non-numeric values).
3. Provide a feature to list all leap years within a given range.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using conditional statements to implement rules.
- Handling user input and validating data.
- Writing reusable functions for specific calculations.
"""


def is_leap_year(year):
 
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True
    else:
        return False


year_to_check = int(input("Enter a year to check if it's a leap year: "))
print(f"Is {year_to_check} a leap year? {is_leap_year(year_to_check)}")
