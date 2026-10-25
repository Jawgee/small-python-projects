import random, hangman_words, hangman_art

lives = 6

# Select a random word to guess from the word list.
print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

# Create the blank characters
placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print("Word to guess: " + placeholder)

game_over = False
correct_letters = []

while not game_over:

    # Tell the user how many lives they have left.
    print(f"****************************{lives}/6 LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()


    display = ""

    # If letter is already guessed, let the user know.
    if guess in correct_letters:
        print(f"You already guessed this letter: {guess}")

    # Update the display: reveal newly guessed letters and keep previously correct ones
    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)


    # If a letter is not correct then a life is lost until game over at 0
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word, you lose a life.")
        lives -= 1

        if lives == 0:
            game_over = True

            print(f"***********************IT WAS {chosen_word} YOU LOSE**********************")

    # Win condition when there are no more underscores in the display string
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")

    print(hangman_art.stages[lives])
