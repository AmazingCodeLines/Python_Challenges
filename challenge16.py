"""
Challenge 16: Anagram Checker 🔄

Create a Python program that checks whether two given strings are anagrams of each other. The program should:

Define a function that:
Removes all spaces from both strings.
Converts both strings to lowercase for case-insensitive comparison.
Sorts the characters in each string.
Compares the sorted results to determine if the strings are anagrams.
Prompt the user to enter two strings or use predefined strings.
Display True if the strings are anagrams and False otherwise.
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