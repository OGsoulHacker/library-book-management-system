# Library book management system

# Initialize the library dictionary and borrowed_books list
# The `library` dictionary will store information about books available in the library.
# The keys in the `library` dictionary will be book IDs (integers).
# The values in the `library` dictionary will be another dictionary containing book details (title, author, quantity).
library = {}

# The `borrowed_books` list will keep track of books that have been borrowed.
# Each entry in the `borrowed_books` list will be a dictionary containing the book ID, borrower name, and borrow date.
borrowed_books = []
#=======================================================================================================================
#Define function add_book()
    #passes in book_id,title, author, quantity
def add_book(book_id, title, author, quantity):
    """Add a new book to the library or update the quantity if the book already exists."""
    # Check if the book ID already exists in the library
    if book_id in library:
        # If the book ID exists, update the quantity of the book by adding the new quantity to the existing quantity
        library[book_id]['quantity'] += quantity
        print(f"Updated quantity of '{title}'.")
    else:
        # If the book ID does not exist, add the book to the library with its details (title, author, quantity)
        library[book_id] = {'title': title, 'author': author, 'quantity': quantity}
        print(f"Added book '{title}' by {author} with ID {book_id}.")

#Define remove_book() function
    #passes in book_id
def remove_book(book_id):
    """Remove a book from the library by its ID."""
    # Check if the book ID exists in the library
    if book_id in library:
        # If the book ID exists, delete the book from the library dictionary
        del library[book_id]
        print(f"Removed book with ID {book_id}.")
    else:
        # If the book ID does not exist, print an error message
        print(f"Book with ID {book_id} does not exist.")

#Define search_book() function
    #passes in keyword
def search_book(keyword):
    """Search for books by title or author, returning a list of matching book IDs."""
    # Initialize an empty list to store matching book IDs
    matching_books = []
    # Iterate through each book in the library
    for book_id, details in library.items():
        # Check if the keyword is in the book title or author (case-insensitive)
        if keyword.lower() in details['title'].lower() or keyword.lower() in details['author'].lower():
            # If a match is found, add the book ID to the matching_books list
            matching_books.append(book_id)
    # Return the list of matching book IDs
    return matching_books

#Define display_inventory() function
def display_inventory():
    """Display the entire library inventory, sorted by book ID."""
    # Check if the library is empty
    if not library:
        # If the library is empty, print a message indicating that
        print("The library inventory is empty.")
    else:
        # Iterate through the sorted book IDs
        for book_id in sorted(library.keys()):
            # Get the details of the book for the current book ID
            details = library[book_id]
            # Print the book ID, title, author, and quantity
            print(f"ID: {book_id}, Title: '{details['title']}', Author: {details['author']}, Quantity: {details['quantity']}")

#Define borrow_book() function
    #passes in book_id, borrower_name, borrow_date
def borrow_book(book_id, borrower_name, borrow_date):
    """Add an entry to the borrowed_books list and decrease the quantity of the book in the library."""
    # Check if the book ID exists in the library and if the quantity of the book is greater than 0
    if book_id in library and library[book_id]['quantity'] > 0:
        # Decrease the quantity of the book by 1
        library[book_id]['quantity'] -= 1
        # Add the borrowed book details to the borrowed_books list
        borrowed_books.append({'book_id': book_id, 'borrower_name': borrower_name, 'borrow_date': borrow_date})
        print(f"Book with ID {book_id} borrowed by {borrower_name} on {borrow_date}.")
    else:
        # If the book is out of stock or does not exist, print an error message
        print(f"Book with ID {book_id} is out of stock or does not exist.")

#Define return_book() function
    #passes in book_id
def return_book(book_id):
    """Remove an entry from the borrowed_books list and increase the quantity of the book in the library."""
    # Iterate through the borrowed_books list
    for entry in borrowed_books:
        # Check if the book ID matches the current entry's book ID
        if entry['book_id'] == book_id:
            # Remove the borrowed book entry from the borrowed_books list
            borrowed_books.remove(entry)
            # Increase the quantity of the book in the library by 1
            library[book_id]['quantity'] += 1
            print(f"Book with ID {book_id} has been returned.")
            return
    # If no record of the book being borrowed is found, print an error message
    print(f"No record of book with ID {book_id} being borrowed.")

