from django.shortcuts import render
from django_pandas.io import read_frame # this
from books.models import Book
from users.models import UserProfile
import pandas as pd

# This function display an index of all books for user
def books_index(request):
    books = Book.objects.all()
    if (request.user.is_authenticated):
        if request.user.userprofile.age < 18 :
            books= Book.objects.filter(genre='CH')
    books_df = read_frame(books)
    print(books_df)

    context = {
        'books': books
    }
    return render(request, 'books_index.html', context)

# this function gets a bookid and display its full details

def book_detail(request, pk):
    book = Book.objects.get(pk=pk)
    context = {
        'book': book
    }
    return render(request, 'book_detail.html', context)