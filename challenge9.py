"""
Challenge 9: Clean Irregular CSV Data 🧹

Create a Python program that cleans CSV-style data by removing unnecessary spaces. The program should:

Take a list of strings where each string represents a CSV row with potential extra spaces.
Define a function that:
Strips leading and trailing whitespace from each row.
Removes extra spaces surrounding the comma that separates values.
Return the cleaned list with properly formatted rows.
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
