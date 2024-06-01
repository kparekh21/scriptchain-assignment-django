from django.shortcuts import render
from django.db.models import Q
from .models import Book, Author, Publisher

def books_select(request):
    books = Book.objects.all()
    return render(request, 'library/books.html', {'books': books})

def books_select_related(request):
    books = Book.objects.select_related('author', 'publisher')
    return render(request, 'library/books.html', {'books': books})

def books_prefetch_related(request):
    books = Book.objects.prefetch_related('author', 'publisher')
    return render(request, 'library/books.html', {'books': books})

def books_with_q_objects(request):
    # Books where the title contains 'Book' or the author's name is 'Author One'
    books = Book.objects.filter(Q(title__icontains='Book') & Q(author__name='Author One'))
    return render(request, 'library/books.html', {'books': books})


def books_without_q_objects(request):

    books_with_title = Book.objects.filter(title__icontains='Book')
    authors = Author.objects.filter(name='Author One')
    books_with_author = Book.objects.filter(author__in=authors)

    books = books_with_title & books_with_author
    books = books.distinct()

    return render(request, 'library/books.html', {'books': books})
