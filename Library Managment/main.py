
print("\n-----Welcome to Saraswati Library-----\n")

class Book:
    def __init__(self, book_id, title, author):
        self.book_id = book_id
        self.title = title
        self.author = author

    def show(self):
        print(f"{self.book_id} : {self.title} : {self.author}")

def get_valid_id(number):
    while True:
        try:
            raw = input(number)
            if not raw:
                print("Book-unique-id can not be blank......")
                continue
            return int(raw)
        except KeyboardInterrupt:
            print("\nPlease re-enter book-unique-id")
        except ValueError:
            print("Please enter a valid number")

class Library:
    def __init__(self):
        self.books = []
        self.load_from_file()

    def load_from_file(self):                         # loads data from books.txt to self.books
        self.books = []                       
        try:
            with open("books.txt", "r") as f:
                for line in f:
                    book_id, title, author = line.strip().split(" : ")
                    self.books.append(Book(int(book_id), title, author))
        except FileNotFoundError:
            print("\nfile not found !!\n")
    
    def save_to_file(self):                         # saves self.books to books.txt
        with open("books.txt", "w") as f:
            for i in self.books:
                f.write(f"{i.book_id} : {i.title} : {i.author}\n")


    def add_book(self):                         # adds book's data from user
        while True:
            try:
                raw = input("Enter book-unique-id: ")
                if not raw:
                        print("Unique-book-id can not be blank.....")
                        continue
                book_id = int(raw)
                for i in self.books:
                    if i.book_id==book_id:
                        print(f"\nThere is already a book with book-unique-id '{book_id}'...... so we can't add this id again\n")
                        return
                break
            except KeyboardInterrupt:
                print("\nPlease re-enter the book-unique-id\n")
                continue
            except ValueError:
                print("Please enter a valid number\n")
                continue
            except Exception as e:
                print("Unexpected error: ", e)
        while True:
            try:
                title = input("Enter book title: ").title()
                if not title:
                        print("Book title can not be blank.....")
                        continue
                break               
            except KeyboardInterrupt:
                print("\nPlease re-enter book title\n")
                continue
        while True:
            try:
                author = input("Enter author name: ").title()
                if not author:
                        print("Author name can not be blank.....")
                        continue
                break
            except KeyboardInterrupt:
                print("\nPlease re-enter author name\n")
                continue
        self.books.append(Book(int(book_id), title, author))
        self.save_to_file()
        print("\nAddtion completed\n")
        input("\nPress enter to return to menu.......")

    def search_book(self):                         # shows data of selected book_id
        user = get_valid_id("Enter unique-book-id: ")          
        for book in self.books:
            if book.book_id==user:
                print(f"\nHere the book info-\nName of book -{book.title}\nName of author -{book.author}\n")
                input("\nPress enter to return to menu.......")
                return
        print("\nNo book found !!\n")
        input("\nPress enter to return to menu.......")

    def view_all_books(self):                         # shows all books information
        print("\n")
        if not self.books:
            print("No book available !!")
            input("\nPress enter to return to menu.......")
            return
        print("\n")
        for i in self.books:
            print(f"Id - {i.book_id} : Title - {i.title} : Author - {i.author}")
        input("\nPress enter to return to menu.......")


    def delete_book(self):                         # deletes all data of selected book_id 
        user = get_valid_id("Enter unique-book-id: ") 
        updated_list = []
        found = False
        for i in self.books:
            if i.book_id==user:
                found = True
            else:
                updated_list.append(i)
        if found:
            self.books = updated_list
            print(f"Book with book-unique-id {user} deleted successfully.")
        elif found == False:
            print(f"There is no book with book-unique-id {user}")
        self.save_to_file()
        input("\nPress enter to return to menu.......")

    def update_book(self):                         # updates title & author name of selected book_id
        user = get_valid_id("Enter unique-book-id: ")  
        book_to_update = None
        for i in self.books:
            if i.book_id == user:
                book_to_update = i
                break
        if not book_to_update:
            print(f"No books found with book-unique-id {user} !!")
            input("\nPress enter to return to menu.......")
        elif book_to_update:
            print(f"The current title of book-unique-id {user} is '{book_to_update.title}' and author is '{book_to_update.author}'") 
            while True:
                try:
                    new_title = input("Enter new book title: ").title()
                    if not new_title:
                        print("Book title can not be blank.....")
                        continue
                    break               
                except KeyboardInterrupt:
                    print("\nPlease re-enter new book title\n")
                    continue
            book_to_update.title = new_title
            while True:
                try:
                    new_author = input("Enter new author name: ").title()
                    if not new_author:
                        print("Author name can not be blank.....")
                        continue
                    break
                except KeyboardInterrupt:
                    print("\nPlease re-enter new author name\n")
                    continue
            book_to_update.author = new_author
            self.save_to_file()
            print(f"Book-unique-id {user} has updated")
            input("\nPress enter to return to menu.......")

    
manager = Library()
    
def menu():
    while True:
        print('''\nHere are the options-
1. Add Book
2. Search Book (by book-unique-id)
3. View All Books
4. Delete Book (by book-unique-id)
5. Update Book's Title & Author (by book-unique-id)
6. Exit from libary''')
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
        elif choice==2:
            manager.search_book()
        elif choice==3:
            manager.view_all_books()
        elif choice==4:
            manager.delete_book()
        elif choice==5:
            manager.update_book()
        elif choice==6:
            print("\nExiting from library..........\n\n\n")
            break

menu()


















