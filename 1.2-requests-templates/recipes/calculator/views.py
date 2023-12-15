from django.shortcuts import render, reverse
from django.http.response import HttpResponse

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}
def omlet(request):
    # template = loader.get_template('index.html')
    count = int(request.GET.get('servings', 1))
    context = {'recipe': {
        'макароны, г': round(0.3 * count, 2),
        'сыр, г': round(0.05 * count, 3)
        }
    }
    return HttpResponse(render(request, 'calculator/index.html', context))

def pasta(request):
    # template = loader.get_template('index.html')
    count = int(request.GET.get('servings', 1))
    context = {'recipe': {
        'яйца, шт': 2 * count,
        'молоко, л': round(0.1 * count, 2),
        'соль, ч.л.': round(0.5 * count, 2)
        }
    }
    return HttpResponse(render(request, 'calculator/index.html', context))

def buter(request):
    # template = loader.get_template('index.html')
    count = int(request.GET.get('servings', 1))
    context = {'recipe': {
        'хлеб, ломтик': 1 * count,
        'колбаса, ломтик': 1* count,
        'сыр, ломтик': 1* count,
        'помидор, ломтик': 1* count,
        }
    }
    return HttpResponse(render(request, 'calculator/index.html', context))

def main(request):
    pages = {
        'Главный омлет': reverse('omlet'),
        'Текущая паста': reverse('pasta'),
        'Твердый бутер': reverse('buter')
    }
    context = {'pages': pages}
    return HttpResponse(render(request, 'calculator/home.html', context))