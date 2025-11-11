import random

words_with_clues = {
    "python": "A popular programming language known for its simplicity.",
    "hangman": "The name of the game you are playing right now!",
    "computer": "An electronic device used for processing information.",
    "science": "The study of the natural world through experiments.",
    "program": "A set of instructions that tells a computer what to do."
}

print("Welcome to Hangman!")
print("Guess the word, one letter at a time.")
print("You have 6 incorrect guesses per round.\n")

play_again = "yes"

while play_again.lower() == "yes":
    word_to_guess, clue = random.choice(list(words_with_clues.items()))
    guessed_letters = []
    wrong_guesses = 0
    max_guesses = 6
    display_word = ["_"] * len(word_to_guess)

    print(f"\nNew Round! Clue: {clue}")

    while wrong_guesses < max_guesses and "_" in display_word:
        print("\nWord:", " ".join(display_word))
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "No guesses yet")
        guess = input("Enter a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Please enter a single alphabetic character.")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in word_to_guess:
            print("✅ Correct guess!")
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess:
                    display_word[i] = guess
        else:
            wrong_guesses += 1
            print(f"Wrong guess! You have {max_guesses - wrong_guesses} tries left.")

    if "_" not in display_word:
        print("\nCongratulations! You guessed the word:", word_to_guess)
    else:
        print("\nGame Over! The word was:", word_to_guess)

    play_again = input("\nDo you want to play again? (yes/no): ")

print("\nThanks for playing Hangman! Goodbye!")
