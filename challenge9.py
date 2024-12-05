"""
Challenge: Clean Irregular CSV Data 🧹

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to clean and reformat a list of CSV-like strings with inconsistent spacing. The goal is to standardize the format by removing unnecessary spaces while preserving the data structure.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - A list of strings where each string represents a CSV entry with irregular formatting (e.g., extra spaces around values or commas).

2. Logic:
    - For each string in the list:
        - Strip leading and trailing spaces.
        - Remove unnecessary spaces around the commas separating values.
    - Return a new list with cleaned and properly formatted strings.

3. Output:
    - Display the cleaned list of strings.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `clean_csv_data(data_list)` that:
    - Accepts a list of CSV-like strings as input.
    - Returns a cleaned list with standardized formatting.

2. Process:
    - Use string manipulation methods like `strip()` and `split()` to clean and reformat the strings.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to handle different delimiters (e.g., semicolons `;` instead of commas `,`).
2. Add functionality to remove duplicate entries from the cleaned list.
3. Ensure that all values are in lowercase or uppercase for uniformity (optional).

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using string methods for cleaning and manipulation.
- Writing reusable functions to process lists of data.
- Handling irregular input and standardizing formats.
- Applying list comprehensions for concise data processing.
"""



# Sample 
data = [" John,25 ", " Alice, 30 ", " Bob , 35 "]


def clean_csv_data(data_list):
    cleaned_list = []
    for item in data_list:
        # Strip leading and trailing whitespace
        cleaned_item = item.strip()
        # Remove unnecessary spaces around the comma
        cleaned_item = ",".join(part.strip() for part in cleaned_item.split(","))
        cleaned_list.append(cleaned_item)
    return cleaned_list

cleaned_data = clean_csv_data(data)

print("Cleaned Data:", cleaned_data)
