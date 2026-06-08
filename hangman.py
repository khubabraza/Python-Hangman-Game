import random


def display_word(secret_word, guessed_letters):
    displayed = ""

    for letter in secret_word:
        if letter in guessed_letters:
            displayed += letter + " "
        else:
            displayed += "_ "

    return displayed.strip()


def play_hangman():
    words = ["python", "flask", "developer", "coding", "programming"]
    secret_word = random.choice(words)

    guessed_letters = []
    incorrect_guesses = 0
    max_attempts = 6

    print("Welcome to the Python Hangman Game!")
    print("Guess the word one letter at a time.")
    print(f"You have {max_attempts} incorrect guesses allowed.\n")

    while incorrect_guesses < max_attempts:
        print("Word:", display_word(secret_word, guessed_letters))
        print(f"Incorrect guesses left: {max_attempts - incorrect_guesses}")
        print("Guessed letters:", ", ".join(guessed_letters) if guessed_letters else "None")

        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter only one alphabetic letter.\n")
            continue

        if guess in guessed_letters:
            print("You already guessed this letter. Try another one.\n")
            continue

        guessed_letters.append(guess)

        if guess in secret_word:
            print("Good guess!\n")
        else:
            incorrect_guesses += 1
            print("Wrong guess!\n")

        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break
    else:
        print("Game Over! The correct word was:", secret_word)


if __name__ == "__main__":
    play_hangman()
