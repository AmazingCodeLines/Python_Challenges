"""
Challenge 11: URL Cleaner 🌐

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to clean a list of URLs by standardizing their format and separating invalid or unsupported URLs.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - A list of URLs, which may have inconsistent protocols (`http://`, `https://`, or none) or trailing slashes.

2. Logic:
    - If a URL starts with `http://`, replace it with `https://`.
    - If a URL does not have any protocol (`://`), add `https://` as the default.
    - Remove unnecessary trailing slashes from the URLs.
    - Identify and separate URLs with unsupported protocols (e.g., `ftp://`).

3. Output:
    - Return two lists:
        - **Cleaned URLs**: A list of standardized URLs.
        - **Exception URLs**: A list of URLs with unsupported protocols or errors.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `clean_urls(urls)` that:
    - Accepts a list of URLs.
    - Returns two lists: cleaned URLs and exception URLs.

2. Process:
    - Use string manipulation methods like `startswith()` and slicing to handle protocols and paths.

3. Ensure:
    - The cleaned URLs have consistent formatting.
    - The exception URLs are identified and separated correctly.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to check for valid domain names in the URLs.
2. Handle query parameters and fragments in the URLs without altering their structure.
3. Allow the program to display detailed reasons why URLs are in the exceptions list (e.g., unsupported protocol, invalid format).

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- String manipulation techniques for processing and formatting data.
- Handling different URL structures and edge cases.
- Separating valid and invalid inputs programmatically.
- Iterating through lists and applying conditional logic effectively.
"""


def cleaned_urls(urls):
    cleaned_urls = []
    exceptions = []

    for url in urls:
        if url.startswith("https://"):
            clean_url = url
        elif url.startswith("http://"):
            clean_url = "https://" + url[len("http://"):]
        elif "://" not in url:
            clean_url = "https://" + url
        else:
            exceptions.append(url.rstrip("/"))
            continue

        clean_url = clean_url.rstrip("/")

        cleaned_urls.append(clean_url)
    return cleaned_urls, exceptions


input_urls = [
    'http://example.com/',
    'https://example.com/test/',
    'http://example.org/path//',
    'https://www.sample.com///',
    'http://subdomain.example.net/path/to/resource/',
    'https://no-trailing-slash.com',
    'http://mixedprotocol.com/path/',
    'ftp://unsupportedprotocol.com/', 
    'www.missingprotocol.com/',
    'http://example.com/path?query=123/',
]

call_cleaned_urls, call_exceptions = cleaned_urls(input_urls)
# print("\n ----- Original URLs _____")
for url in input_urls:
    print(url)

print("\n ----- Cleaned URLs -----")
for url in call_cleaned_urls:
    print(url)

print("\n ----- Exceptions -----")
for url in call_exceptions:
    print(url)
    