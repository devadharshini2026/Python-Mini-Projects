import random

WORDS = ["python", "developer", "hangman", "programming", "github", "algorithm"]

HISTORY_FILE = "hangman_history.txt"

def save_history(word, attempts, won):
    with open(HISTORY_FILE, "a") as f:
        status = "Won" if won else "Lost"
        f.write(f"{word} - Attempts: {attempts}, Result: {status}\n")

def display_word(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def hangman_game():
    word = random.choice(WORDS)
    guessed_letters = set()
    attempts = 6
    won = False

    print("=== Hangman Game ===")
    print(f"Word has {len(word)} letters. You have {attempts} wrong attempts.\n")

    while attempts > 0:
        print(display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Enter a single letter!")
            continue

        if guess in guessed_letters:
            print("You already guessed that letter!")
            continue

        guessed_letters.add(guess)

        if guess not in word:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")

        if all(letter in guessed_letters for letter in word):
            won = True
            print(f"🎉 You guessed it! The word was '{word}'")
            break

    if not won:
        print(f"Game Over! The word was '{word}'")

    save_history(word, 6 - attempts, won)

if __name__ == "__main__":
    hangman_game()
