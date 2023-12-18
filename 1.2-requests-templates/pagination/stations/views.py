from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.paginator import Paginator
import csv


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    list_ = []
    with open('data-398-2018-08-30.csv', newline='', encoding='utf-8') as file:
        read = csv.DictReader(file, delimiter=',')
        for i in read:
            list_.append({'Name': i['Name'], 'Street': i['Street'], 'District': i['District']})
    optional_page = int(request.GET.get('page', 1))
    paginator = Paginator(list_, per_page=10)
    page = paginator.get_page(optional_page)
    context = {
        'bus_stations': page,
        'page': page
    }
    return render(request, 'stations/index.html', context)
