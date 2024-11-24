"""
Challenge: FizzBuzz Implementation 🎯

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program that prints numbers from 1 to 100 with the following conditions:

1. For multiples of 3, print "Fizz" instead of the number.
2. For multiples of 5, print "Buzz" instead of the number.
3. For numbers that are multiples of both 3 and 5, print "FizzBuzz".
4. For all other numbers, print the number itself.

---------------------------------------------------
Rules
---------------------------------------------------
1. Range:
    - The program must handle numbers from 1 to 100 (inclusive).

2. Output Requirements:
    - Print each result (number or string) on a new line.

3. Logic:
    - Ensure that numbers divisible by both 3 and 5 are checked **before** checking for individual divisibility by 3 or 5.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a loop to iterate through the numbers from 1 to 100.
2. Use conditional statements to apply the FizzBuzz logic:
    - "FizzBuzz" for numbers divisible by both 3 and 5.
    - "Fizz" for numbers divisible by 3.
    - "Buzz" for numbers divisible by 5.
    - The number itself otherwise.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Modify the program to allow the user to specify a custom range (e.g., 1 to 50).
2. Add an option for the user to customize the Fizz and Buzz values (e.g., multiples of 4 and 6).
3. Print all results in a single line separated by commas, instead of one per line.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Implementing conditional logic.
- Using loops to iterate through a sequence of numbers.
- Applying basic modulo arithmetic.
"""




import random

number_range = range(1, 101)

for i in number_range:
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    elif i % 3 == 0:
        print("Fizz")
    
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)