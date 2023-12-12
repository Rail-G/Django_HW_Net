from django.http import HttpResponse
from django.shortcuts import render, reverse
import pytz
from datetime import datetime
import os


def home_view(request):
    template_name = 'app/home.html'
    # впишите правильные адреса страниц, используя
    # функцию `reverse`
    pages = {
        'Главная страница': reverse('home_view'),
        'Показать текущее время': reverse('time_view'),
        'Показать содержимое рабочей директории': reverse('workdir_view')
    }
    
    # context и параметры render менять не нужно
    # подбробнее о них мы поговорим на следующих лекциях
    context = {
        'pages': pages
    }
    return render(request, template_name, context)


def time_view(request):
    time = datetime.now()
    tz = pytz.timezone('Etc/Gmt-3')
    current_time = tz.localize(time)
    current_time = current_time.astimezone(tz).strftime('%d/%B/%Y %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)


def workdir_view(request):
    dirs = os.listdir(path='.')
    new_dir = []
    for i in dirs:
        if '.' not in i:
            new_dir.append(f'{i}/')
        else:
            new_dir.append(i)

    return HttpResponse(' -> '.join(new_dir))
