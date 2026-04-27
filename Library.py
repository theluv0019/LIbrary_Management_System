books = []
issued_books = []
def add_book():
    book = input("Enter book name: ")
    books.append(book)
    print(book,'is added to the library')
def show_books():
    if len(books) == 0:
        print("No books in the library")
    else:
        print("Books in the library:")
        for book in books:
            print(book)
def issue_book():
    book = input("Enter book name to issue: ")
    if book in books:
        books.remove(book)
        issued_books.append(book)
        print(book,'is issued')
    else:
        print(book,'is not available in the library')
def return_book():                  
    book = input("Enter book name to return: ")
    if book in issued_books:
        issued_books.remove(book)
        books.append(book)
        print(book,'is returned')
    else:
        print(book,'is not issued from the library')

def library_menu():
    while True:
        print("\nLibrary Menu:")
        print("1. Add Book")
        print("2. Show Books")
        print("3. Issue Book")
        print("4. Return Book")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_book()
        elif choice == '2':
            show_books()
        elif choice == '3':
            issue_book()
        elif choice == '4':
            return_book()
        elif choice == '5':
            print("Exiting the library system.")
            break
        else:
            print("Invalid choice. Please try again.")
library_menu()