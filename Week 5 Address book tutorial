# Python Address Book Tutorial

In this task, our goal is to create an in-memory address book in Python with the following basic features:

1. **Add a new entry**: The most important feature of all, we want to be able to add a new contact to the address book with details like name, phone, and email.

2. **Remove an existing entry**: At some point, we want to be able to remove contacts when we no longer need a particular entry.

3. **List all entries**: We want to be able to display all current entries in the address book, showing each entry's index and name.

4. **View a specific entry**: After viewing a list of possible entries, we want to be able to display the specific details about a contact.

5. **Clear all entries**: We want to be able to delete all entries from the address book (possibly a slightly disastrous option 🙂)

6. **Menu**: We want to be able to select all of the above options (add, remove, list, view details, clear entries) via a main menu, along with an option to gracefully quit the program.

Ideally, all the major functionality of the program should be implemented as Python functions, with the main menu serving as the entry point to call these functions based on user input.

## Broad Design

First, we need to make some decisions about how we're going to store the data about each entry in our address book. Because we will need to handle an arbitrary number of contacts, we won't be able to create individual variables for each one. Instead, we need to utilise Python's various collection types, such as lists or dictionaries, to store the contact information efficiently. We will need:

1. A structure to serve as the overall container that holds all users in the list.

2. A structure that will hold the details about each individual contact.

