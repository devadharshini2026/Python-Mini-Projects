HISTORY_FILE = "mad_libs_history.txt"

def save_story(story):
    with open(HISTORY_FILE, "a") as f:
        f.write(story + "\n\n")

def main():
    print("=== Mad Libs Generator ===")

    noun = input("Enter a noun: ")
    verb = input("Enter a verb: ")
    adjective = input("Enter an adjective: ")
    place = input("Enter a place: ")

    story = f"One day, a {adjective} {noun} decided to {verb} at the {place}."
    print("\n--- Your Story ---")
    print(story)

    save_story(story)
    print(f"\nYour story has been saved in {HISTORY_FILE}")

if __name__ == "__main__":
    main()
