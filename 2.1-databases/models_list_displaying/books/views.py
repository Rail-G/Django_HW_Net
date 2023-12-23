from django.shortcuts import render
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    info = Book.objects.all()
    context = {'info': info}
    return render(request, template, context)

def bookss(request, pub_date):
    template = 'books/new_book.html'
    info = Book.objects.filter(pub_date=pub_date).order_by('pub_date').all()
    info_next = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()
    info_previous = Book.objects.filter(pub_date__lt=pub_date).order_by('pub_date').last()
    context = {'info': info, 'next_info': info_next, 'previous_info': info_previous}
    return render(request, template, context)