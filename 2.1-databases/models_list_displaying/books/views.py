from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Book

def books_view(request):
    template = 'books/books_list.html'
    info = Book.objects.all()
    optional_page = request.GET.get('page', 1)
    info_pagi = Paginator(info, 2)
    page = info_pagi.get_page(optional_page)
    context = {'info': page, 'page': page}
    return render(request, template, context)



def bookss(request, pub_date):
    template = 'books/new_book.html'
    info = Book.objects.filter(pub_date=pub_date)
    context = {'info': info}
    return render(request, template, context)