# Extending the Python Address Book

In our previous task we built a simple but functional address book program in Python. We learned how to use lists and dictionaries to store and manage our contacts, and how to interact with the user via a command-line interface.

However, our previous program had a couple of fairly glaring limitations:

1. It didn't persist data between sessions. Every time we started the program, we started with an empty address book.

2. It allowed any input for the email and phone fields, even if they were invalid.

In this task, we're going to address these issues by extending our program with two new features:

1. **Data Persistence**: We'll save our address book to a file when the program exits, and load it back up when the program starts. This way, our contacts will persist between sessions.

2. **Data Validation**: We'll use regular expressions to validate the format of email addresses and phone numbers. This will ensure that the data in our address book is consistent and correct.

## Data Persistence with CSV

One of the key limitations of our previous address book program was that it didn't save the data anywhere. Every time we started the program, we started with an empty address book. If we wanted to keep our contacts, we had to re-enter them every time. That's not very useful for a real-world application, and definitely not what we want in our address book.

To fix this, we need to implement **data persistence**. This means saving our data to a file when we close the program, and loading that data back into the program when we start it up again.

There are many ways we could store our data (such as [XML](https://en.wikipedia.org/wiki/XML), [JSON](https://en.wikipedia.org/wiki/JSON) or [SQLite](https://en.wikipedia.org/wiki/SQLite)), but for this tutorial, we're going to use the [**CSV** (**C**omma-**S**eparated **V**alues)](https://en.wikipedia.org/wiki/Comma-separated_values) format. CSV is a simple, universal data format that can be read by many programs, including spreadsheet applications like Microsoft Excel or Google Sheets.

In a CSV file, each line represents a single data record (in our case, a single contact), and each record consists of one or more fields, separated by commas. The first line of the file usually contains the names of the fields (the headers).

Here's what a CSV file of our address book data might look like:

```csv
name,phone,email
John Doe,1234567890,john@example.com
Jane Doe,9876543210,jane@example.com
```

Python provides a built-in `csv` module that makes it easy to read from and write to CSV files. This module provides two main classes for working with CSV data: `csv.reader` and `csv.writer`. These classes allow you to read and write CSV data as lists of strings.

However, in our program, we're storing our contact data as dictionaries, not lists. Fortunately, the `csv` module also provides two classes specifically for working with dictionaries: `csv.DictReader` and `csv.DictWriter`.

`csv.DictReader` reads a CSV file and returns each row as a dictionary. The keys of the dictionary are taken from the header row of the CSV file. This is perfect for our use case, because we can read each row of the CSV file directly into a dictionary that matches the format of our address book entries.

Similarly, `csv.DictWriter` writes dictionaries to a CSV file. You provide the fieldnames (the keys of your dictionaries) when you create the `DictWriter`, and then you can write each dictionary as a row in the CSV file.

We'll use these classes to implement two new functions in our program: `save_to_csv()`, which will save our address book data to a CSV file, and `load_from_csv()`, which will load our address book data from a CSV file.

We'll call `load_from_csv()` when our program starts up, so that we start with the data from our previous session. And we'll call `save_to_csv()` when our program is about to exit, so that we save any changes we've made.

With these additions, our address book will be truly useful - we'll be able to add, remove, and view contacts, and those changes will persist even after we close the program.

Now, let's implement these functions.

### Saving to CSV

We'll start by creating a function to save our address book data to a CSV file. This function will take a filename as a parameter, and will use Python's `csv` module to write our address book data to this file.

Inside the function, we'll open the file in write mode using a `with` statement. This ensures that the file is properly closed after we're done with it, even if an error occurs. We're using the `"w"` mode with the `open()` function to open our file for writing, and we're also specifying `newline=''`. The latter is to ensure that no erroneous newline characters are inserted into the output, and is recommended when dealing with CSV files.

We'll then create a `csv.DictWriter` object, which will allow us to write our address book entries (which are dictionaries) directly to the CSV file. We'll provide the fieldnames (`'name'`, `'phone'`, and `'email'`) to the `DictWriter` so it knows what keys to expect in each dictionary.

We'll write the header row to the file using the `writeheader()` method, and then iterate over each entry in our address book, writing it to the file using the `writerow()` method.

Here's the code for our `save_to_csv()` function:

```python
def save_to_csv(filename: str):
    """Save the address book entries to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['name', 'phone', 'email'])
        writer.writeheader()  # Write the header to the CSV file
        for entry in address_book:
            writer.writerow(entry)  # Write each entry as a row in the CSV file
```

Here is the updated section of the tutorial about loading from CSV, incorporating the use of `extend()` instead of a loop with `append()`:

### Loading from CSV

Next, we'll create a function to load our address book data from a CSV file. This function will also take a filename as a parameter, and will use Python's `csv` module to read data from this file.

First, we'll check if the file exists using `os.path.exists()`. If it does, we'll open it in read mode.

We'll then create a `csv.DictReader` object, which will read each row of the CSV file as a dictionary. The keys of these dictionaries will be taken from the header row of the CSV file.

Before we start reading, we'll clear any existing entries in our address book using `address_book.clear()`. Then, instead of iterating over each row in the `DictReader` and appending them one by one, we can use the `extend()` method to add all the rows at once. 

`extend()` takes an iterable (a sequence of items, like a list or tuple) as an argument and adds each element of that iterable to the end of the list. In this case, the `DictReader` object is an iterable that yields a dictionary for each row in the CSV file. So by passing the `DictReader` directly to `extend()`, we're adding each of these dictionaries (each row from the CSV file) to our address book list in one step.

Here's the updated code for our `load_from_csv()` function:

```python
def load_from_csv(filename: str):
    """Load address book entries from a CSV file."""
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            address_book.clear()  # Clear existing entries before loading
            address_book.extend(reader)  # Load all entries from the CSV file at once
```

Using `extend()` here provides a slight performance boost compared to appending each row individually in a loop, especially for larger CSV files. It's a concise way to say "add all these elements to the end of the list".

### Integrating CSV Persistence

Now that we have functions to save and load our address book, let's integrate them into our program.

We'll load the address book from the CSV file at the start of our program, in the `main()` function:

```python
def main():
    """Main function to run the extended address book program."""
    load_from_csv("address_book.csv")  # Load entries from CSV file at the start
    # ... rest of the function ...
```

And we'll save the address book to the CSV file when the user chooses to exit:

```python
        elif choice == EXIT:
            save_to_csv("address_book.csv")
            print("Address book saved. Exiting program.")
            break
```

With these changes, our address book will now persist between sessions.

## Regular Expressions

[Regular expressions](https://en.wikipedia.org/wiki/Regular_expression) (often shortened to just "regex") are a powerful tool for pattern matching and manipulation of strings. They provide a concise and flexible way to search for patterns in text, validate input, and extract information from strings.

Regular expressions are not unique to Python - they are supported by many programming languages and tools, including Java, JavaScript, C#, Go, and even text editors like Visual Studio Code, Sublime Text and Notepad++. While the specific syntax for using regular expressions may differ slightly between languages, the core concepts and patterns are generally the same.

In Python, support for regular expressions is provided by the [built-in `re` module](https://docs.python.org/3/library/re.html). This module provides functions for searching strings for patterns, replacing text, and splitting strings based on patterns.

So, what does a regular expression look like? Here's a common example:

```
^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$
```

Now, this might _look_ like someone fell face-first onto the keyboard, but it's actually a pattern that matches email addresses:

- `^` asserts the start of the string.
- `[a-zA-Z0-9_.+-]+` matches one or more characters that can be alphanumeric, or one of the following: `_`, `.`, `+`, `-`. This is for the username part of the email.
- `@` matches the `@` character.
- `[a-zA-Z0-9-]+` matches one or more alphanumeric characters or `-`. This is for the domain name.
- `\.` matches a dot (full-stop). The backslash is used to escape the dot, which has a special meaning in regex.
- `[a-zA-Z0-9-.]+` matches one or more alphanumeric characters, `-`, or `.`. This is for the top-level domain (.com, .org, etc.).
- `$` asserts the end of the string.

We'll use this pattern in our program to validate email addresses. We'll also use a similar pattern to validate phone numbers:

```
^(?:0[2-8])(\d{8})$
```

Specifically, this pattern matches Australian phone numbers (just the regular ones, not 1800 or 1300 numbers):

- `^` asserts the start of the string.
- `(?:0[2-8])` is a non-capturing group that matches a `0` followed by a number from `2` to `8`. This is the area code.
- `(\d{8})` is a capturing group that matches exactly 8 digits (`\d` is shorthand for any digit).
- `$` asserts the end of the string.

Don't worry if this seems confusing at first. Regular expressions have a bit of a learning curve (there are [whole books on them](https://www.oreilly.com/library/view/mastering-regular-expressions/0596528124/)), but they're an incredibly useful tool once you get the hang of them. If you're interested in learning more, have a look at the following resources and tools:

- [Python's re module documentation](https://docs.python.org/3/library/re.html)
- [Regular Expression HOWTO](https://docs.python.org/3/howto/regex.html)
- [Regex tutorial on Real Python](https://realpython.com/regex-python/)
- [https://regex101.com/](https://regex101.com/) - Interactive regex testing tool
- [https://regexr.com/](https://regexr.com/) - Another tool similar to the above

## Validating Email Addresses and Phone Numbers

Now that we've implemented data persistence and understand the basics of regular expressions, let's use them to implement our data validation. We want to ensure that the email addresses and phone numbers entered by the user are in a valid format before we add them to the address book.

We'll create two functions: `validate_email()` and `validate_phone()`. These functions will take an email address or phone number as a parameter, and return `True` if it matches our expected format, `False` otherwise.

### Validating Email Addresses

Here's the code for our `validate_email()` function:

```python
def validate_email(email) -> bool:
    """Validate the format of an email address using regular expressions."""
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None
```

We use `re.match()` to check if the email matches the pattern we discussed earlier. It returns a match object if the string matches the pattern, or `None` if it doesn't. We return `True` if a match is found (`is not None`), `False` otherwise.

By the way, using `is` or `is not` this way to test **equality** is only appropriate when comparing to `None`. `None` is a special value, and all other cases should use `==` or `!=` instead.

### Validating Phone Numbers

Here's the code for our `validate_phone()` function:

```python
def validate_phone(phone) -> bool:
    """Validate the format of a phone number using regular expressions."""
    pattern = r"^(?:0[2-8])([0-9]{8})$"
    return re.match(pattern, phone) is not None
```

This function works similarly, but uses the phone number pattern from earlier instead.

### Integrating Validation

To use these two validation functions, we'll call them from our `add_entry()` function. If either the email or the phone number is invalid, we'll print an error message and return early, without adding the entry to the address book.

```python
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
```

And we're done. We've extended our address book program with data persistence and validation. Our contacts will now be saved between sessions (assuming we exit normally), and we can be sure that the email addresses and phone numbers we enter are in a valid format.
