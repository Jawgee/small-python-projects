import art
import random

def generate_number():
    """
    Generate a random integer between 1 and 100.

    Returns:
        int: number between 1 and 100.
    """
    number = random.randint(1, 100)
    return number

def winning_number(u_num, c_num):
    """
    Discover the winning number.

    Parameters:
        u_num (int): The user's guess.
        c_num (int): The computer's number.

    Returns:
        int: 0 if both numbers match.
        None: if both numbers don't match.
    """
    if u_num == c_num:
        return 0
    return None

def compare_number(u_num, c_num):
    """
    Compare the two numbers.

    Parameters:
        u_num (int): The user's guess.
        c_num (int): The computer's number.

    Returns:
        int: "Too high." if the user's guess is higher than the computer's number.
        int: "Too low." if the user's guess is lower than the computer's number.
        None: if both statements aren't met.

    """
    if u_num > c_num:
        return "Too high."

    if u_num < c_num:
        return "Too low."
    return None

def main():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
    game_over = False

    while not game_over:

        attempts = 0
        c_num = generate_number()
        difficulty_continue = False
        guess_continue = False
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()

        # Attempts are dependent on difficulty levels
        while not difficulty_continue:
            if difficulty == "easy":
                attempts = 10
                difficulty_continue = True
            elif difficulty == "hard":
                attempts = 5
                difficulty_continue = True
            else:
                print("Invalid input. Try again.")
                difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").strip().lower()

        print(f"You have {attempts} attempts remaining to guess the number.")
        attempts -= 1

        while not guess_continue:
            guess = 0

            try:
                guess = int(input("Make a guess: "))
            except ValueError:
                print("Error: That's not a valid integer!")


            winner = winning_number(guess, c_num)

            if attempts > 0 and winner != 0:
                print(compare_number(guess, c_num))
                print(f"You have {attempts} attempts remaining to guess the number.")
                attempts -= 1
            elif winner == 0:
                print(f"You got it! The answer was {c_num}")
                guess_continue = True
            elif attempts == 0:
                print("You've run out of guesses.")
                guess_continue = True

        if input("Do you want to play again? (y/n): ").strip().lower() == "y":
            main()
        else:
            game_over = True

main()
