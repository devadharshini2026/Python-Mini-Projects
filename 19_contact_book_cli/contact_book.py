import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ").strip()
    email = input("Enter email: ").strip()

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!\n")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n📒 Contact List:")
    for name, info in contacts.items():
        print(f"- {name}: {info['phone']}, {info['email']}")
    print()

def search_contact(contacts):
    name = input("Enter name to search: ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"🔍 {name} → {info['phone']}, {info['email']}\n")
    else:
        print(f"❌ Contact '{name}' not found.\n")

# Delete contact
def delete_contact(contacts):
    name = input("Enter name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"🗑️ Contact '{name}' deleted.\n")
    else:
        print(f"❌ Contact '{name}' not found.\n")

# Main CLI loop
def contact_book():
    contacts = load_contacts()
    while True:
        print("📘 Contact Book CLI")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print(
