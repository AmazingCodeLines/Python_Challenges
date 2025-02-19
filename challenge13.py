
"""
Challenge 13: Count Unique Characters in a String 🔤

Create a Python program that counts the number of unique characters in a given string. The program should:

Define a function that:
Removes all spaces from the input string.
Identifies all unique characters in the cleaned string.
Returns the count of these unique characters.
Prompt the user with a predefined string (or allow them to input their own string).
Display the total number of unique characters found in the string.
"""



def count_unique_characters(input_string):

    cleaned_string = input_string.replace(" ", "")
    unique_characters = set(cleaned_string)

    return len(unique_characters)


input_string = "This is a test string."
unique_count = count_unique_characters(input_string)

print(f"The number of unique characters in the string is: {unique_count}")

