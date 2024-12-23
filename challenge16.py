"""
Challenge: Anagram Checker 🔄

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to determine if two given strings are anagrams.

An anagram is a word or phrase formed by rearranging the letters of another, 
typically using all the original letters exactly once.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Accept two strings as input to check if they are anagrams.

2. Logic:
    - Ignore spaces and case when comparing the strings.
    - Sort the characters in both strings and compare the results.
    - Return `True` if the sorted strings match, and `False` otherwise.

3. Output:
    - Display `True` if the two strings are anagrams.
    - Display `False` if they are not.

---------------------------------------------------
Examples
---------------------------------------------------
1. Input:
    - `str1 = "Listen!"`
    - `str2 = "Silent!"`
   Output: `True` (ignoring case and spaces, the letters match after sorting)

2. Input:
    - `str1 = "Hello"`
    - `str2 = "World"`
   Output: `False` (the letters do not match)

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `are_anagrams(str1: str, str2: str) -> bool` that:
    - Accepts two strings.
    - Processes the strings to remove spaces and convert them to lowercase.
    - Sorts the characters in each string and compares them.

2. Handle:
    - Case insensitivity.
    - Spaces in the strings.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to ignore punctuation (e.g., `Listen!` and `Silent!` should still be considered anagrams).
2. Allow the user to input strings interactively.
3. Handle edge cases, such as empty strings or strings with different lengths before processing.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- String manipulation techniques such as `replace()` and `lower()`.
- Sorting and comparing sequences.
- Implementing reusable functions for string analysis.
"""




def are_anagrams(str1: str, str2: str) -> bool:
 

    processed_str1 = str1.replace(" ", "").lower()
    processed_str2 = str2.replace(" ", "").lower()
    
    sorted_str1 = sorted(processed_str1)
    sorted_str2 = sorted(processed_str2)
    
    return sorted_str1 == sorted_str2

str1 = "Listen!"
str2 = "Silent!"

print(are_anagrams(str1, str2))