from models.book import *
import datetime

book1 = Book("The Rubiyat", "Omar Khayyam", "Poetry", True, datetime.date(2022, 9, 30))
book2 = Book("The Histories", "Herodotus", "History", False, False)
book3 = Book("The Satires", "Juvenal", "Latin Satire", True, datetime.date(2022, 10, 1))
books = [book1, book2, book3]

def add_new_book(book):
    books.append(book)

def delete_book(book_title):
    book_to_delete = None
    for book in books:
        if book.title == book_title:
            book_to_delete = book
            break
    books.remove(book_to_delete)






