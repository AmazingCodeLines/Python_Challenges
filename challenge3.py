
"""
Challenge: Generate a Random Word with NLTK 🎯

---------------------------------------------------
Objective
---------------------------------------------------
Your task is to use NLTK to generate a random word from a given set of English words.

The word must:
    - Be between 5 and 12 characters long.
    - Be in lowercase.
    - Ensure all necessary resources are downloaded properly.

---------------------------------------------------
Instructions
---------------------------------------------------
1. Import Necessary Libraries: 
    - Use the imports provided below.

2. Download Required NLTK Data: 
    - Ensure the words corpus is downloaded. Use the NLTK download utility.

3. Filter and Generate: 
    - Use Python to filter words by length and randomly select one.

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Modify the function so it can:
    - Accept a custom length range (e.g., 6 to 10 characters).
    - Return `None` if no eligible words are found for the given range.
    - Print a clear error message if the words corpus is not downloaded.

2. Bonus Points:
    - Create a list of 10 random words instead of just one.
    - Write an additional function to exclude words that contain any numbers or special characters.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- How to work with NLTK’s words corpus.
- Filtering data using list comprehensions.
- Generating random items from a list.
"""

import nltk
from nltk.corpus import words
import random

nltk.download('words')

word_list = words.words()

def get_random_word(min_length=5, max_length=12):
    eligible_words = [word for word in word_list
                      if min_length <= len(word) <= max_length]
    
    return random.choice(eligible_words).lower()

random_word = get_random_word()

print(f"Generated random word: {random_word}")