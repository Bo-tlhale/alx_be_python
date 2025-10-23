class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class EBook(Book):
    def __init__(self, title, author, filesize):
        super().__init__(title, author)
        self.filesize = filesize
               
class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title, author)
        self.page_count = page_count
        
class Library:
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def list_books(self):
        for book in self.books:
            if book.__class__.__name__ == "EBook":
                print(f"EBook: {book.title} by {book.author}, File Size: {book.filesize}KB")
            elif book.__class__.__name__ == "PrintBook":
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")