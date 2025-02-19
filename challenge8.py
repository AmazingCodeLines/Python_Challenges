""" 
Challenge 8: Silent Auction Program 🏆

Create a Python program that simulates a simple auction system. The program should:

Continuously prompt users to enter:
Their name.
Their bid amount.
Store each bid in a dictionary where the bidder's name is the key and the bid amount is the value.
After each bid, ask if there are additional bidders:
If yes, continue collecting bids.
If no, stop the bidding process.
Define a function that:
Sorts the bids in descending order based on the bid amount.
Identifies and returns the highest bidder along with the full list of sorted bids.
Display:
The name and bid amount of the highest bidder.
The final standings of all bidders sorted by their bid amounts
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
   








