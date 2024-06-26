import sqlite3

# Connect to the database (or create it if it doesn't exist)
db = sqlite3.connect('ebookstore.db')

# Create a cursor object to interact with the database
cursor = db.cursor()

# Create the book table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS book (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        Title TEXT NOT NULL, Author TEXT NOT NULL,
        Qty INTEGER
    )
''')

# Define the rows to be inserted
rows_to_insert = [
    (3001, 'A Tale of Two Cities', 'Charles Dickens', 30),
    (3002, 'Harry Potter and the Philosopher\'s Stone', 'J.K Rowling', 40),
    (3003, 'The Lion, The Witch, and The Wardrobe', 'C.S Lewis', 25),
    (3004, 'The Lord of the Rings', 'J.R.R Tolkien', 37),
    (3005, 'Alice in Wonderland', 'Lewis Caroll', 12)
]

# Insert multiple rows into the PythonProgramming table
cursor.executemany('''
    INSERT INTO book (ID, Title, Author, Qty)
    VALUES (?, ?, ?, ?)
''', rows_to_insert)


# Funcion to add new book
def add_new_book(ID, Title, Author, Qty):
    cursor.execute("INSERT INTO book (ID, Title, Author, Qty) VALUES (?, ?, ?, ?)", (ID, Title, Author, Qty))
    db.commit()
    print(f"Book '{Title}' by {Author} added to the library database.")


# Function to update book info
def update_book_info(ID, Title, Author, Qty):
    cursor.execute("UPDATE book SET title = ?, author = ?, qty = ? WHERE id = ?", (Title, Author, Qty, ID))
    db.commit()
    print(f"Book ID {ID} updated to title '{Title}', author '{Author}', and quantity '{Qty}'.")
    

# Function to delete a book
def delete_book_by_name(name):
    cursor.execute("DELETE FROM book WHERE title = ?", (name,))
    db.commit()
    print(f"Book with title '{name}' has been deleted from the library database.")


# Function to find/search for a book
def find_book(search_term):
    cursor.execute("SELECT * FROM book WHERE title LIKE ? OR author LIKE ?", ('%' + search_term + '%', '%' + search_term + '%'))
    books = cursor.fetchall()
    if not books:
        print(f"No books found for search term '{search_term}'.")
    else:
        for book in books:
            print(f"{book[0]}. {book[1]} by {book[2]}, Quantity: {book[3]}")

# Display menu function
def display_menu():
    print("\nMenu:")
    print("1. Enter book")
    print("2. Update book")
    print("3. Delete book")
    print("4. Search books")
    print("0. Exit")


# Main Function
def main():
    try:
        while True:
            display_menu()
            choice = input("Enter your choice: ")

            if choice == '1':
                ID = input("Enter book ID: ")
                Title = input("Enter book title: ")
                Author = input("Enter book author: ")
                Qty = input("Enter book quantity: ")
                add_new_book(ID, Title, Author, Qty)
            elif choice == '2':
                ID = input("Enter book ID to update: ")
                Title = input("Enter new title: ")
                Author = input("Enter new author: ")
                Qty = input("Enter new quantity: ")
                update_book_info(ID, Title, Author, Qty)
            elif choice == '3':
                name = input("Enter the title of the book to delete: ")
                delete_book_by_name(name)
            elif choice == '4':
                search_term = input("Enter a search term (title or author): ")
                find_book(search_term)
            elif choice == '0':
                break
            else:
                print("Invalid choice. Please try again.")
    finally:
        db.close()


if __name__ == "__main__":
    main()
