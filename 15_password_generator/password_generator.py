import random
import string

def generate_password(length=12, use_digits=True, use_specials=True):
    """Generates a random password with given options."""

    # Start with letters
    characters = string.ascii_letters  

    if use_digits:
        characters += string.digits
    if use_specials:
        characters += string.punctuation

    if not characters:
        raise ValueError("No character set selected!")

    # Generate password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password


if __name__ == "__main__":
    print("🔐 Password Generator 🔐")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_digits = input("Include digits? (y/n): ").lower() == "y"
        use_specials = input("Include special characters? (y/n): ").lower() == "y"

        password = generate_password(length, use_digits, use_specials)
        print(f"\nGenerated Password: {password}")
    except ValueError as e:
        print(f"Error: {e}")
