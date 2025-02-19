"""
Challenge 10: Find All Substrings in a Sentence 🔍

Create a Python program that finds all occurrences of a specific word within a given sentence. The program should:

Prompt the user to:
Enter a sentence.
Enter a word to search for within the sentence.
Search for all instances of the word in the sentence, including overlapping occurrences.
Store and display the starting index positions of each occurrence.
Indicate if the word is not found.
"""


def find_substrings():
    sentence = input("Enter a sentence: ").strip()
    word = input("Enter a word to find: ").strip()

    positions = []
    start = 0

    while start < len(sentence):
        start = sentence.find(word, start)

        if start == -1:
            break
        
        positions.append(start)
        start += 1

    if positions:
        print(f"The word '{word}' is found at positions: {positions}")
    else:
        print("Word not found")


find_substrings()