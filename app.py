import json
import os

# Data file name
DATA_FILE = "library_data.json"

# 📌 Load data from the file
def load_library():
    if not os.path.exists(DATA_FILE):
        return []
    
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []

# 📌 Save data to the file
def save_library(library):
    with open(DATA_FILE, "w") as f:
        json.dump(library, f, indent=4)

# 📌 Add a book
def add_book():
    library = load_library()
    title = input("📖 Book Title: ").strip()
    author = input("✍️ Author Name: ").strip()

    while True:
        try:
            year = int(input("📅 Publication Year: ").strip())
            if year > 2025:  # Future years not allowed
                print("⚠️ Invalid year! Please enter a past or current year.")
                continue
            break
        except ValueError:
            print("⚠️ Please enter a valid numeric year!")

    genre = input("📚 Genre: ").strip()
    read_status = input("📖 Have you read this book? (yes/no): ").strip().lower() == "yes"

    book = {
        "title": title,
        "author": author,
        "year": year,
        "genre": genre,
        "read_status": read_status
    }
    
    library.append(book)
    save_library(library)
    print(f"✅ '{title}' added successfully!")

# 📌 View all books
def view_books():
    library = load_library()
    if not library:
        print("⚠️ No books available!")
        return

    print("\n📚 Your Library:\n")
    for idx, book in enumerate(library, start=1):
        status = "✅ Read" if book['read_status'] else "❌ Unread"
        print(f"{idx}. {book['title']} - {book['author']} ({book['year']}) | {book['genre']} | {status}")
    print()

# 📌 Search for a book
def search_book():
    library = load_library()
    keyword = input("🔎 Search by title or author: ").strip().lower()
    
    found_books = [book for book in library if keyword in book['title'].lower() or keyword in book['author'].lower()]
    
    if not found_books:
        print("❌ No books found!")
        return
    
    print("\n📖 Search Results:\n")
    for book in found_books:
        status = "✅ Read" if book['read_status'] else "❌ Unread"
        print(f"{book['title']} - {book['author']} ({book['year']}) | {book['genre']} | {status}")
    print()

# 📌 Update book details
def update_book():
    library = load_library()
    view_books()
    
    try:
        book_index = int(input("🔄 Enter book number to update: ")) - 1
        if book_index < 0 or book_index >= len(library):
            print("⚠️ Invalid selection!")
            return

        book = library[book_index]
        book['title'] = input(f"📖 New Title ({book['title']}): ").strip() or book['title']
        book['author'] = input(f"✍️ New Author ({book['author']}): ").strip() or book['author']
        
        while True:
            try:
                new_year = input(f"📅 New Year ({book['year']}): ").strip()
                if new_year:
                    new_year = int(new_year)
                    if new_year > 2025:
                        print("⚠️ Invalid year! Enter a past or current year.")
                        continue
                    book['year'] = new_year
                break
            except ValueError:
                print("⚠️ Please enter a valid numeric year!")

        book['genre'] = input(f"📚 New Genre ({book['genre']}): ").strip() or book['genre']
        book['read_status'] = input(f"📖 Mark as read? (yes/no): ").strip().lower() == "yes"

        save_library(library)
        print("✅ Book updated successfully!")
    
    except ValueError:
        print("⚠️ Please enter a valid number!")

# 📌 Delete a book
def delete_book():
    library = load_library()
    view_books()
    
    try:
        book_index = int(input("🗑️ Enter book number to delete: ")) - 1
        if book_index < 0 or book_index >= len(library):
            print("⚠️ Invalid selection!")
            return

        deleted_book = library.pop(book_index)
        save_library(library)
        print(f"✅ '{deleted_book['title']}' deleted successfully!")
    
    except ValueError:
        print("⚠️ Please enter a valid number!")

# 📌 Show library statistics
def show_statistics():
    library = load_library()
    total_books = len(library)
    if total_books == 0:
        print("📊 No books available!")
        return

    read_books = sum(1 for book in library if book['read_status'])
    percentage_read = (read_books / total_books) * 100

    print("\n📊 Library Statistics:")
    print(f"📚 Total Books: {total_books}")
    print(f"✅ Read Books: {read_books}")
    print(f"📖 Read Percentage: {percentage_read:.2f}%\n")

# 📌 Show menu options
def show_menu():
    while True:
        print("\n📚 Personal Library Manager")
        print("1️⃣ Add a Book")
        print("2️⃣ View All Books")
        print("3️⃣ Search for a Book")
        print("4️⃣ Update a Book")
        print("5️⃣ Delete a Book")
        print("6️⃣ Show Statistics")
        print("7️⃣ 🔴 Exit")

        choice = input("\n🔘 Select an option: ").strip()
        
        if choice == "1":
            add_book()
        elif choice == "2":
            view_books()
        elif choice == "3":
            search_book()
        elif choice == "4":
            update_book()
        elif choice == "5":
            delete_book()
        elif choice == "6":
            show_statistics()
        elif choice == "7":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Please select a valid option!")

# 📌 Run the program
if __name__ == "__main__":
    show_menu()
