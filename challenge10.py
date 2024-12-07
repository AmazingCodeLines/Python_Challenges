"""
Challenge: Find All Substrings in a Sentence 🔍

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to find all occurrences of a specific word in a given sentence and return their positions.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter a sentence.
    - Prompt the user to enter the word they want to find.

2. Logic:
    - Search for all occurrences of the word in the sentence.
    - Record the starting positions of each occurrence.
    - Allow overlapping matches if applicable.

3. Output:
    - If the word is found, display a list of starting positions where the word occurs.
    - If the word is not found, display a message indicating no matches.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `find_substrings()` that:
    - Takes a sentence and a word as input.
    - Finds and returns all positions of the word in the sentence.

2. Use string methods like `find()` to locate the word's positions efficiently.

3. Handle case sensitivity (e.g., "Hello" and "hello" should be treated as different words).

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Add an option for case-insensitive matching.
2. Allow the user to search for multiple words and display their positions.
3. Handle overlapping matches (e.g., finding "ana" in "banana").

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using string manipulation methods like `find()`.
- Handling input and output with user interaction.
- Iterating through a string to find multiple occurrences.
- Returning and formatting results for readability.
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