#define menu function
def menu():
    """Simple menu-driven interface to interact with the library system."""
    while True:
        # Display the menu options
        print("\nLibrary Menu:")
        print("1. Add a book")  # Option to add a new book
        print("2. Remove a book")  # Option to remove an existing book
        print("3. Search for a book")  # Option to search for a book by title or author
        print("4. Display inventory")  # Option to display the entire library inventory
        print("5. Borrow a book")  # Option to borrow a book from the library
        print("6. Return a book")  # Option to return a borrowed book
        print("7. Exit")  # Option to exit the library system

        # Get the user's choice from the menu options
        choice = input("Enter your choice (1-7): ")

        # If the user chooses option 1: Add a book
        if choice == '1':  # Check if the user's choice is '1'
            try:
                # Get book details from the user
                book_id = int(
                    input("Enter book ID: "))  # Prompt the user to enter the book ID and convert it to an integer
                title = input("Enter book title: ")  # Prompt the user to enter the book title
                author = input("Enter book author: ")  # Prompt the user to enter the book author
                quantity = int(input(
                    "Enter quantity: "))  # Prompt the user to enter the quantity of the book and convert it to an integer
                # Add the book to the library by calling the add_book function
                add_book(book_id, title, author, quantity)
            except ValueError:  # Handle invalid input error
                print(
                    "Invalid input. Please enter numeric values for book ID and quantity.")  # Print an error message if input is not valid

        # If the user chooses option 2: Remove a book
        elif choice == '2':  # Check if the user's choice is '2'
            try:
                # Get the book ID to remove from the user
                book_id = int(input(
                    "Enter book ID to remove: "))  # Prompt the user to enter the book ID to remove and convert it to an integer
                # Remove the book from the library by calling the remove_book function
                remove_book(book_id)
            except ValueError:  # Handle invalid input error
                print(
                    "Invalid input. Please enter a numeric value for book ID.")  # Print an error message if input is not valid

        # If the user chooses option 3: Search for a book
        elif choice == '3':  # Check if the user's choice is '3'
            # Get the search keyword from the user
            keyword = input(
                "Enter keyword to search (title or author): ")  # Prompt the user to enter a keyword to search for books
            # Search for matching books by calling the search_book function
            matching_books = search_book(keyword)
            if matching_books:  # Check if there are any matching books
                # Display matching books
                for book_id in matching_books:  # Iterate through the list of matching book IDs
                    details = library[book_id]  # Get the details of each matching book
                    print(
                        f"ID: {book_id}, Title: '{details['title']}', Author: {details['author']}, Quantity: {details['quantity']}")  # Print the details of each matching book
            else:
                print("No matching books found.")  # Print a message if no matching books are found

        # If the user chooses option 4: Display inventory
        elif choice == '4':  # Check if the user's choice is '4'
            # Display the library inventory by calling the display_inventory function
            display_inventory()

        # If the user chooses option 5: Borrow a book
        elif choice == '5':  # Check if the user's choice is '5'
            try:
                # Get book details and borrower information from the user
                book_id = int(input(
                    "Enter book ID to borrow: "))  # Prompt the user to enter the book ID to borrow and convert it to an integer
                borrower_name = input("Enter borrower's name: ")  # Prompt the user to enter the borrower's name
                borrow_date = input("Enter borrow date (YYYY-MM-DD): ")  # Prompt the user to enter the borrow date
                # Borrow the book by calling the borrow_book function
                borrow_book(book_id, borrower_name, borrow_date)
            except ValueError:  # Handle invalid input error
                print(
                    "Invalid input. Please enter a numeric value for book ID.")  # Print an error message if input is not valid

        # If the user chooses option 6: Return a book
        elif choice == '6':  # Check if the user's choice is '6'
            try:
                # Get the book ID to return from the user
                book_id = int(input(
                    "Enter book ID to return: "))  # Prompt the user to enter the book ID to return and convert it to an integer
                # Return the book by calling the return_book function
                return_book(book_id)
            except ValueError:  # Handle invalid input error
                print(
                    "Invalid input. Please enter a numeric value for book ID.")  # Print an error message if input is not valid

        # If the user chooses option 7: Exit the library system
        elif choice == '7':  # Check if the user's choice is '7'
            # Exit the library system
            print("Exiting the library system. Goodbye!")  # Print a goodbye message
            break  # Exit the loop and end the program

        # If the user enters an invalid choice
        else:
            # Handle invalid menu choice
            print(
                "Invalid choice. Please enter a number between 1 and 7.")  # Print an error message for invalid menu choice


# Start the library system by calling the menu function
menu()