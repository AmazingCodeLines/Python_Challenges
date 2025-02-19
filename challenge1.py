"""
Challenge 1: FizzBuzz Implementation 🎯

Write a Python program that iterates through a sequence of numbers from 1 to 100. For each number, the program should apply the following rules:

If the number is divisible by both 3 and 5, print a specific word.
If the number is divisible only by 3, print another specific word.
If the number is divisible only by 5, print a different word.
If none of the above conditions apply, print the number itself.
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