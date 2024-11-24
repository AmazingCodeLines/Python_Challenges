import nltk
from nltk.corpus import words
import random

from HangmanStages import hangman_stages

"""----------- Generate Random Word -----------"""

# Downloads all the words in the nltk corpus
nltk.download('words')

# Saves the downloaded words
word_list = words.words()

def get_random_word(min_length=5, max_length=14):
    eligible_words = [word for word in word_list
                     if min_length <= len(word) <= max_length]
    
    return random.choice(eligible_words).lower()

# Random word to be guessed
word_to_guess = get_random_word()

"""----------- Mask word -----------"""

def get_masked_word(word_to_guess):
    return ["_"] * len(word_to_guess)

masked_list = get_masked_word(word_to_guess)


"""----------- Game Logic -----------"""
fail_count = 0

while "_" in masked_list and fail_count < len(hangman_stages) - 1:

    print("\n--------- Masked word ---------")
    print(" ".join(masked_list))
    print("\n-------------------------------")
    print(hangman_stages[fail_count])

    user_guess = input("Guess a letter: ").lower()
    
    def update_masked_string(word_to_guess, user_guess, masked_list):
        updated = False
        for index, letter in enumerate(word_to_guess):
            if letter == user_guess:
                masked_list[index] = letter 
                updated = True

        return updated
    
    if not update_masked_string(word_to_guess, user_guess, masked_list):
        fail_count += 1
        print(f"Incorrect guess! You have {len(hangman_stages) - 1 - fail_count} lives remaining.")
            

if "_" not in masked_list:
    print("\nCongratulations! You've guessed the word!")
    print(f"The word was: {word_to_guess}")

else:
    print(hangman_stages[fail_count])
    print("\nGame Over! You've been hanged.")
    print(f"The word was: {word_to_guess}")



    


