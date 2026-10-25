import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    dealt_card = random.choice(cards)
    return dealt_card

def calculate_score(cards):
    """
    Take a list of cards and calculate the score.

    Parameters:
        cards (list): List of cards either from the user or computer.

    Returns:
        int: the sum of all the card values.
        int: 0 if blackjack is obtained.
    """
    if sum(cards) == 21 and len(cards) == 2:
        return 0

    if 11 in cards and sum(cards) > 21:  # Aces become the value of 1 if the sum of the cards is greater than 21
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare_score(user_score, computer_score):
    """
    Compare the scores between both user and computer.

    Parameters:
        user_score (int): The total score of the user's hand.
        computer_score (int): The total score of the computer's hand.

    Returns:
        str: if user_score and computer_score are equal, return "Push!"
        str: If computer_score is equal to 0, return "Dealer got blackjack. You lose!"
        str: If user_score is equal to 0, return "You got blackjack. You win!"
        str: If user_score is greater than 21, return "You busted. You lose!"
        str: If computer_score is greater than 21, return "Dealer busted. You win!"
        str: If user_score is greater than computer_score, return "You win!"
        str: If computer_score is greater than user_score, return "You lose!"
    """
    if user_score == computer_score:
        return "Push!"
    elif computer_score == 0:
        return "Dealer got blackjack. You lose!"
    elif user_score == 0:
        return "You got blackjack. You win!"
    elif user_score > 21:
        return "You busted. You lose!"
    elif computer_score > 21:
        return "Dealer busted. You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"

def play_game():
    print(art.logo)
    u_cards = []
    c_cards = []
    u_score = -1
    c_score = -1
    game_over = False

    # Deal 2 cards for the user and computer
    for i in range(2):
        u_cards.append(deal_card())
        c_cards.append(deal_card())

    while not game_over:
        u_score = calculate_score(u_cards)
        c_score = calculate_score(c_cards)
        print(f"Your cards: {u_cards}, current score: {u_score}")
        print(f"Computer's first card: {c_cards[0]}")

        if u_score == 0 or c_score == 0 or u_score > 21:  # When the user or computer gets blackjack or the user gets more than 21, the loop is broken
            game_over = True
        else:
            user_continue = input("Type 'y' to hit or type 'n' to stand: ")
            if user_continue == "y":
                u_cards.append(deal_card())
            else:
                game_over = True

    # The computer keeps drawing until their score is 17 or higher
    while c_score != 0 and c_score < 17:
        c_cards.append(deal_card())
        c_score = calculate_score(c_cards)

    print(f"Your final hand: {u_cards}, final score: {u_score}")
    print(f"Computer's final hand: {c_cards}, final score: {c_score}")
    print(compare_score(u_score, c_score))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()