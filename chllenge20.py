""""
🛠 Dynamic User Profile Builder
Description:
This Python project allows for the creation of dynamic user profiles using flexible keyword arguments. It takes a user's first and last name as mandatory inputs and allows additional attributes such as location, profession, age, and hobbies to be added dynamically.

Key Features:
✔ Uses keyword arguments (**kwargs) to handle any number of additional attributes
✔ Creates structured dictionaries containing user information
✔ Easily extendable to store and process various user details
"""



def build_profile(first, last, **kwargs):
    profile = {
        "first_name": first,
        "last_name": last
    }

    for key, value in kwargs.items():
        profile[key] = value
    
    return profile


user_profile = build_profile(
    "Alice",
    "Smith",
    location="New York",
    field="Computer Science",
    age=30,
    hobby="Reading"
)

print(user_profile)
