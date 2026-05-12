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
    user_input = input("What would you like to do?")    
    # Add
        # ask for book 
    if user_input.lower() == "add":
        book_name = input("Which book would you like to add?")
        # add to list 
        My_Books.append(book_name.isalpha())
        # success message
        print("Book has been successfully added.")

    # Show 
        # print out list with numbers
    elif user_input.lower() == "show":
        for count, item in enumerate (My_Books, start=1):
            print(f"{count}. {item}")
    # Remove 
    elif user_input.lower() == "remove":
        # ask for book
        book_name2 = input("Which book would you like to remove?")
        # remove the book
        My_Books.remove(book_name2.isalpha())
        # success message
        print("Book has been successfully removed.") 
    # Count 
    elif user_input.lower() == "count":
        # print out the message with count number
        print(len(My_Books)) 
        print("book(s)")
    # Quit
    else:
        user_input.lower() == ("quit")
        print("Goodbye, thanks for visiting the Book Nook!")
        break
