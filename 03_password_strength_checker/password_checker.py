def check_strength(pwd):
    strength = "Weak"
    criteria = {
        "Minimum 8 characters": len(pwd) >= 8,
        "Lowercase letter": any(c.islower() for c in pwd),
        "Uppercase letter": any(c.isupper() for c in pwd),
        "Digit": any(c.isdigit() for c in pwd),
        "Special character": any(not c.isalnum() for c in pwd)
    }

    score = sum(criteria.values())
    if score >= 4:
        strength = "Strong"
    elif score == 3:
        strength = "Medium"

    return strength, criteria

def password_checker():
    print("=== Password Strength Checker ===")
    print("Type 'exit' to quit.\n")

    while True:
        pwd = input("Enter password: ")
        if pwd.lower() == "exit":
            break

        strength, criteria = check_strength(pwd)
        print(f"\nPassword Strength: {strength}")
        print("Criteria Check:")
        for c, passed in criteria.items():
            print("✓" if passed else "✗", c)
        print()

if __name__ == "__main__":
    password_checker()
