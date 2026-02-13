
class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author
    def __str__(self):
        return(f"{self.book_id} : {self.title} : {self.author}")


def get_valid_id():
    while True:
        try:
            raw = input("Enter ID: ")
            if not raw.strip():
                print("ID can not be empty !!")
                continue
            user = int(raw)
            return user
        except KeyboardInterrupt:
            print("\nPLease re-enter ID")
            continue
        except ValueError:
            print("Please enter a valid number")
            continue
        except Exception as e:
            print("Unexpected error: ", e)
            continue

def get_valid_string(field_name):
    while True:
        try:
            user = input(f"Enter {field_name}: ").strip()
            if not user.strip():
                print(f"{field_name.capitalize()} can not be empty !!")
                continue
            return user
        except KeyboardInterrupt:
            print(f"\nPLease re-enter {field_name}")
            continue
        except Exception as e:
            print("Unexpected error: ", e)
            continue


class Library:
    def __init__(self):
        self.books = []
        self.load_from_file()

    def load_from_file(self):
        self.books = []
        try:
            with open ("books.txt", "r") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue    
                    book_id, title, author = line.split(" | ")
                    self.books.append(Book(int(book_id), title, author))
        except FileNotFoundError:
            print("File not found")
        except Exception as e:
            print("Unexpected error: ", e)

    def save_to_file(self):
        with open ("books.txt", "w") as f:
            for book in self.books:
                f.write(f"{book.book_id} | {book.title.title()} | {book.author.title()}\n")

    def add_book(self):
        while True:
            book_id = get_valid_id()
            for book in self.books:
                if book.book_id == book_id:
                    print(f"There is already a book with ID {book_id}")
                    return
            break
        title = get_valid_string("title")
        author = get_valid_string("author")
        self.books.append(Book(int(book_id), title, author))
        self.save_to_file()
        print("\nAddition completed")

    def search_book(self):
        book_id = get_valid_id()
        for book in self.books:
            if book.book_id == book_id:
                print(f"\nHere's the book information-\nTitle: {book.title}\nAuthor: {book.author}")
                return
        print(f"\nNo book find with ID {book_id} !!")

    def view_all_books(self):
        if not self.books:
            print("\nNo book found !!")
            return
        print("\n")
        for book in self.books:
            print(f"ID - {book.book_id} | Title - {book.title} | Author - {book.author}")
        
    def delete_book(self):
        book_id = get_valid_id()
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                self.save_to_file()
                print("Deletion completed")
                return
        print(f"\nThere is no book with ID {book_id}")

    def update_book(self):
        book_id = get_valid_id()
        book_to_update = None
        for book in self.books:
            if book.book_id == book_id:
                book_to_update = book
                break
        if book_to_update:
            print(f"\nThe current title is '{book_to_update.title}' and the author is '{book_to_update.author}'\n")
            book_to_update.title = get_valid_string("New title")
            print("Title got updated\n")
            book_to_update.author = get_valid_string("New author")
            print("Author got updated")
            self.save_to_file()
        else:
            print(f"\nNo book found with ID  {book_id}")


  
manager = Library()

def menu():
    while True:
        print('''\nHere are the options-
1. Add Book
2. Search Book (by book-unique-id)
3. View All Books
4. Delete Book (by book-unique-id)
5. Update Book's Title & Author (by book-unique-id)
6. Exit from library''')
        while True:
            try:
                choice = int(input("\nEnter your choice here: "))
                if choice<1 or choice>6:
                    print("\nPlease enter a valid choice (1-6)")
                    continue
                break
            except KeyboardInterrupt:
                print("\n\nPlease re-enter your choice")
                continue
            except Exception:
                print("\nPlease enter a valid choice")
        if choice==1:
            manager.add_book()
            input("\nPress enter to return to menu.......")
        elif choice==2:
            manager.search_book()
            input("\nPress enter to return to menu.......")
        elif choice==3:
            manager.view_all_books()
            input("\nPress enter to return to menu.......")
        elif choice==4:
            manager.delete_book()
            input("\nPress enter to return to menu.......")
        elif choice==5:
            manager.update_book()
            input("\nPress enter to return to menu.......")
        elif choice==6:
            print("\nExiting from library..........\n\n\n")
            break

menu()

