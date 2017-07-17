import django
from apps.dojo_ninjas.models import Dojo, Ninja
from apps.book_authors.models import Book, Author

# create a new dojo
def new_dojo(name, city, state):
    return Dojo.objects.create(name=name, city=city, state=state)
    
# create a new ninja
def new_ninja(first_name, last_name, dojo_name):
    dojo = Dojo.objects.get(name=dojo_name)
    return Ninja.objects.create(first_name=first_name, last_name=last_name, dojo = dojo)

# all ninjas from the first dojo
def first_dojo_ninjas():
    ninjas = Dojo.objects.first().ninjas.all()
    for ninja in ninjas:
        print ninja.first_name, ninja.last_name

# all ninjas from the last dojo
def last_dojo_ninjas():
    ninjas = Dojo.objects.last().ninjas.all()
    for ninja in ninjas:
        print ninja.first_name, ninja.last_name

# create new book
def new_book(name, desc):
    return Book.objects.create(name=name, desc=desc)

# create new author
def new_author(first_name, last_name, email):
    return Author.objects.create(first_name=first_name, last_name=last_name, email=email)

# assign author to book
def author_book(author_first_name, author_last_name, book_name):
    book = Book.objects.get(name=book_name)
    author = Author.objects.get(first_name=author_first_name, last_name=author_last_name)
    book.authors.add(author)

# change the name of a book
def change_book_name(old_name, new_name):
    book = Book.objects.get(name=old_name)
    book.name = new_name
    book.save()
    return book

# change author's first name
def change_author_first_name(old_name, new_name):
    author = Author.objects.get(first_name=old_name)
    author.first_name=new_name
    author.save()
    return author

# get all authors of a book
def all_authors(book_name):
    book = Book.objects.get(name=book_name)
    authors = book.authors.all()
    for author in authors:
        print author.first_name, author.last_name

# remove the first author of a book
def remove_first_author(book_name):
    book = Book.objects.get(name=book_name)
    first_author = book.authors.first()
    book.authors.remove(first_author)
    return all_authors(book_name)

# get all books by an author
def all_books(author_first_name, author_last_name):
    author = Author.objects.get(first_name=author_first_name, last_name=author_last_name)
    books = author.books.all()
    for book in books:
        print book.name