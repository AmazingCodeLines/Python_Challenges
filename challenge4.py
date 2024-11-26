
"""
Challenge: Love Score Calculator 💖

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program that calculates the "Love Score" between two people based on the occurrence of specific letters in their names.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt the user to enter their name.
    - Prompt the user to enter the name of their loved one.

2. Logic:
    - Combine the two names into a single string (case-insensitive).
    - Count the occurrences of the letters in the word "TRUE" to get the "True" count.
    - Count the occurrences of the letters in the word "LOVE" to get the "Love" count.
    - Combine the "True" count and the "Love" count to form the final Love Score (e.g., if True Count = 4 and Love Count = 7, the score is 47).

3. Output:
    - Display the Love Score in the format: 
      `"The love score for [User Name] & [Loved One] is [Score]."`

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function called `calculate_love_score` that:
    - Accepts two names as inputs.
    - Calculates and returns the Love Score.

2. Make the program case-insensitive by converting all inputs to lowercase.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Add validation to ensure the user enters non-empty names.
2. Display a fun message based on the score:
    - If the score is greater than 80, display: `"You are a perfect match!"`
    - If the score is between 50 and 80, display: `"You are a good match!"`
    - If the score is less than 50, display: `"You may need to work on your relationship."`

3. Allow the user to calculate the Love Score for multiple pairs without restarting the program.

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using string manipulation and counting characters.
- Writing and using custom functions.
- Handling and combining user input for meaningful output.
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