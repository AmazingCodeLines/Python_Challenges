
"""
Challenge 3: Generate a Random Word with NLTK 🎯

Write a Python program that generates a random word from a predefined English dictionary. The program should:

Download and use a list of English words from an external library.
Filter the words based on a specified minimum and maximum length.
Select one random word from the filtered list.
Display the selected word in lowercase.
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