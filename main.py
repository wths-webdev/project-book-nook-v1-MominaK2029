# make list of books
My_Books = []
# print Welcome message and image 
print("Welcome to the book nook.")
    # image
# print out the commands
print("To add (add)")
print("To show (show)")
print("To remove (remove)")
print("To count (count)")
print("To quit (quit)")
# ask user for what they wanna do (While Loop)
user_input = input("What would you like to do?")
while True:

    # Add
        # ask for book 
    if user_input == "add":
        book_name = input("Which book would you like to add?")
        # add to list 
        My_Books.append(book_name)
        # success message
        print("Book has been successfully added.")

    # Show 
        # print out list with numbers
    elif user_input == "show":
        print (My_Books)
    # Remove 
        # ask for book
        book_name2 = input("Which book would you like to add?")
        # remove the book
        My_Books.remove()
        # success message
        print("Book has been successfully removed.") 

    # Count 
        # print out the message with count number

    # Quit
    else:
        print("Goodbye, thanks for visiting the Book Nook!")
        break
