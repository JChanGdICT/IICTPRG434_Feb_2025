#!/usr/bin/env python3
# coding: utf-8

"""
Python ATM Simulator

This script simulates basic operations of an Automated Teller Machine (ATM). It allows a user to log in using a PIN,
check their balance, make deposits, and withdraw money. The script demonstrates the use of functions, loops,
conditionals, and exception handling in Python.
"""

import getpass  # Import getpass module for hiding PIN input
import sys

# Define global variables for account name, balance, and pin. Note that we are
# using global variables here for simplicity, but this is generally not a good
# practice.

account_name = "Alan Turing"
balance = 0.0
pin = "1337"

def make_deposit(amount: float) -> None:
    """Function to handle deposit transactions."""
    global balance  # Declare global variable 'balance' to modify it
    balance += amount  # Update balance
    print(f"\nBalance for {account_name}: ${balance}\n")  # Display updated balance

def make_withdrawal(amount: float) -> None:
    """Function to handle withdrawal transactions."""
    global balance  # Declare global variable 'balance' to modify it
    if amount > balance:
        print("Insufficient funds.")  # Check for sufficient balance
    else:
        balance -= amount  # Update balance
        print(f"\nBalance for {account_name}: ${balance}\n")  # Display updated balance

def show_balance() -> None:
    """Function to display the current balance."""
    print(f"\nBalance for {account_name}: ${balance}\n")

def login() -> bool:
    """Function to handle user login. Returns True if login is successful, False otherwise."""
    entry = get_pin()  # Get user-entered PIN
    if entry.strip() == pin:
        print(f"\nWelcome, {account_name}!\n")  # Check if PIN matches and welcome user
        return True
    else:
        return False  # Return False if PIN does not match

def get_pin() -> str:
    """Function to securely get the user's PIN."""
    while True:
        entry = getpass.getpass("Please enter your PIN: ")  # Prompt for PIN without echoing
        if entry.isdigit() and len(entry) == 4:
            return entry  # Return valid PIN
        else:
            print("Please enter a 4-digit PIN.")  # Prompt for valid PIN format

def show_menu() -> int:
    """Function to display the main menu and get user's choice."""
    print("1) Check Balance")
    print("2) Make a Deposit")
    print("3) Make a Withdrawal")
    print("4) Exit")

    while True:
        choice = input("What would you like to do? ")  # Get user's choice
        if choice.isdigit() and 1 <= int(choice) <= 4:
            return int(choice)  # Return valid choice
        else:
            print("Please enter 1, 2, 3, or 4.")  # Prompt for valid choice

def main() -> None:
    """Main function to run the ATM program."""
    print("Welcome to the Python ATM!\n")

    # Login loop
    while True:
        if login():
            break  # Break loop if login successful
        else:
            print("Invalid PIN. Please try again.")  # Prompt for valid PIN

    # Main operation loop
    while True:
        choice = show_menu()  # Show main menu, and get user's choice
        if choice == 1:
            show_balance()  # Display balance
        elif choice == 2:
            try:
                amount = float(input("How much would you like to deposit? "))  # Get deposit amount
                make_deposit(amount)  # Handle deposit
            except ValueError:
                print("Please enter a valid number.")
        elif choice == 3:
            try:
                amount = float(input("How much would you like to withdraw? "))  # Get withdrawal amount
                make_withdrawal(amount)  # Handle withdrawal
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Thank you for using the Python ATM!")  # Exit message
            break  # Break loop to exit

# Run the main function if the script is executed directly
if __name__ == "__main__":
    sys.exit(main())
