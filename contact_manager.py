# contact_manager.py

class DuplicateContactError(Exception):
    """Custom exception when a duplicate contact is attempted to be added."""
    def __init__(self, message="Duplicate contact detected."):
        self.message = message
        super().__init__(self.message)

contacts = {}

def add_contact(name, phone):

    if name in contacts:
        raise DuplicateContactError(f"Contact '{name}' already found in contacts.")
    else:
        contacts[name] = phone
        print(f"Added {name} to contacts.")

def find_contact(name):
    return contacts[name]


def delete_contact(name):
    del contacts[name]
    print(f"Deleted {name}.")


def main():
    while True:
        print("\n--- Contact Manager ---")
        print("1. Add Contact")
        print("2. Find Contact")
        print("3. Delete Contact")
        print("4. Exit")
        choice = input("Enter your choice: ")
        while True:
            try:
                number = int(choice)
                break
            except ValueError:
                print("Please enter whole number from 1-4.")
    
        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            try:
                add_contact(name, phone)
            except DuplicateContactError as e:
                print("Error:", e)
                pass
        elif choice == '2':
            name = input("Enter name to find: ").strip()
            """try/except block for searching non-existing contact"""
            try:
                find_contact(name)
                print(phone)
                pass
            except KeyError:
                print(f"\nContact not found.")
                pass
        elif choice == '3':
            name = input("Enter name to delete: ")
            """try/except block for deleting non-existing contact"""
            try:
                delete_contact(name)
                pass
            except KeyError:
                print(f"\nContact not found.")
                pass
        elif choice == '4':
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()