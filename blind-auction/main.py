import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)

def find_highest_bidder(bidders_dictionary):
    max_bid = 0
    winner = ""

    # find the highest bidder based on the highest bid amount
    for key in bidders_dictionary:
        if bidders_dictionary[key] > max_bid:
            max_bid = bidders_dictionary[key]
            winner = key

    print(f"The winner is {winner} with a bid of ${max_bid}.")

bidders = {}
game_over = False

while not game_over:
    # Ask for bidders participating until there are no more new bidders
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    bidders[name] = bid

    go_again = input("Are there any other bidders? Type 'yes' or 'no'.\n ").lower()

    if go_again == "no":
        find_highest_bidder(bidders)
        game_over = True
    else:
        print("\n" * 100)  # clear the terminal rudimentally for some privacy




