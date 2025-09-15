import json
import os
CONTACTS_FILE = "contacts.json"

def load_contacts():
    """Load contacts from JSON file."""
    if not os.path.exists(CONTACTS_FILE):
        return []
    with open(CONTACTS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_contacts(contacts):
    """Save contacts into JSON file."""
    with open(CONTACTS_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)


def add_contact():
    """Add a new contact."""
    name = input("Enter name: ").strip()
    phone = input("Enter phone: ").strip()
    email = input("Enter email: ").strip()

    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!")


def view_contacts():
    """View all saved contacts."""
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    print("\n=== Contact List ===")
    for i, c in enumerate(contacts, 1):
        print(f"{i}. {c['name']} | {c['phone']} | {c['email']}")


def search_contact():
    """Search for a contact by name."""
    name = input("Enter name to search: ").strip().lower()
    contacts = load_contacts()
    results = [c for c in contacts if name in c['name'].lower()]

    if not results:
        print("No contacts found.")
    else:
        print("\n=== Search Results ===")
        for c in results:
            print(f"{c['name']} | {c['phone']} | {c['email']}")


def delete_contact():
    """Delete a contact by name."""
    name = input("Enter name to delete: ").strip().lower()
    contacts = load_contacts()
    updated = [c for c in contacts if c['name'].lower() != name]

    if len(updated) == len(contacts):
        print("❌ Contact not found.")
    else:
        save_contacts(updated)
        print(f"🗑️ Contact '{name}' deleted successfully!")


def menu():
    """Main menu loop for the contact book."""
    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.")


if __name__ == "__main__":
    menu()
