books = []
def add_book() :
    book_id = input("Enter book ID : ")
    title = input("Enter book Title : ")
    author = input("Enter author name : ")
    quantity = int(input("Enter Quantity : "))

    book = {
        "ID" : book_id,
        "Title" : title,
        "Author" : author,
        "Quantity" :  quantity
    }

    books.append(book)
    print("book added successfully")

def view_books() :
    if len(books) == 0 :
        print("No book available")
    else :
        for book in books :
            print(book)

def search_book() :
    book_id = input("enter book id to search : ")

    for book in books :
        if book["id"] == book_id :
            print("book found")
            print(book)
            return
        print("book not  found")

def update_book() :
    book_id = input("Enter book id to update : ")
    for book in books :
        if book[id] == books :
            new_quantity = int(input("enter new quantity to update : "))
            book["Quantity"] = new_quantity
            print("book quantity updated")
            return
        print("book not found")

def delete_book() :
    book_id = input("Enter book id to delete : ")
    for book in books :
        if book[id] == books :
            books.remove(book)
            print("book deleted successfully")
            return
        print("book not found")

while True:
    print("\n===== BOOK INVENTORY SYSTEM =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Update Book Quantity")
    print("5. Delete Book")
    print("6. Exit")

    choice = int(input("enter your choice : "))

    if choice == 1 :
        add_book()

    elif choice == 2 :
        view_books()

    elif choice == 3 :
        search_book()

    elif choice == 4 :
        update_book()

    elif choice == 5 :
        delete_book()

    elif choice == 6 :
        print("thank you!")
        break

    else :
        print("invalid choice")



      


