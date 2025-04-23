#!/usr/bin/env python3
# coding: utf-8

"""
Extended Address Book Program

This script extends the previous simple address book implementation by adding data persistence and input validation.
The program now supports saving the address book to and loading it from a CSV file. This ensures that entries are
retained between sessions. Additionally, it includes validation for email addresses and phone numbers to ensure that
entries are correctly formatted.

Enhancements over the previous version:
- Data Persistence: Entries are saved to 'address_book.csv', allowing them to persist between program runs.
- Input Validation: Email addresses and phone numbers are validated using regular expressions.
"""

import csv
import os
import re
import sys

# Constants for menu options
ADD_ENTRY = 1
REMOVE_ENTRY = 2
LIST_ENTRIES = 3
SHOW_ENTRY = 4
CLEAR_ENTRIES = 5
EXIT = 6

address_book = []  # List to store address book entries

def num_input(prompt: str) -> int:
    """Prompt the user for a numeric input."""
    while True:
        try:
            return int(input(prompt))  # Convert input to an integer
        except ValueError:
            print("Please enter a valid number.")

def add_entry(name, phone, email):
    """Add a new entry to the address book."""
    if not validate_email(email):
        print("Invalid email format. Entry not added.")
        return
    if not validate_phone(phone):
        print("Invalid phone format. Entry not added.")
        return
    entry = {'name': name, 'phone': phone, 'email': email}
    address_book.append(entry)  # Append the new entry to the address book
    print("Entry successfully added.")

def remove_entry(number):
    """Remove an entry from the address book by its number."""
    if not (1 <= number <= len(address_book)):
        print("Invalid entry number.")
        return
    item = address_book.pop(number - 1)  # Remove and return the entry at the specified index
    print(f"{item['name']} successfully removed.")

def list_entries():
    """List all entries in the address book."""
    for index, entry in enumerate(address_book, start=1):
        print(f"{index} - {entry['name']}")  # Print each entry's index and name

def show_entry(number):
    """Show details of a specific entry in the address book."""
    if not (1 <= number <= len(address_book)):
        print("Invalid entry number.")
        return
    entry = address_book[number - 1]  # Access the entry at the specified index
    print(f"Name: {entry['name']}\nPhone: {entry['phone']}\nEmail: {entry['email']}")

def clear_entries():
    """Clear all entries in the address book."""
    address_book.clear()  # Clear the address book list
    print("All entries successfully cleared.")

def validate_email(email) -> bool:
    """Validate the format of an email address using regular expressions."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None

def validate_phone(phone) -> bool:
    """Validate the format of a phone number using regular expressions."""
    pattern = r"^(?:0[2-8])(\d{8})$"
    return re.match(pattern, phone) is not None

def save_to_csv(filename: str):
    """Save the address book entries to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email'])
        writer.writeheader()  # Write the header to the CSV file
        for entry in address_book:
            writer.writerow(entry)  # Write each entry as a row in the CSV file

def load_from_csv(filename: str):
    """Load address book entries from a CSV file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            address_book.clear()  # Clear existing entries before loading
            address_book.extend(reader)  # Load entries from the CSV file

def show_menu() -> int:
    """Display the main menu options to the user and get their choice."""
    print("\nMenu:")
    print(f"1 - Add entry")
    print(f"2 - Remove entry")
    print(f"3 - List entries")
    print(f"4 - Show entry")
    print(f"5 - Clear entries")
    print(f"6 - Exit\n")
    return num_input("Enter your choice: ")

def main():
    """Main function to run the extended address book program."""
    load_from_csv("address_book.csv")  # Load entries from CSV file at the start

    while True:
        choice = show_menu()  # Get user's choice

        if choice == ADD_ENTRY:
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email address: ")
            add_entry(name, phone, email)

        elif choice == REMOVE_ENTRY:
            if not address_book:
                print("No entries to remove.\n")
                continue
            number = num_input("Enter entry number to remove: ")
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
            number = num_input("Enter entry number to show: ")
            show_entry(number)

        elif choice == CLEAR_ENTRIES:
            clear_entries()

        elif choice == EXIT:
            save_to_csv("address_book.csv")
            print("Address book saved. Exiting program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == '__main__':
    sys.exit(main())
