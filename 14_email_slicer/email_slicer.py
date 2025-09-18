def email_slicer(email):
    """Function to split email into username and domain"""
    try:
        username, domain = email.split("@")
        return username, domain
    except ValueError:
        return None, None


def save_to_file(email, username, domain, filename="sliced_emails.txt"):
    """Save the sliced email info into a file"""
    with open(filename, "a") as file:
        file.write(f"Email: {email}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Domain: {domain}\n")
        file.write("-" * 30 + "\n")


def main():
    print("=== Email Slicer ===")
    email = input("Enter your email address: ").strip()

    username, domain = email_slicer(email)

    if username and domain:
        print(f"\nUsername: {username}")
        print(f"Domain  : {domain}")

        save_to_file(email, username, domain)
        print("\n✅ Details saved to 'sliced_emails.txt'")
    else:
        print("\n❌ Invalid email format. Please try again.")


if __name__ == "__main__":
    main()
