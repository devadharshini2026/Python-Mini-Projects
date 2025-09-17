import time

def countdown_timer(seconds):
    print(f"\nCountdown started for {seconds} seconds!\n")
    while seconds > 0:
        mins, secs = divmod(seconds, 60)
        timer = f"{mins:02d}:{secs:02d}"
        print(timer, end="\r")
        time.sleep(1)
        seconds -= 1
    print("⏰ Time's up!\n")

def main():
    print("=== Countdown Timer ===")
    while True:
        try:
            user_input = input("Enter time in seconds (or 'exit' to quit): ")
            if user_input.lower() == "exit":
                break
            seconds = int(user_input)
            countdown_timer(seconds)
        except ValueError:
            print("Please enter a valid integer.\n")

    input("Press Enter to exit...")

if __name__ == "__main__":
    main()
