"""
Countdown Iterator ⏳ 
Description:
This Python project defines a custom iterator that generates a countdown sequence starting from a specified number down to zero. The class implements Python’s iterator protocol by defining __iter__() and __next__() methods, making it iterable in loops and list comprehensions.

Key Features:
✔ Implements a custom iterator using Python's built-in __iter__() and __next__() methods
✔ Counts down from a given starting number to zero
✔ Uses StopIteration to gracefully stop iteration when the countdown reaches below zero
✔ Can be converted to a list or used directly in a loop
"""


class Countdown:
    def __init__(self, start):
        self.start = start

    def __iter__(self):
        self.current = self.start
        return self

    def __next__(self):
        if self.current < 0:
            raise StopIteration
        else:
            result = self.current
            self.current -= 1
            return result

# Create an instance of Countdown starting from 5
countdown = Countdown(5)

# Convert the Countdown instance to a list
countdown_list = list(countdown)

print(countdown_list)
