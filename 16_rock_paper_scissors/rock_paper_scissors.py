import random

def play_round(user_choice):
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)

    print(f"\n🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")

    if user_choice == computer_choice:
        return "It's a Tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "🎉 You Win!"
    else:
        return "😢 You Lose!"

def game():
    print("🎮 Rock-Paper-Scissors Game 🎮")
    print("Type 'exit' to quit.\n")

    while True:
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        if user_choice == "exit":
            print("👋 Thanks for playing!")
            break
        elif user_choice not in ["rock", "paper", "scissors"]:
            print("❌ Invalid choice. Try again.")
        else:
            result = play_round(user_choice)
            print(result)

if __name__ == "__main__":
    game()
