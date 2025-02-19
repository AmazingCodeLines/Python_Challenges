"""
Challenge 17: Normalize File Extensions 🗂️

Create a Python program that normalizes the file extension of a given filename. The program should:

Define a function that:
Converts the entire filename to lowercase.
Checks if the filename already has an extension.
If it does, replace the existing extension with the specified new extension.
If it does not, append the new extension to the filename.
Return the updated filename with the normalized extension.
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
