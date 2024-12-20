
"""
Challenge: Count Unique Characters in a String 🔤

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program that takes a string and calculates the number of unique characters it contains, excluding spaces.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter a string.

2. Logic:
    - Remove all spaces from the input string using the `replace()` method.
    - Count the number of unique characters using a set, as sets only store distinct values.

3. Output:
    - Display the total number of unique characters in the string.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `count_unique_characters(input_string)` that:
    - Accepts a string as input.
    - Returns the count of unique characters after removing spaces.

2. Handle:
    - Case sensitivity (e.g., "A" and "a" should be treated as different characters).
    - Ensure spaces do not contribute to the count.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to display the unique characters themselves in addition to their count.
2. Add an option to ignore case, treating "A" and "a" as the same character.
3. Handle punctuation and special characters as part of the count unless explicitly excluded.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using the `replace()` method to modify strings.
- Working with sets to extract unique values.
- Writing reusable functions for string manipulation.
- Handling user input and formatting output.
"""



def count_unique_characters(input_string):

    cleaned_string = input_string.replace(" ", "")
    unique_characters = set(cleaned_string)

    return len(unique_characters)


input_string = "This is a test string."
unique_count = count_unique_characters(input_string)

print(f"The number of unique characters in the string is: {unique_count}")

