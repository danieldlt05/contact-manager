# Contact Manager
This Contact Manager program allows users to add, find, and delete contacts stored in a dictionary.
It also uses a custom exception to prevent duplicate entries from being added.

## Features
- Add a new contact with a name and phone number
- Search for existing contacts
- Delete contacts
- Raise a custom DuplicateContactError if a name already exists
- Gracefully handle missing contacts using try/except blocks
- Includes automated unit tests usig the built-in unittest module

## How It Works
1. add_conntact(name, phone)
  - Adds a contact to the dictionary.
  - Raises DuplicateContactError if the name already exists.
2. find_contact(name)
  - Returns the contact's phone number if found.
  - Raises KeyError if the name doesn't exist.
3. delete_contact(name)
  - Removes the contact from the dictionary.
  - Raises KeyError if the contact doesn't exist.
4. DuplicateContactError
  - A custom exception class used to handle duplicates in the contact list.
5. Main Program Loop
  - Displays a menu with 4 options: Add, Find, Delete, and Exit.
  - Continues running until the user selects "Exit".

## How to Run
1. Open a terminal and navigate to the folder containing your files.
2. Run the main program:
  python contact_manager.py
3. Follow the menu prompts to manage contacts.

## How to Run Tests
This project includes a test file named test_contact_manager.py
To run all unit tests:
  python -m unittest test_contact_manager.py

## Where to Watch Explanation
https://youtu.be/T44gurOqjLY