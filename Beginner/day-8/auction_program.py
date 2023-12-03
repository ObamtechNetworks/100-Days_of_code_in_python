from os import system
from art import logo
import sys
#HINT: You can call clear() to clear the output in the console.
# os.clear()


def highest_bidder(bidding_data):
    # get max bidder
    
    max_bidder = max(bidding_data, key=bidding_data.get)
    max_bid = bidding_data[max_bidder]
    # going the crude way
    '''
    max_bidder = None
    max_bid = -1
    
    for key, value in bidding_data.items():
        if value > max_bid:
            max_bid = value
            max_bidder = key
    '''
    return [max_bidder, max_bid]

# print logo
print(logo)
bidding_info = {}
game_play = True
while game_play:
    print("Welcome to the secret auction program.")
    user_name = input ("What is your name?: ")
    try:
    	bid_value = int(input ("What's your bid?: $"))
    except Exception:
        print("Bid value must be a number")
        sys.exit(1)
    other_bidders = input("Are there any other bidders? Type 'yes' or 'no'.")
    # store data into dictionary
    bidding_info[user_name] = bid_value
    
    if other_bidders == 'no':
        # call function here
        max_bidder = highest_bidder(bidding_info)
        print(f"The winner is {max_bidder[0]} with a bid of ${max_bidder[1]}")
        print(bidding_info)
        game_play = False
    elif other_bidders == 'yes':
        system('clear')
        game_play = True
    else:
        print("Incorrect input, goodbye...")
        game_play = False