Because the number of users can grow indefinitely, the choice that makes the most logical sense for the overall container [is a list](https://realpython.com/python-list/): an ordered collection that we can append items to as needed, and remove items via their index.

To store data about each **individual contact**, we *could* use another list or [a tuple](https://realpython.com/python-lists-tuples/) like this:

```python
contact = ["Ada Lovelace", "alovelace@byron.co.uk", "0418345678"]
print(contact[1]) # Print the email address
```

but we'd have to remember the particular order of each of the details, and it would be difficult to change if we wanted to modify the order later. Not only that, but it's not immediately obvious in our code what an index like `1` or `2` refers to.

Instead, the logical option here is to [use a dictionary](https://realpython.com/python-dicts/), which will allow us to store and retrieve contact details by a key instead of an index:

```python
contact = {"name": "Ada Lovelace", "email": "alovelace@byron.co.uk", "phone": "0418345678"}
print(contact["email"]) # Print the email address
```

Not only is this clearer to read, but we can add or remove an arbitrary number of details as we like, regardless of the order in which they are stored. 

Putting it together, this means our contacts database will be a list of dictionaries like this:

```python
contacts = [
    {"name": "Alan Turing", "email": "aturing@bletchleypark.co.uk"},
    {"name": "Grace Hopper", "email": "ghopper@yale.edu", "phone": "0418234567"},
    {"name": "Ada Lovelace", "email": "alovelace@byron.co.uk", "phone": "0418345678"},
]
```

This will allow us to fetch a particular entry via its index when the user chooses it from a list of available contacts, and we can fetch individual contact details with a descriptive key.

## Writing the Functions

Now that we know how we're going to store our address book entries, we can start working on the functions we'll need to provide each element of functionality in our program.

### The `num_input()` Helper Function

Before we start writing the main functions, we're going to define a little [helper function](https://www.geeksforgeeks.org/what-are-the-helper-functions/) for obtaining numeric input from the user.

In our address book program, we often need to prompt the user for numeric input, such as when they're choosing a menu option or specifying an entry to remove or display. We could just use `input()` each time, but then we'd have to handle the possibility of the user entering invalid input (like a letter instead of a number) every time.

To make our code more DRY (**D**on't **R**epeat **Y**ourself), we can create a helper function to handle this for us:

```python
def num_input(prompt: str) -> int:
    """Prompt the user for a numeric input."""
    while True:
        try:
            return int(input(prompt))  # Convert input to an integer
        except ValueError:
            print("Please enter a valid number.")
```

This function takes a `prompt` string as a parameter, which is the message we want to display to the user when asking for input.

Inside the function, we start an infinite loop with `while True`. This loop will keep running until we explicitly break out of it with a `return` statement.

Inside the loop, we use a `try...except` block to attempt to convert the user's input to an integer with `int(input(prompt))`. If the user enters something that can be converted to an integer (like `"42"`), this will succeed and the function will `return` that integer, breaking out of the loop.

If the user enters something that can't be converted to an integer (like `"hello"`), `int()` will raise a `ValueError`. In this case, the `except` block will catch this exception, print an error message to the user, and the loop will start again from the beginning, prompting the user for input again.

By encapsulating this logic in a helper function, we can simply call `num_input()` whenever we need to get a numeric input from the user, without worrying about handling invalid input each time.

For example, in our `main()` function, we use `num_input()` to get the user's menu choice:

```python
choice = num_input("Enter your choice: ")
```

And in `remove_entry()` and `show_entry()`, we use it to get the entry number from the user:

```python
number = num_input("Enter entry number: ")
```

This makes our code more readable and less repetitive. Whenever you find yourself writing the same or very similar code multiple times, always consider if you can refactor it into a reusable function! Helper functions like the one above let you break your code down into smaller, more manageable and reusable pieces. As your programs get more complex, this becomes increasingly important for keeping your code organised and maintainable.

If you're new to Python's `try...except` error handling, you might find these resources helpful:

* [Exception Handling in Python](https://diveintopython.org/learn/exceptions)
* [Python Try Except](https://www.w3schools.com/python/python_try_except.asp)

### Adding a New Entry

To add a new entry to our address book, we need to create an `add_entry()` function. This function will take the contact details as parameters, create a new dictionary representing the contact, and append it to our `contacts` list.

```python
def add_entry(name: str, phone: str, email: str) -> None:
    """Add a new entry to the address book."""
    entry = {
        'name': name,
        'phone': phone,
        'email': email
    }
    address_book.append(entry)  # Append the new entry to the address book
    print("Entry successfully added.")
```

Here, we're using Python's [type hints](https://docs.python.org/3/library/typing.html) to specify the expected types of the function's parameters and return value. This is optional but can make our code more readable and catch potential errors early.

The `entry` dictionary is constructed using the provided `name`, `phone`, and `email` values. We then use the `append()` method to add this new dictionary to the end of our `address_book` list.

### Removing an Entry

Next, let's write a function to remove an entry from the address book. We'll assume the user will input the number of the entry they want to remove (which we'll display when listing the entries).

```python
def remove_entry(number: int) -> None:
    """Remove an entry from the address book by its number."""
    if not (1 <= number <= len(address_book)):
        print("Invalid entry number.")
        return

    item = address_book.pop(number - 1)  # Remove and return the entry at the specified index
    print(f"{item['name']} successfully removed.")
```

First, we check if the provided `number` is within the valid range (from 1 to the length of the `address_book` list). If it's not, we print an error message and `return` early.

If the number is valid, we use the `pop()` method to remove the entry at the specified index. Note that we subtract 1 from `number` because list indices start at 0, but we'll display entry numbers starting from 1 to the user.

The `pop()` method removes and returns the item at the given index, so we can use that to print a confirmation message including the removed contact's name.

### Listing All Entries

To list all entries, we'll iterate over the `address_book` list and print each entry's number and name.

```python
def list_entries() -> None:
    """List all entries in the address book."""
    for index, entry in enumerate(address_book, start=1):
        print(f"{index} - {entry['name']}")  # Print each entry's index and name
```

Here, we use [the `enumerate()` function](https://www.programiz.com/python-programming/methods/built-in/enumerate) to get both the index and the value of each item as we loop over the `address_book` list. By passing `start=1`, we make the numbering start from 1 instead of the default 0.

For each entry, we print the index and the 'name' value from the dictionary.

### Showing a Specific Entry

When the user wants to see the details of a specific entry, we'll prompt them for the entry number and display all the stored details for that contact.

```python
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
```

Similar to `remove_entry()`, we first check if the provided `number` is within the valid range and return early if it's not.

If the number is valid, we fetch the corresponding entry from the `address_book` list (remembering to subtract 1 from `number` to get the correct index).

We then print out each detail of the entry, accessing the values by their keys in the dictionary.

### Clearing All Entries

Sometimes we might want to clear out the entire address book. Here's a function to do that:

```python
def clear_entries() -> None:
    """Clear all entries in the address book."""
    address_book.clear()  # Clear the address book list
    print("All entries successfully cleared.")
```

This one's quite straightforward. We just use the `clear()` method to remove all items from the `address_book` list, and inform the user that the address book has been successfully cleared.

### Defining Menu Constants

Before we move onto the `show_menu()` and `main()` functions, let's take a look at the constants we define at the start of our code:

```python
ADD_ENTRY = 1
REMOVE_ENTRY = 2
LIST_ENTRIES = 3
SHOW_ENTRY = 4
CLEAR_ENTRIES = 5
EXIT = 6
```

These are integer constants that we use to represent the different menu options. But why define these constants instead of just using the numbers directly in our code? There are several reasons:

1. **Readability**: Using named constants makes our code more readable. When we see `ADD_ENTRY` in our code, it's immediately clear what it represents. If we just used `1`, it would be less obvious what that `1` means in the context of our program.

2. **Maintainability**: If we decide to change the order of our menu options or add/remove options, we only need to change these constants. If we used numbers directly in our code, we'd have to find and replace every occurrence of the number we want to change.

3. **Reduces Errors**: Using constants reduces the chance of errors in our code. If we mistype a number in our code, it might not be immediately obvious and could lead to bugs. But if we mistype a constant name, Python will immediately throw a `NameError`, making it easy to spot and fix the mistake.

4. **Consistency**: By defining these constants in one place, we ensure that we're using the same value for each menu option throughout our code. If we used numbers directly and accidentally used `4` instead of `5` in one place, it could lead to hard-to-find bugs.

In Python, constants are usually defined in all caps with underscores separating words (this is just a convention, not a rule enforced by Python).

We use these constants in our `main()` function to check the user's choice and decide what action to take:

```python
if choice == ADD_ENTRY:
    # Code to add an entry
elif choice == REMOVE_ENTRY:
    # Code to remove an entry
elif choice == LIST_ENTRIES:
    # Code to list entries
# ... and so on
```

This makes our code more readable and less prone to errors than if we had used numbers directly:

```python
if choice == 1:
    # Code to add an entry
elif choice == 2:
    # Code to remove an entry
elif choice == 3:
    # Code to list entries
# ... and so on
```

Defining and using constants is a good programming practice that makes your code more readable, maintainable, and less error-prone. It's especially useful when you have a set of related values that are used throughout your code, like our menu options here.

## Putting It All Together

Now that we've covered defining constants, let's move on to tying everything together with our `show_menu()` and `main()` functions.

The `show_menu()` function displays the available options and prompts the user to enter their choice. It uses our `num_input()` helper function to get a numeric input from the user:

```python
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
```

Finally, our `main()` function serves as the entry point for our program. It runs in an infinite loop, repeatedly prompting the user for their choice until they choose to exit:

```python
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
```

In the `main()` function, we use our menu constants to check the user's choice and decide what action to take. This is where defining those constants really pays off - our code is much more readable than if we had used numbers directly.

Before calling `remove_entry()`, `list_entries()`, or `show_entry()`, we check if the `address_book` list is empty and display a message if it is. This not only prevents errors that would occur if we tried to remove or display entries from an empty list, but also provides information to the user about the state of their address book.

If the user chooses to add a new entry, we prompt for the necessary details and pass them to our `add_entry()` function.

The program keeps running until the user chooses the `EXIT` option, at which point we `break` out of the infinite loop and the program ends.

And that's it. A complete, if somewhat limited, address book program in Python. At this stage, the major limitation is that we will lose all our entries when the program exits. We will address that problem in the next task, where we implement data persistence.
