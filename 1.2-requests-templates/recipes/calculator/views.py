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
def omlet(request, recipe, ):
    # template = loader.get_template('index.html')
    count = int(request.GET.get('servings', 1))
    ingredients = DATA.get(recipe, {})
    result = {key: round(value * count, 3) for key, value in ingredients.items()}
    print(result)
    context = {'recipe': result}
    return HttpResponse(render(request, 'calculator/index.html', context))

def main(request):
    pages = {
        'Главный омлет': reverse('omlet'),
        'Текущая паста': reverse('pasta'),
        'Твердый бутер': reverse('buter')
    }
    context = {'pages': pages}
    return HttpResponse(render(request, 'calculator/home.html', context))

