""" 
Challenge: Silent Auction Program 🏆

---------------------------------------------------
Objective
---------------------------------------------------
Write a Python program to simulate a silent auction. Participants enter their names and bids without knowing what others have bid. At the end, the program announces the highest bidder and their bid amount.

---------------------------------------------------
Rules
---------------------------------------------------
1. Input:
    - Prompt users to enter their name and bid amount.
    - Allow multiple participants to submit bids.
    - Ask if there are more bidders after each entry.
    - End the bidding process when no more bidders are present.

2. Logic:
    - Store all bids in a dictionary where keys are participant names and values are their bid amounts.
    - Determine the highest bid and the corresponding bidder.
    - Sort all bids in descending order for final standings.

3. Output:
    - Announce the highest bidder and their bid amount.
    - Display the final standings (all bids sorted in descending order).

---------------------------------------------------
Challenge Requirements
---------------------------------------------------
1. Write a function `get_highest_bidder(offers)` that:
    - Accepts the dictionary of bids as input.
    - Returns the sorted bids and the highest bidder.

2. Handle user input:
    - Ensure bids are numeric values.
    - Gracefully handle invalid inputs, such as non-numeric bids.

3. Loop:
    - Allow multiple users to place bids until the auction is explicitly closed.

---------------------------------------------------
Bonus Points
---------------------------------------------------
1. Extend the program to allow ties:
    - Display all bidders who submitted the highest bid.
2. Add a minimum bid increment:
    - Require each new bid to exceed the current highest bid by a certain amount.
3. Format the output to display standings neatly, e.g., "Name: $Amount".

---------------------------------------------------
What You’ll Learn
---------------------------------------------------
- Using dictionaries to store and sort data.
- Writing functions to encapsulate logic.
- Handling loops for iterative user input.
- Sorting and working with dictionary items.
"""


def get_highest_bidder(offers):
    sorted_bids = dict(sorted(offers.items(), key=lambda item: item[1], reverse=True))
    highest_bidder = list(sorted_bids.items())[0]

    return sorted_bids, highest_bidder

bids = {}

while True:
    name = input("Please enter your name: ")
    bid = float(input("Please enter your bid: "))

    bids[name] = bid

    new_bid = input("Is there other bid? (Y/N): ").strip().upper()

    if new_bid == "N":
        break

sorted_bids, highest_bidder = get_highest_bidder(bids)


print(f"The highest bidder is {highest_bidder[0]} with an offer of ${highest_bidder[1]}")

print(f"The final standings are {sorted_bids}")
   








