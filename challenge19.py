"""
Challenge 19: Title Consistency Checker 📝

Create a Python program that checks the consistency of title formatting across a list of strings. The program should:

Define a function that:
Evaluates each title against predefined formatting rules:
Uppercase: All letters in the title are uppercase.
Lowercase: All letters in the title are lowercase.
Capitalized: Only the first letter of the first word is uppercase, and the rest are lowercase.
Title Case: The first letter of each significant word is uppercase.
Returns the matching format if all titles share the same style.
Returns "Inconsistent Formatting" if no single format applies to all titles.
Include various test cases to verify the function's correctness, handling:
Titles with special characters, numbers, emojis, acronyms, and hyphenated words.
Titles with different letter cases, leading/trailing spaces, and non-ASCII characters.
Scenarios with an empty list or a single title.
"""


def check_title_consistency(titles):

    # Define predefined format checks
    def is_uppercase(title):
        return title.isupper()
    
    def is_lowercase(title):
        return title.islower()
    
    def is_capitalized(title):
        return title == title.capitalize()
    
    def is_title_case(title):
        return title == title.title()
    
    # Mapping format names to their checking functions
    formats = {
        "Uppercase": is_uppercase,
        "Lowercase": is_lowercase,
        "Capitalized": is_capitalized,
        "Title Case": is_title_case,
    }
    
    # Check which formats the titles conform to
    matching_formats = {format_name: all(check(title) for title in titles) for format_name, check in formats.items()}
    
    # Filter formats where all titles match
    matched_formats = [format_name for format_name, matches in matching_formats.items() if matches]
    
    # Determine result
    if len(matched_formats) == 1:
        return matched_formats[0]
    return "Inconsistent Formatting"




# Test Case 1: Standard Title Case Consistency
titles1 = ["Introduction to Python", "Advanced Python Techniques", "Python in Data Science"]
print(check_title_consistency(titles1))  # Expected: "Title Case"

# Test Case 2: Inconsistent Formatting
titles2 = ["python basics", "Python Advanced", "PYTHON Intermediate"]
print(check_title_consistency(titles2))  # Expected: "Inconsistent Formatting"

# Test Case 3: All Uppercase Titles
titles3 = ["INTRODUCTION TO PYTHON", "ADVANCED PYTHON TECHNIQUES", "PYTHON IN DATA SCIENCE"]
print(check_title_consistency(titles3))  # Expected: "Uppercase"

# Test Case 4: All Lowercase Titles
titles4 = ["introduction to python", "advanced python techniques", "python in data science"]
print(check_title_consistency(titles4))  # Expected: "Lowercase"

# Test Case 5: All Capitalized Titles
titles5 = ["Introduction to python", "Advanced python techniques", "Python in data science"]
print(check_title_consistency(titles5))  # Expected: "Capitalized"

# Test Case 6: Mixed Case with Punctuation
titles6 = ["Introduction to Python!", "Advanced Python Techniques.", "Python in Data Science?"]
print(check_title_consistency(titles6))  # Expected: "Title Case"

# Test Case 7: Titles with Numbers
titles7 = ["Python 101", "Advanced Python Techniques 2025", "Python in Data Science 3"]
print(check_title_consistency(titles7))  # Expected: "Title Case"

# Test Case 8: Titles with Special Characters
titles8 = ["Introduction to Python#", "Advanced-Python Techniques", "Python in Data Science!"]
print(check_title_consistency(titles8))  # Expected: "Title Case"

# Test Case 9: Empty List of Titles
titles9 = []
print(check_title_consistency(titles9))  # Expected: "Inconsistent Formatting"

# Test Case 10: Single Title
titles10 = ["Introduction to Python"]
print(check_title_consistency(titles10))  # Expected: "Title Case"

# Test Case 11: Titles with Non-ASCII Characters
titles11 = ["Introducción a Python", "Avanzado Técnicas de Python", "Python en Ciencia de Datos"]
print(check_title_consistency(titles11))  # Expected: "Title Case"

# Test Case 12: Titles with Mixed Formats but Uniform Case
titles12 = ["INTRODUCTION TO PYTHON", "INTRODUCTION TO PYTHON", "INTRODUCTION TO PYTHON"]
print(check_title_consistency(titles12))  # Expected: "Uppercase"

# Test Case 13: Titles with Leading and Trailing Whitespaces
titles13 = ["  Introduction to Python", "Advanced Python Techniques  ", "  Python in Data Science  "]
print(check_title_consistency(titles13))  # Expected: "Title Case"

# Test Case 14: Titles with Mixed Letter Cases
titles14 = ["Introduction to PYTHON", "Advanced python Techniques", "Python in DATA Science"]
print(check_title_consistency(titles14))  # Expected: "Inconsistent Formatting"

# Test Case 15: Titles with All Letters the Same but Mixed Case
titles15 = ["PYTHON", "python", "Python"]
print(check_title_consistency(titles15))  # Expected: "Inconsistent Formatting"

# Test Case 16: Titles with Only One Word
titles16 = ["Python", "PYTHON", "python"]
print(check_title_consistency(titles16))  # Expected: "Inconsistent Formatting"

# Test Case 17: Titles with Numbers and Mixed Cases
titles17 = ["Python 101", "PYTHON 202", "python 303"]
print(check_title_consistency(titles17))  # Expected: "Inconsistent Formatting"

# Test Case 18: Titles with Emojis
titles18 = ["Introduction to Python 😊", "Advanced Python Techniques 🚀", "Python in Data Science 📊"]
print(check_title_consistency(titles18))  # Expected: "Title Case"

# Test Case 19: Titles with Acronyms
titles19 = ["Introduction to AI and ML", "Advanced AI Techniques", "AI in Data Science"]
print(check_title_consistency(titles19))  # Expected: "Title Case"

# Test Case 20: Titles with Hyphenated Words
titles20 = ["Introduction to Python-Programming", "Advanced Python-Techniques", "Python-in-Data Science"]
print(check_title_consistency(titles20))  # Expected: "Title Case"
