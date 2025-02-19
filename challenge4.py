
"""
Challenge 4: Love Score Calculator 💖

Create a Python program that calculates a "love score" between two individuals based on their names. The program should:

Prompt the user to input their first name and the name of their loved one.
Combine both names and convert them to lowercase.
Count the total occurrences of the letters in the word "TRUE" and the word "LOVE" within the combined names.
Form a score by concatenating the counts of "TRUE" and "LOVE."
Display the love score along with the names provided.
"""



user_name = input("Enter your first name: ").lower()
loved_one = input("Enter the name of your loved one: ").lower()

def calculate_love_score(user_name, loved_one):
    combined_names = (user_name + loved_one).lower()

    true_letter_count = sum(combined_names.count(letter) for letter in "true")
    love_letter_count = sum(combined_names.count(letter) for letter in "love")

    score = int(f"{true_letter_count}{love_letter_count}")

    return f"The love score for {user_name} & {loved_one} is {score}."

love_score = calculate_love_score(user_name, loved_one)

print(love_score)