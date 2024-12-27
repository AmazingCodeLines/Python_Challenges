"""
Challenge 17: Normalize File Extensions 🗂️

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to normalize file extensions in filenames.

The program should:
    - Convert filenames to lowercase.
    - Replace the existing file extension with a new one.
    - If no file extension exists, append the new extension.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Accept a filename and a new extension.

2. Logic:
    - Convert the filename to lowercase to ensure case insensitivity.
    - Locate the last dot (`.`) in the filename to identify the existing extension.
    - Replace the current extension with the new extension, or append the new extension if none exists.

3. Output:
    - Return the filename with the normalized extension.

---------------------------------------------------
Examples
---------------------------------------------------
1. Input:
    - Filename: `"My_Document.TXT"`
    - New Extension: `".md"`
   Output: `"my_document.md"`

2. Input:
    - Filename: `"IMAGE.JPEG"`
    - New Extension: `".png"`
   Output: `"image.png"`

3. Input:
    - Filename: `"README"`
    - New Extension: `".txt"`
   Output: `"readme.txt"`

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `normalize_extension(filename, new_extension)` that:
    - Converts the filename to lowercase.
    - Replaces the existing extension or appends the new one.

2. Handle:
    - Filenames with multiple dots (e.g., `"archive.tar.gz"`).
    - Filenames without any extension.

3. Test the function with various filenames and extensions.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to validate file extensions (e.g., ensure they start with a dot `.`).
2. Add functionality to strip extra whitespace from filenames before processing.
3. Handle edge cases, such as filenames that already match the desired extension.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- String manipulation techniques using `lower()`, `rfind()`, and slicing.
- Handling optional components in strings (e.g., file extensions).
- Writing reusable functions for file name processing.
"""


def normalize_extension(filename, new_extension):

    lower_filename = filename.lower()
    
    dot_index = lower_filename.rfind('.')
    
    if dot_index != -1:
        base_name = lower_filename[:dot_index]
        normalized_filename = base_name + new_extension
    else:
        normalized_filename = lower_filename + new_extension
    
    return normalized_filename



# Test Cases
print(normalize_extension("My_Document.TXT", ".md"))  # Expected: "my_document.md"
print(normalize_extension("IMAGE.JPEG", ".png"))       # Expected: "image.png"
print(normalize_extension("archive.tar.gz", ".zip"))   # Expected: "archive.tar.zip"
print(normalize_extension("README", ".txt"))           # Expected: "readme.txt"
print(normalize_extension("photo.PNG", ".jpeg"))       # Expected: "photo.jpeg"
