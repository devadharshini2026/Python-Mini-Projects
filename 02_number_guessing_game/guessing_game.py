import random
import os

history_file = "history.txt"

def save_history(entry):
    with open(history_file, "a") as f:
        f.write(entry + "\n")

def show_history():
    if os.path.exists(history_file):
        print("\n=== Game History ===")
        with open(history_file, "r") as f:
            print(f.read())
    else:
        print("\nNo history available.")

def guessing_game():
    print("=== Number Guessing Game ===")
    print("Guess the number between 1 and 100")
    print("Type 'history' to see past attempts or 'exit' to quit.\n")

    while True:
        secret_number = random.randint(1, 100)
        attempts = 0

        while True:
            guess = input("Enter your guess: ").strip()

            if guess.lower() == "exit":
                print("Exiting the game. Goodbye!")
                return
            elif guess.lower() == "history":
                show_history()
                continue

            try:
                guess = int(guess)
            except ValueError:
                print("Invalid input! Enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed it in {attempts} attempts.")
                save_history(f"Guessed {secret_number} in {attempts} attempts")
                break

        play_again = input("Play again? (y/n): ").strip().lower()
        if play_again != "y":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    guessing_game()
