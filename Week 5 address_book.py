#!/usr/bin/env python3
# coding: utf-8

"""
This script implements a simple address book using a list of dictionaries,
where each dictionary represents an individual's contact details. Users can
add, remove, list, show, or clear entries. It's designed to teach basic
programming constructs like functions, lists, dictionaries, and user input handling.

Note: Data isn't persisted across sessions, as the focus is on basic concepts.
Future improvements will include data persistence.
"""

import sys

# Constants for menu options
ADD_ENTRY = 1
REMOVE_ENTRY = 2
LIST_ENTRIES = 3
SHOW_ENTRY = 4
CLEAR_ENTRIES = 5
EXIT = 6

address_book = []  # Initialise an empty list to store address book entries

def num_input(prompt: str) -> int:
    """Prompt the user for a numeric input."""
    while True:
        try:
            return int(input(prompt))  # Convert input to an integer
        except ValueError:
            print("Please enter a valid number.")

def add_entry(name: str, phone: str, email: str) -> None:
    """Add a new entry to the address book."""
    entry = {
        'name': name,
        'phone': phone,
        'email': email
    }
    address_book.append(entry)  # Append the new entry to the address book
    print("Entry successfully added.")

def remove_entry(number: int) -> None:
    """Remove an entry from the address book by its number."""
    if not (1 <= number <= len(address_book)):
        print("Invalid entry number.")
        return


    item = address_book.pop(number - 1)  # Remove and return the entry at the specified index
    print(f"{item['name']} successfully removed.")


def list_entries() -> None:
    """List all entries in the address book."""
    for index, entry in enumerate(address_book, start=1):
        print(f"{index} - {entry['name']}")  # Print each entry's index and name

def show_entry(number: int) -> None:
    """Show details of a specific entry in the address book."""
    if not (1 <= number <= len(address_book)):
        print("Invalid entry number.")
        return

    entry = address_book[number - 1]  # Access the entry at the specified index
    # Print details of the entry
    print()
    print(f"Name: {entry['name']}")
    print(f"Phone: {entry['phone']}")
    print(f"Email: {entry['email']}")

def clear_entries() -> None:
    """Clear all entries in the address book."""
    address_book.clear()  # Clear the address book list
    print("All entries successfully cleared.")

def show_menu() -> None:
    """Display the main menu options to the user."""
    print("1 - Add entry")
    print("2 - Remove entry")
    print("3 - List entries")
    print("4 - Show entry")
    print("5 - Clear entries")
    print("6 - Exit\n")

    choice = num_input("Enter your choice: ")
    return choice

def main() -> None:
    """Main function to run the address book program."""
    while True:
        choice = show_menu()  # Prompt for user's choice

        # Handle user's choice
        if choice == ADD_ENTRY:
            # Prompt for new entry details
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_entry(name, phone, email)

        elif choice == REMOVE_ENTRY:
            if not address_book:
                print("No entries to remove.\n")
                continue

            number = num_input("Enter entry number: ")
            remove_entry(number)

        elif choice == LIST_ENTRIES:
            if not address_book:
                print("Address book is empty.\n")
                continue

            list_entries()

        elif choice == SHOW_ENTRY:
            if not address_book:
                print("No entries to show.\n")
                continue

            number = num_input("Enter entry number: ")
            show_entry(number)

        elif choice == CLEAR_ENTRIES:
            clear_entries()

        elif choice == EXIT:
            break  # Exit the program
        else:
            print("Please enter a number between 1 and 6.")  # Handle invalid choice

        print()

# Run the main function if the script is executed directly
if __name__ == '__main__':
    sys.exit(main())
