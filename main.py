# make list of books
My_Books = []
# print Welcome message and image 
print("Welcome to the book nook.")
    # image
print("\nWelcome to...\n"
    "      ______ ______\n"
    "    _/      Y      \\_\n"
    "   // ~Book | ~~ ~  \\\n"
    "  // ~ ~ ~~ |  Nook~ \\\n"
    " //________.|.________\\\n"
    "`----------`-'----------'\n"
'')
# print out the commands
print("To add (add)")
print("To show (show)")
print("To remove (remove)")
print("To count (count)")
print("To quit (q)")
# ask user for what they wanna do (While Loop)

while True:
    user_input = input("What would you like to do?").lower().strip()                  
    # Add
        # ask for book 
    if user_input == "add":
        book_name = input("Which book would you like to add?")
        (book_name.isalpha())
        # add to list 
        My_Books.append(book_name)
        # success message
        print("Book has been successfully added.")

    # Show 
        # print out list with numbers
    elif user_input == "show":
        for count, item in enumerate (My_Books, start=1):
            print(f"{count}. {item}")
    # Remove 
    elif user_input == "remove":
        # ask for book
        book_name2 = input("Which book would you like to remove?")
        (book_name2.isalpha())
        # remove the book
        My_Books.remove(book_name2)
        # success message
        print("Book has been successfully removed.") 
        # Book remove error message
        if book_name2 not in My_Books:
            print("Book is not avaliable in Book Nook.")
    # Count 
    elif user_input == "count":
        # print out the message with count number
        print(len(My_Books)) 
        print("book(s)")
    # Quit
    else:
        user_input == ("quit")
        print("Goodbye, thanks for visiting the Book Nook!")
        break
