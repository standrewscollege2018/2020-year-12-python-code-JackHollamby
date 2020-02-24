#this is the list of the books
bookstore = [["Harry Potter", "J.K Rowling", 20], ["Percy Jackson", "Rick Riordon", 25], ["Dracula", "Bram Stoker", 30]]
repeat = True
#while loop will make it infinite unless the user stops the program
while repeat == True:
    choice = input('''Hello! If you want to view the list of books, type view. If you want
to add a book to the list, type add. if you want to delete a book, type delete. If you want to end the program, type end.''')
    if choice == "view":
        print(bookstore)
    elif choice == "end":
        repeat == False
    elif choice == "add":
        name = input("Please enter a name")
        author = input("Please entere an author")
        price = int(input("Please enter a price"))
        addition = [name, author, price]
        bookstore.append(addition) 
 
