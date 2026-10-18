from django.shortcuts import render, redirect
from .models import Book, Author

def index(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'books.html', context)

def create_book(request):
    if request.method == 'POST':
        Book.objects.create(
            title=request.POST['title'],
            description=request.POST['description']
        )
    return redirect('/')

def book_detail(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book,
        'all_authors': Author.objects.exclude(books=book)
    }
    return render(request, 'book_detail.html', context)

def add_author_to_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        author = Author.objects.get(id=request.POST['author_id'])
        book.authors.add(author)
    return redirect(f'/books/{book_id}')

def edit_book(request, book_id):
    book = Book.objects.get(id=book_id)
    context = {
        'book': book
    }
    return render(request, 'edit_book.html', context)

def update_book(request, book_id):
    if request.method == 'POST':
        book = Book.objects.get(id=book_id)
        book.title = request.POST['title']
        book.description = request.POST['description']
        book.save()
    return redirect(f'/books/{book_id}')

def delete_book(request, book_id):
    book = Book.objects.get(id=book_id)
    book.delete()
    return redirect('/')

def authors_view(request):
    context = {
        'authors': Author.objects.all()
    }
    return render(request, 'authors.html', context)

def create_author(request):
    if request.method == 'POST':
        Author.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            notes=request.POST['notes']
        )
    return redirect('/authors')

def author_detail(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        'author': author,
        'all_books': Book.objects.exclude(authors=author)
    }
    return render(request, 'author_detail.html', context)

def add_book_to_author(request, author_id):
    if request.method == 'POST':
        author = Author.objects.get(id=author_id)
        book = Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{author_id}')

def edit_author(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        'author': author
    }
    return render(request, 'edit_author.html', context)

def update_author(request, author_id):
    if request.method == 'POST':
        author = Author.objects.get(id=author_id)
        author.first_name = request.POST['first_name']
        author.last_name = request.POST['last_name']
        author.notes = request.POST['notes']
        author.save()
    return redirect(f'/authors/{author_id}')

def delete_author(request, author_id):
    author = Author.objects.get(id=author_id)
    author.delete()
    return redirect('/authors')