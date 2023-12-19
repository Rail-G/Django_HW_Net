from django.shortcuts import render
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    info = Book.objects.all()
    context = {'info': info}
    return render(request, template, context)

