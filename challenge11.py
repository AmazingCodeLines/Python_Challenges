"""
Challenge 11: URL Cleaner 🌐

Challenge Description:

Create a Python program that standardizes and cleans a list of URLs. The program should:

Define a function that:
Converts all URLs to use the https:// protocol:
If the URL starts with http://, replace it with https://.
If the URL lacks a protocol, prepend https://.
If the URL uses an unsupported protocol (e.g., ftp://), add it to an exceptions list.
Remove all trailing slashes (/) from the URLs.
Return:
A list of cleaned URLs with consistent formatting.
A separate list of URLs that could not be processed due to unsupported protocols.
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
    