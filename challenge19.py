"""
Challenge 19: Title Consistency Checker 📝

---------------------------------------------------
Objective
---------------------------------------------------
Create a function `check_title_consistency(titles)` that takes a list of titles and checks if all titles follow a consistent casing format.

---------------------------------------------------
Predefined Formats
---------------------------------------------------
1. **Uppercase**: All letters are uppercase.
2. **Lowercase**: All letters are lowercase.
3. **Capitalized**: Only the first character of the title is uppercase; the rest are lowercase.
4. **Title Case**: The first character of each word is uppercase; the rest are lowercase.

---------------------------------------------------
Instructions
---------------------------------------------------
1. **Define the Function**:
    - Create a function `check_title_consistency(titles)` that:
        - Returns the consistent format's name if all titles match one predefined format.
        - Returns `"Inconsistent Formatting"` if the titles do not all match the same format.

2. **Examples**:
    ```python
    titles1 = ["Introduction to Python", "Advanced Python Techniques", "Python in Data Science"]
    print(check_title_consistency(titles1))  # Output: "Title Case"

    titles2 = ["python basics", "Python Advanced", "PYTHON Intermediate"]
    print(check_title_consistency(titles2))  # Output: "Inconsistent Formatting"
    ```

3. **Solution Approach**:
    - **Define Format Checks**: For each format, determine a way to check if a title conforms to it.
    - **Iterate and Compare**: For each format, check if all titles match the format.
    - **Determine Consistency**:
        - If all titles match exactly one format, return that format's name.
        - If titles match multiple formats or none, return `"Inconsistent Formatting"`.

4. **Edge Cases**:
    - **Empty Titles**: An empty string (`""`) can be considered to match all formats since transformations on it result in an empty string.
    - **Single Title**: A list with a single title should return the format it matches.
    - **Multiple Matching Formats**: If all titles match more than one format, prioritize the most specific format or indicate inconsistency.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Handle mixed-case formats (e.g., `PyThOn BasiCs`) and return `"Inconsistent Formatting"` for such cases.
2. Extend the function to suggest corrections for inconsistent titles.
3. Optimize the function to minimize redundant checks.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Implementing and applying string transformation methods.
- Iterating through lists and comparing results.
- Handling edge cases and ensuring robustness in algorithms.
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
