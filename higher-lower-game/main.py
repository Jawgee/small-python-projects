import art
import game_data
import random

def format_data(account):
    """
    Takes in account data and formats it.

    Parameters:
        account (dict): Instagram account data.

    Returns:
        str: Formatted account data.
    """
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}"

def compare_data(user_guess, a_followers, b_followers):
    """
    Takes in user guess and finds out if the user is correct or not.

    Parameters:
        user_guess (str): User guess.
        a_followers (int): Amount of followers in account A.
        b_followers (int): Amount of followers in account B.

    Returns:
        bool: If the user's guess is the same as A or B respectively, then return True else False.
    """
    if a_followers > b_followers:
        return user_guess == "a"
    else:
        return user_guess == "b"

print(art.logo)
account_a = random.choice(game_data.data)
account_b = random.choice(game_data.data)
score = 0
game_over = False

while not game_over:
    print(f"Compare A: {format_data(account_a)}.")
    print(art.vs)
    print(f"Compare B: {format_data(account_b)}.")

    guess = input("Who has more followers? Type 'A' or 'B': ").lower()

    a_followers_count = account_a["follower_count"]
    b_followers_count = account_b["follower_count"]

    is_correct = compare_data(guess, a_followers_count, b_followers_count)

    print("\n" * 20)
    print(art.logo)

    # Account A becomes account B and a new account B is chosen
    if is_correct:
        score += 1
        print(f"You're right! Current score: {score}.")
        account_a = account_b
        account_b = random.choice(game_data.data)
    else:
        print(f"Sorry, that's wrong. Final score: {score}")
        game_over = True