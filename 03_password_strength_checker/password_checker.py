import re
import os

history_file = "history.txt"

def save_history(entry):
    with open(history_file, "a") as f:
        f.write(entry + "\n")

def show_history():
    if os.path.exists(history_file):
        print("\n=== Password Check History ===")
        with open(history_file, "r") as f:
            print(f.read())
    else:
        print("\nNo history available.")

def check_password_strength(password):
    strength = 0
    criteria = []

    if len(password) >= 8:
        strength += 1
        criteria.append("✓ Minimum 8 characters")
    else:
        criteria.append("✗ Minimum 8 characters")

    if re.search(r"[a-z]", password):
        strength += 1
        criteria.append("✓ Lowercase letter present")
    else:
        criteria.append("✗ Lowercase letter missing")

    if re.search(r"[A-Z]", password):
        strength += 1
        criteria.append("✓ Uppercase letter present")
    else:
        criteria.append("✗ Uppercase letter missing")

    if re.search(r"\d", password):
        strength += 1
        criteria.append("✓ Digit present")
    else:
        criteria.append("✗ Digit missing")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
        criteria.append("✓ Special character present")
    else:
        criteria.append("✗ Special character missing")

    if strength <= 2:
        overall = "Weak"
    elif strength == 3 or strength == 4:
        overall = "Moderate"
    else:
        overall = "Strong"

    return overall, criteria

def password_checker():
    print("=== Password Strength Checker ===")
    print("Type 'history' to see past checks or 'exit' to quit.\n")

    while True:
        pwd = input("Enter password: ").strip()

        if pwd.lower() == "exit":
            print("Exiting password checker. Goodbye!")
            break
        elif pwd.lower() == "history":
            show_history()
            continue

        strength, criteria = check_password_strength(pwd)
        print("\nPassword Strength:", strength)
        print("Criteria Check:")
        for c in criteria:
            print(c)

        save_history(f"{pwd} → {strength}")

if __name__ == "__main__":
    password_checker()
